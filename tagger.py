import numpy as np
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestCentroid

# set the client and relevance threshold
client = ""
relevance_threshold = 75

# load in the content embeddings
print(f"Loading the content with embeddings...")
content_embeddings_df = pd.read_json("/home/jupyter/ai/data/{client}/{client}_content_embeddings.jsonl", lines=True)
# columns of content_embeddings_df are 'content' and 'embeddings'

# extract the 'embedding' from the 'embedding' object
content_embeddings_df['embedding'] = content_embeddings_df['embedding'].apply(lambda x: x['embedding'])
content_embeddings_df['embedding'] = content_embeddings_df['embedding'].apply(np.array)

# truncate the content description to 100 characters
content_embeddings_df['content'] = content_embeddings_df['content'].str[:100]

# load in the taxonomy report as a DataFrame
print(f"Loading the tags with embeddings...")
keyword_df = pd.read_json(f"/home/jupyter/ai/data/{client}/{client}_taxonomy_keywords.jsonl", lines=True)


# columns of the dataframe: ['id', 'archived', 'type', 'percolate', 'description', 'alchemist_embedding_nomic-embed-text-v1.5-768']

# define a function to find the 10 nearest neighbors based on cosine similarity
def find_nearest_neighbors(content_embedding, tag_embeddings, n_neighbors=10):
    cos_similarities = cosine_similarity(content_embedding.reshape(1, -1), tag_embeddings).flatten()
    top_n_indices = np.argsort(cos_similarities)[-n_neighbors:][::-1]
    top_n_similarities = cos_similarities[top_n_indices]
    return top_n_indices, top_n_similarities


# define a function to calculate relevance score
def calculate_relevance_score(cosine_similarity):
    return (cosine_similarity + 1) * 50


# define a function to tag the documents locally
def tag_documents(content_embeddings_df, keyword_df, relevance_threshold, n_neighbors=10):
    tag_embeddings = np.vstack(keyword_df['alchemist_embedding_nomic-embed-text-v1.5-768'].values)
    tag_ids = keyword_df['id'].values

    applied_tags = []  # Store the list of tags applied to each document
    tag_counts = []  # Store the count of tags applied to each document

    for idx, row in content_embeddings_df.iterrows():
        content_embedding = row['embedding']

        # find the 10 nearest tags by cosine similarity
        top_n_indices, top_n_similarities = find_nearest_neighbors(content_embedding, tag_embeddings)

        # filter tags by relevance score
        valid_tags = []
        for i in range(n_neighbors):
            relevance_score = calculate_relevance_score(top_n_similarities[i])
            if relevance_score >= relevance_threshold:
                valid_tags.append(tag_ids[top_n_indices[i]])

        applied_tags.append(valid_tags)  # add the valid tags for this document
        tag_counts.append(len(valid_tags))  # count the number of tags and add to tag_counts list

    # add results as new columns in the DataFrame
    content_embeddings_df['assigned_tags'] = applied_tags
    content_embeddings_df['num_applied_tags'] = tag_counts

    return content_embeddings_df

# apply the tagging function
print(f"Tagging the content...")
content_embeddings_df = tag_documents(content_embeddings_df, keyword_df, relevance_threshold)