# generating a truth table fpr p ^ q

values = [False, True]

for p in values:
    for q in values:
        print(p,q, p and q, p or q, not p, not q, not p or q, p == q)