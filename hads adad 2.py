import random

n_U = 0
n_pcmin = 0
n_pcmax = 100
n_pc = random.randint(1, 100)
print ('Is it', n_pc, '?')
h_l = 'Idk'
y_n = input()
while y_n != 'yes':
    h_l = input ('Higher or Lower?')
    if h_l == 'higher':
        n_pcmin = n_pc
        n_pc = random.randint(n_pc, n_pcmax)
    elif h_l == 'lower':
        n_pcmax = n_pc
        n_pc = random.randint(n_pcmin, n_pc)
    print ('Is it', n_pc, '?')
    y_n = input()
print ('Ezzzzzzz...')