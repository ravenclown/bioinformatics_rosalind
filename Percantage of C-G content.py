def perc_calc(s):
    gc = s.count("G")+s.count("C")
    at = s.count("A")+s.count("T")
    total = at+gc
    gc_frac = float(gc) / float(total)
    return 100*gc_frac