from random import randint

figure = ['rock', 'scissors', 'paper']
a = input('Print rock or scissors or paper. If u wanna stop game - print exit\n')
b = figure[randint(0,2)]
while a in figure:
    print(f'PC choose - {b}')
    if a == b:
        print('Make another one!')
    elif a == 'rock':
        if b == 'scissors':
            print('U win!')
        else:
            print('Sorry, U lose, try again!')
    elif a == 'scissors':
        if b == 'paper':
            print('U win!')
        else:
            print('Sorry, U lose, try again!')
    elif a == 'paper':
        if b == 'rock':
            print('U win!')
        else:
            print('Sorry, U lose, try again!')  
    a = input()
    b = figure[randint(0,2)]
print('See u!')
