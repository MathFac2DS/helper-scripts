from smart_open import open

# set the file path
file_path = "/home/jupyter/ai/data/{client}/{client}_content_embeddings.jsonl"

for idx, _ in enumerate(open(file_path)):
     if (idx+1) % 50000 == 0:
          print(idx+1)
print(f'There are {idx+1} embeddings in the file from {file_path}.')