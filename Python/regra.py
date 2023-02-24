def  regraJogo(obj1, obj2):
    if obj1 != obj2:
        try:
            if int(obj1) == 1 and (int(obj2) == 3 or int(obj2) == 5):
                print('Jogador 1 Ganhou!')

            elif int(obj1) == 2 and (int(obj2) == 4 or int(obj2) == 1):
                print('Jogador 1 Ganhou!')

            elif int(obj1) == 3 and (int(obj2) == 2 or int(obj2) == 5):
                print('Jogador 1 Ganhou!')

            elif int(obj1) == 4 and (int(obj2) == 3 or int(obj2) == 1):
                print('Jogador 1 Ganhou!')

            elif int(obj1) == 5 and (int(obj2) == 2 or int(obj2) == 4):
                print('Jogador 1 Ganhou!')
            else:
                print("Jogador 1 perdeu!")
        except:
            if str(obj1) == 'Pedra' or str(obj1) == 'pedra' and (str(obj2) == 'Tesoura' or 
              (str(obj2) == 'tesoura' or str(obj2) == 'Lagarto' or str(obj2) == 'lagarto')):
                print('Jogador 1 Ganhou!')

            elif str(obj1) == 'Papel' or str(obj1) == 'papel' and (str(obj2) == 'Spock' or
                 str(obj2) == 'spock' or str(obj2) == 'Pedra' or str(obj2) == 'pedra'):
                print('Jogador 1 Ganhou!')

            elif str(obj1) == 'Tesoura' or str(obj1) == 'tesoura' and (str(obj2) == 'Papel' or 
                 str(obj2) == 'papel' or str(obj2) == 'Lagarto' or str(obj2) == 'lagarto'):
                print('Jogador 1 Ganhou!')

            elif str(obj1) == 'Spock' or str(obj1) == 'spock' and (str(obj2) == 'Tesoura' or 
                 str(obj2) == 'tesoura' or str(obj2) == 'Pedra' or str(obj2) == 'pedra'):
                print('Jogador 1 Ganhou!')

            elif str(obj1) == 'Lagarto' or str(obj1) == 'lagarto' and (str(obj2) == 'Papel' or 
                 str(obj2) == 'papel' or str(obj2) == 'Spock' or str(obj2) == 'spock'):
                print('Jogador 1 Ganhou!')
            else:
                print("Jogador 1 perdeu!")
    else:
        print("Empate")