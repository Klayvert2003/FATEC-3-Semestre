from regra import regraJogo

print('Escolha duas Opções:')
print("""1 - Pedra
2 - Papel
3 - Tesoura
4 - Spock
5 - Lagarto""")

obj1 = input()
obj2 = input()

regraJogo(obj1, obj2)