import os

folder_name = "test_data/en/"
corpus_file = "test_data/en/corpus.txt"

os.makedirs(folder_name, exist_ok=True)

with open(corpus_file, 'r', encoding='utf-8') as corpus:
    corpus_lines = corpus.readlines()

lines_per_chunk = 400

# split the corpus into 400 line chunks
chunks = [corpus_lines[i:i + lines_per_chunk] for i in range(0, len(corpus_lines), lines_per_chunk)]

# write each chunk into the respective 0.txt to 19.txt files
for i, chunk in enumerate(chunks):
    file_path = os.path.join(folder_name, f"{i}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(chunk)

print("corpus split and written to files successfully!")