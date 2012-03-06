likef = 0.9
priorf = 0.001
liken = 0.1
priorn = 0.999

nonF = likef * priorf #pbar(f|b)
nonN = liken * priorn #pbar(n|b)
pF = nonF / (nonF+nonN) #p(f|b)
pN = nonN / (nonF+nonN) #p(n|b)

print nonF
print nonN
print pF
print pN
