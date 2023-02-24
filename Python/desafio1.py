def caixamagica(n1, n2):
    if n1 <= n2:
        return 0
    return n1 - n2
        
assert caixamagica(20, 10) == 10

print(caixamagica(20,10))