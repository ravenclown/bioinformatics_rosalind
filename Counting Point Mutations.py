s1 = 'ATAGCAGGCTTACGGTATACATTCTTGACTTTATAGCGTACTCGCTTTCTCGTCGCATCGGTTACGTACGTGTCATCCGATGGTTCCAATGGGATATTGCAGATAAATGATCTTCCTGTACAAAACATCTATGGTATTGGCACGGATGTCGCGTATAGAGGCTCTCTTCGATGAATATGGTCGCCGTACGACTATTTGCACGCCACCCGCGGTTAAGCCCCCAATACCCGGCGGAGTTGGTTCAGAATAAGCCCCCCGCCATACCCAGAGCCTCGCCGTCTTGTAATAGTGACTGCACAATCCTTGCCTATGTTCAGTGCCACCCTCCGTGTACTGAGAGTGGGTATATAGACCGAGTTGCAAGATATCGGTGTGCACTTGCCATTAAAGGGCCGTCTACCGAGGCACAAGGGCTTCCCGGCCTTGCTCAATTTAATGCTACAACCCTTGGGGAGCGTTACCGGCTGCCGTGACCGCGTAAACTCGGCAGTTAGGTTTTTCGCGCCGGACTCCTAGACTCATATGAGTTTATGACGTCACAAGTAGGAATTAGAGCGGCGCTGGATGACGCAAAGAAACTCTCCTACGAAATATAGCAACGAAAGCCTCAGTCTTCTGTACGTGATCTTTCAAAGTGGTGTCAACACAAGCGCCCGTCACGGTCTGCACGCCATTCAGTTCGCAGTTGTCGAGCGGCCGAATGGTGGTCGGTGCTACTAAGCCTGGGGGCGAAGATCGGATTACCTGTCTATGTTTCATTCGGCGAGCCCGCGAGTTACCGGGACCCCTTTCATGGCTAGCAAGCCTCCTAATAAAGTGATCTTACTGGTTTGACATTCTGCATTCTAAACTCATTCTGAATATCTTGTGTTCATACACGCACGGGGTAAGAAGTTTAGGGACTGCCAGTAGGCGAAGCTCCGCGTGACGCACAGTACACTACTTATCCACAGGTCGAAGATAATATTTTGTCTAC'
s2 = 'GGATTTAACCGATGGTGCACATGTGCGCCTTTATCCCGTTGGGCGAATTTCGCCGTATATCGGCCGTAAGTGTCTTCCTAGACACAATGTGCAAGACCGTTCCTAGCAGGAGTACCCTTATAGTGTATGTGTCGTGCTGACACTGGCGGCGGGGAAAAAAGATATCCTGAGAAAAGATTGAAGCCTAACGGTGCTTTGAACGTCGCTAGTACGGTAGTCCAGCAGAAACGGGCGCTTTGTGTAGGGGTAAGAACGGCTCCATTGCCTAGGGCGCTACGGCAGATTCACCTTATTAAACCCGCCAGGCGAATGAGCAATCTCCGCGTTCATGAAGAGCGATCGCGTTAGGTGGGCAAGGTTCGAGTTATCTATAGACTGCCTCCAAACATGTGTGAGGCCCGTTTGCAAGAGGGGTTTGCGCGCTCGTTCAACTCAAGGCTTCAGCCCTTAACACAGGTCAGGGGCAGATCCAAACGGGCTAAGTCTGGCGTCCGGTCTTCCTCGTCGTTTTAATTACCACGGACGTGAATGGCTCGCCGAAGCTGGTAGGTATAGCGTTACAAAGTTACCAAGAGGGAGGCCCCAAGGTAATGCCATACCGATTGGATAAAGGGGTCGTACGAGGGCATCCACAGTCATGTCGACTCAATTCCGCGTCACGGTCTGCCAGCCGTTGCATAGAGGCTAAGATAACGACACAACGGGGAGGGAAGGTACTAACAGCGGGTACATATACAAAAACTCTAGGCTTAGGACGAATCGATCACCCTAGCAACGTCGGTGTTCCTCTCTATCGATCCCGAGCGTAACAGCCCCGTGTCCTTCCTGATTTTATGCTCTCTGTTAGACAGTGACTCTTAACACATGGCGGTAGGAAAATGGAGGGCTACACATTTTAGTGAAAGTAAGCCGTACATACATACGGAGTACTACAGTAAACCATTTTTCCCACATGCCAGGAGTATACTATCCCACC'
Hamming = 0
for x in range(len(s1)):
    if s1[x] != s2[x]:
        Hamming += 1
print(Hamming)
