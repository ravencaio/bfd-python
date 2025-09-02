cas_vaz = [['   '] for c in range(8)]
inicio_pretas = [['tor'],['cav'],['bis'],['rai'],['rei'],['bis'],['cav'],['tor']]
inicio_peoes = [['pea'] for c in range(8)]
inicio_brancas = inicio_pretas.copy()[::-1]

for c in range(6):
    if c == 0:    
        print(inicio_pretas)
        print(inicio_peoes)
        continue
    if c == 5:
        print(inicio_peoes)
        print(inicio_brancas)
        break
    print(cas_vaz)
    
