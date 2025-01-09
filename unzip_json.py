import gzip
import shutil

# set the client, input and output file paths
client = ""
CLIENT = ""
input_file = '/home/jupyter/ai/data/{client}/{CLIENT}_corpus.jsonl.gz'
output_file = '/home/jupyter/ai/data/{client}/{client}_corpus.jsonl'

# Open the gzip file and write its content to the output file
with gzip.open(input_file, 'rt', encoding='utf-8') as gz_file:
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        shutil.copyfileobj(gz_file, jsonl_file)

print(f"File '{input_file}' has been successfully unzipped to '{output_file}'.")