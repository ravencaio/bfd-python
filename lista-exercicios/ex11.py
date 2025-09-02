cas_vaz = [['   '] for c in range(8)]
inicio_peças = [['tor'],['cav'],['bis'],['rai'],['rei'],['bis'],['cav'],['tor']]
inicio_peoes = [['pea'] for c in range(8)]

for c in range(6):
    if c == 0:    
        print(inicio_peças)
        print(inicio_peoes)
        continue
    if c == 5:
        print(inicio_peoes)
        print(inicio_peças[::-1])
        break
    print(cas_vaz)
    
