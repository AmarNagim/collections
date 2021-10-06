# Amar Nagim
# F1.6.01.L1

import random
import time

def mm(amount):
    #colors
    oranje = 0
    blauw = 0
    groen = 0
    bruin = 0
    times=0
    colors = ['oranje', 'blauw', 'groen', 'bruin']
    print(f'\nDe zak bestaat uit {amount} m&m\'s. De kleur van elke van deze m&m\'s is:')
    for colorAssignment in range (amount):  
        times+=1
        randomChoice = random.randint(0,3)
        mmrandom = print(str(times) + '.', colors[randomChoice])
        if randomChoice in [0]:
            oranje += 1
        elif randomChoice in [1]:
            blauw += 1
        elif randomChoice in [2]:
            groen += 1
        elif randomChoice in [3]:
            bruin += 1                    
    bag = {
        'oranje': oranje,
        'blauw': blauw,
        'groen': groen,
        'bruin': bruin
    }
    print('')
    print (bag)
    return bag

howMany = int(input('Hoeveel m&m\'s wil je in de zak?: '))

mm(howMany)    









# times=0
# colors = ['oranje', 'blauw', 'groen', 'bruin']

# howMany = int(input('Hoeveel m&m\'s wil je in de zak?: '))
# print(f'\nDe zak bestaat uit {howMany} m&m\'s. De kleur van elke van deze m&m\'s is:')
# for colorAssignment in range (howMany):  
#     times+=1
#     print(str(times) + '.', colors[random.randint(0,3)])