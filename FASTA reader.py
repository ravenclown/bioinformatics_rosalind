import sys

fasta = {}
file_one = open("file.txt", "r")
for line in file_one:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        active_sequence_name = line[1:]
        if active_sequence_name not in fasta:
            fasta[active_sequence_name] = []
        continue
    sequence = line
    fasta[active_sequence_name].append(sequence)

print(fasta)
