k = 26  # homozygous dominant YY
m = 24  # heterozygous Yy
n = 15  # homozygous recessive yy
total = k + m + n

total_prob = total * (total - 1)

recessive = (n * (n - 1)) + float((m * (m - 1) * 0.25)) + 2 * (float((n * m * 0.5)))

print(recessive)

dominant = total_prob - recessive

print(dominant)

print(dominant / total_prob)
