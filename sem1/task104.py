#Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
#(то есть разломить шоколадку на два прямоугольника).

n= int(input('введите число n:'))
m= int(input('введите число n:'))
k= int(input('введите число n:'))
if(k%n==0 and k<(n*m)) or (k%m ==0 and k<(m*n)):
    print ('yes')
else:
    print('no')