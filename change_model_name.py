import json

# set the client
client = ""

# file paths
input_file_path = "/home/jupyter/ai/data/{client}/{client}_content_embeddings_base.jsonl"
output_file_path = "/home/jupyter/ai/data/{client}/{client}_content_embeddings.jsonl"

# New model name
new_model_name = "nomic-embed-text-v1.5"

# process the JSONL file
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        if line.strip():  # skip empty lines
            row = json.loads(line)  # parse the JSON object
            if "embedding" in row and "model_name" in row["embedding"]:  # check keys
                row["embedding"]["model_name"] = new_model_name  # update model name
            json.dump(row, outfile)  # write the updated row to output file
            outfile.write("\n")  # add a newline for each JSON object

print(f"Updated file saved to {output_file_path}")