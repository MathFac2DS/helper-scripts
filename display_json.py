N = 2

# file_path = "/home/jupyter/ai/data/aipp/aipp_content_embeddings_tuned.jsonl"
# # model_name = "alchemist_embedding_lodestone-v3-client-768"

# file_path = "/home/jupyter/ai/data/aipp/aipp_content_embeddings_base.jsonl"
# # model_name = "alchemist_embedding_lodestone-v3-base-768"

# file_path = "/home/jupyter/ai/data/aipp/aipp_content_embeddings_base2.jsonl"
# # model_name = "nomic-ai/nomic-embed-text-v1.5" # this is the model_name in create_config.ipynb, but not the model_name

# file_path = "/home/jupyter/ai/data/annex/annex_content_embeddings.jsonl"
# # model_name = "nomic-embed-text-v1.5" # match this one for use in the regular process

# file_path = "/home/jupyter/ai/data/rup2.0/rup_content_embeddings.jsonl"
# # model_name = "nomic-embed-text-v1.5"
# # rows are objects of the form {"content": "description of content", "embedding": {"model_name" = "nomic-embed-text-v1.5", "embedding": [...]}}

# file_path = "/home/jupyter/ai/data/rup2.1.1/rup_content_embeddings.jsonl"
# # rows are objects of the form {"content": "description of content", "embedding": {"model_name" = "nomic-embed-text-v1.5", "embedding": [...]}}

file_path = "/home/jupyter/ai/data/tandf/tandf_augmented_candidates.jsonl"

with open(file_path) as f:
    for i in range(0, N):
        line = f.readline()
        print(line)