gen = str(input())
p = gen.upper().count('g'.upper())
a = gen.upper().count('c'.upper())
print((p + a) / len(gen) * 100)
