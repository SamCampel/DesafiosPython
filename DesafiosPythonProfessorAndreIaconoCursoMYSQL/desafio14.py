print('LOOP COM BREAK: ')
for i in range(1,11):
    if i > 5:
        break
    print(i)
    
print('LOOP COM CONTINUE: ')
for j in range(1,11):
    if j == 5:
        continue
    print(j)