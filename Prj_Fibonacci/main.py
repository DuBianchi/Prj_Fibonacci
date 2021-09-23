print('='*50)
print('Sequencia Fibonacci')
print('='*50)

# Código principal
vqtde = int(input('Quantas vezes você quer repetir: '))
t1 = 0
t2 = 1

# o contador começa em 3 porque ja mostrei 2 posições
count = 3
t3 = 0
print('{} - {} - '.format(t1,t2) , end = '')

while count <= vqtde:
    t3 = t1 + t2
    print('{} - '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1

print('Fim')