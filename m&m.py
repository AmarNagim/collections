# Amar Nagim
# F1.6.01.L1

import random
import time

times=0
colors = ['oranje', 'blauw', 'groen', 'bruin']

howMany = int(input('Hoeveel m&m\'s wil je in de zak?: '))
print(f'\nDe zak bestaat uit {howMany} m&m\'s. De kleur van elke van deze m&m\'s is:')
for colorAssignment in range (howMany):  
    times+=1
    print(str(times) + '.', colors[random.randint(0,3)])