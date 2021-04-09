def perc_calc(s):
    gc = at = 0
    for word in s:
        if word in ['A', 'T', 'a', 't']:
            at += 1
        if word in ['G', 'C', 'g', 'c']:
            gc += 1
    total = float(at + gc)
    gc_over_total = float(gc / total)
    gc_perc = gc_over_total * 100
    print("AT = %d , GC = %d , Total = %d , GC / Total = %f , Perc = %f" % (at, gc, total, gc_over_total, gc_perc))
    x = ((gc * 100) / (gc + at))
    return x


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

results = {}
h_perc = 0
for line in fasta:
    perc = perc_calc(str(fasta.get(line)))
    results.update({perc: line})
    if perc > h_perc:
        h_perc = perc
print(results[h_perc])
print(h_perc)
