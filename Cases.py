'''Крисяк Михаил Игоревич'''

#Глава №1


print('Пpoвepкa интерпретатора Python.')

#Глава №2

#num1
print ("""Михаил Игоревич.
Где-то,Там, 23123.
Номер: 89183078915.
Некто,программинг.""")

#num2
balans = input("Введите плановую сумму продаж: ")
Itog = 0.23 * float(balans)
print ('Итоговая прибыль составляет $' , format (Itog, '.2f') , sep='')

#num3
qr = input ('Впришите общее количество кв. метров: ')
agr = float(qr) / 4047
print ('Колличество акров земли:', format (agr, '.2f'))


#num4

tovar1 = float(input('Введите цену первого товара: '))
tovar2 = float(input('Введите цену второго товара: '))
tovar3 = float(input('Введите цену третьего товара: '))
tovar4 = float(input('Введите цену четвертого товара: '))
tovar5 = float(input('Введите цену пятого товара: '))

sum = tovar1 + tovar2 + tovar3 + tovar4 + tovar5
nalog = sum * 0.07
total = nalog + sum

print ('Сумма товаров равна: ', sum)
print('Налог на товар равен:', nalog)
print('Итоговая цена на товар: ', total)

#num5
speed = 70
time = 6
distance = speed * time
print('Пройденое расстояние машиной за 6 часов равно', distance)
time = 10
distance = speed * time
print('Пройденое расстояние машиной за 10 часов равно', distance)
time = 15
distance = speed * time
print('Пройденое расстояние машиной за 15 часов равно', distance)

#num6
price = float(input('Введите величину покупки: '))
reg = 0.025
fed = 0.05
print('Сумма покупки:', price)
nalog1 = price * reg
print('Региональный налог:', format(nalog1, '.1f'))
nalog2 = price * fed
print('Федеральный налог:', format(nalog2, '.1f'))
obsh = nalog1 + nalog2
print('Общий налог:', format(obsh, '.1f'))
itogi = float(price) + obsh
print('Общая сумма покупки:', format(itogi, '.1f'))

#num7
distance = float(input('Ведите пройденные километры: '))
fuel = float(input('Введите расход бензина: '))
coast = distance / fuel
print('Рассход бензина равен', format(coast, '.1f'))

#num8
price1 = float(input('Введите величину покупки: '))
tips = 0.18
procent = 0.07
print('Сумма заказа:', price1)
Pchai = price1 * tips
print('Чаевые:', format(Pchai, '.1f'))
Pprocent = price1 * procent
print('Налог:', format(Pprocent, '.1f'))
obsh1 = Pchai + Pprocent
print('Общий налог:', format(obsh1, '.1f'))
itog = float(price1) + obsh1
print('Итоговая сумма оплаты:', format(itog, '.1f'))

#num9

celsius = float(input('Введите температуру по шкале Цельсия: '))
forengeit = (9/5) * celsi + 32
print ('Температура по шкале Фаренгейта:', format(forengeit, '.1f'))

#num10
pies = float(input('Сколько булочек вы хотите приготовить? '))
glassca = 1.5 * (pies / 48)
glassma = 1.0 * (pies/ 48)
glassmy = 2.75 * (pies / 48)
print ('Вам понадобиться', format(glassca, '.1f'), 'стаканов сахара')
print ('Вам понадобиться', format(glassma, '.1f'), 'стаканов масла')
print ('Вам понадобиться', format(glassmy, '.1f'), 'стаканов муки')

#num11
boys = float(input('Сколько парней в группе? '))
girls = float(input('Сколько девушек в группе? '))
all = boys + girls
boysp = boys / vse
girlsp = girls / vse
print('Процент парней в группе ', format(boysp, '.0%'))
print('Процент девушек в группе ', format(girlsp, '.0%'))

#num12
akc = 2000.0 * 40.00
proc = akc * 0.03
akc1 = 2000.0 * 42.75
proc1 = akc1 * 0.03
itog = (akc+proc) - (akc1+proc1)
print('сумма уплаченая за покупку акций', akc,
    '\n комиссия при покупке', proc,
    '\n сумма уплаченая за прождажу акций', akc1,
    '\n комиссия при продаже', proc1,
    '\n Итог махинаций Джо', itog )

#num13
R = float(input('Введите длину гряды, в метрах: '))
E = float(input('Введите размер пространства в метрах, занимаемых концевыми опорами: '))
S = float(input('Введите размер пространства между виноградными лозами в метрах: '))
V = (R - (2 * E)) / S
print('Количество виноградных лоз, которые поместятся на гряде:', format(V, '.2f'))

#num14
P = float(input('Введите основную сумму, которая была внесена на счет в начале: '))
r = float(input('Введите годовую процентную ставка: '))
n = float(input('Введите частоту начисления процентного дохода(кол-во месяцев в год): '))
t = float(input('Введите конкретное количество лет: '))
r = r / 100
A = P * ((1+(r/n))**n*t)
print ('Сумма денег на счете после конкретного количества лет:', format(A, '.2f'))


#num15 POTOM
import turtle
turtle.forward(200)
turtle.
'''

#Глава №3
"""
#num1

nubmir = int(input('Введите число то 1 до 7: '))

if numbir == 7:
    print ('воскресенье')
elif numbir == 6:
    print ('суббота')
elif numbir == 5:
    print ('пятница')
elif numbir == 4:
    print ('четверг')
elif numbir == 3:
    print ('среда')
elif numbir == 2:
    print ('вторник')
elif numbir == 1:
    print ('понедельник')
else:
    print('Ошибка, введите число в диапозоне от 1 до 7')

#num2
width1 = int(input('Введите ширину первого прямоугольника: '))
length1 = int(input('Введите длину первого прямоугольника: '))
width2 = int(input('Введите ширину второго прямоугольника: '))
length2 = int(input('Введите длину второго прямоугольника: '))
perimeter1 = width1 * length1
perimeter2 = width2 * length2
if perimeter1 < perimeter2:
    print ('периметр первого прямоугольника меньше второго')
elif perimeter1 > perimeter2:
    print ('периметр первого прямоугольника больше второго')
else:
    print ('периметры прямоугольников равны')

#num3
age = float(input('Введите возраст: '))
if 0 < age < 1:
    print('младенец')
elif 1 < age < 13:
    print ('ребенок')
elif 13 < age < 20:
    print ('подросток')
elif age > 20:
    print ('взрослый')

#num4
numbir1 = int(input('Введите число то 1 до 10: '))

if numbir1 == 10:
    print ('X')
elif numbir1 == 9:
    print ('IX')
elif numbir1 == 8:
    print ('VIII')
elif numbir1 == 7:
    print ('VII')
elif numbir1 == 6:
    print ('VI')
elif numbir1 == 5:
    print ('V')
elif numbir1 == 4:
    print ('IV')
elif numbir1 == 3:
    print ('III')
elif cheslo1 == 2:
    print ('II')
elif numbir1 == 1:
    print ('I')
else:
    print('Ошибка, введите число в диапозоне от 1 до 10')

#num5
weight = float(input('Введите массу тела: '))
ves = weight * 9.8
if ves < 100:
    print ('Вес тела слишком маленький')
elif ves > 500:
    print ('Вес тела слишком большой')
else:
    print ('Вес тела составляет: ', format (ves, '.0f'))

#num6
#POTOM
#num7
print('Вводите цвет с маленькой буквы, без знаков препинания и пробелов.')
col2 = str(input('Введите первый цвет: '))
col1 = str(input('Ввседите второй цвет: '))
if col2 == 'красный' and col1 == 'синий':
    print ('фиолетовый')
elif col2 == 'красный' and col1 == 'желтый':
    print('оранжевый')
elif col2 == 'синий' and col1 == 'желтый':
    print('зеленый')
else:
    print('Ошибка, вы ввели не привильный цвет')

#num8
hot = int(input('Введите количество хот-догов: '))
guests = int(input('Введите количество гостей: '))
vse = guests * hot
sos = 1
byl = 1
#hot = sos + byl
sosp = ((sos * 10) / vse)
bylp= ((byl * 8) / vse)

print ('количество пачек сосисок: ', sosp,
    '\n количество пачек булочек: ', bylp,)
print

#num9
num = int (input('Ввидите число от 0 до 36: '))
if 0<num<=10 and chislo%2 or 11<=num<=18 and chislo!=num%2 or 19<=chislo<=28 and num%2 or 29<=num<=36 and num%2:
    print ('красный')
elif 0<num<10 and num%2==0 or 10<num<18 and num%2==0 or 19<=num<=28 and num%2==0 or 29<=num<=36 and num%2==0:
    print ('черный')
elif num == 0:
    print ('зеленый')
else:
    print ('Ошибка, введите правильное число')


#num10
print ('Введите количествол своих монет')
five = int(input('Сколько у вас 5 копеечных монет? '))
ten = int(input('Сколько у вас 10 копеечных монет? '))
fifty = int(input('Сколько у вас 50 копеечных монет? '))
#vfive = five * 5
#vten = (ten * 10)
#vfifty = (fifty * 50)
money = (five * 5) + (ten * 10) + (fifty * 50)
if money == 100:
    print ('Поздавляю у вас рубль! Вы выйграли зачет.')
elif money > 100:
    print ('У вас больше рубля, вы ни чего не выйграли.')
else:
    print ('У вас меньше рубля, вы ни чего не выйграли.')

#num11
books = int(input ('Введите количество купленных книг: '))
if 0 <= books < 2:
    print('Вы получили 0 очков за купленные книги')
elif 2 <= books < 4:
    print('Вы получили 5 очков за купленные книги')
elif 4 <= books < 6:
    print('Вы получили 15 очков за купленные книги')
elif 6 <= books < 8:
    print('Вы получили 30 очков за купленные книги')
elif 8 <= books:
    print('Вы получили 60 очков за купленные книги')
else:
    print('Ошибка ввода')


#num12
pak = float(input('Введите количество купленных программных пакетов: '))
price = pak * 99.0
discount1 = price * 0.1
price1 = price * 0.9
discount2 = price * 0.2
price2 = price * 0.8
discount3 = price * 0.3
price3 = price * 0.7
discount4 = price * 0.4
price4 = price * 0.6
if 10 <= pak <= 19:
    print('Ваша скидка равняется ', discount1,
    '\n Итоговая цена: ', price1)
elif 20 <= pak <= 49:
    print('Ваша скидка равняется ', discount2,
    '\n Итоговая цена: ', price2)
elif 50 <= pak <= 99:
    print('Ваша скидка равняется ', discount3,
    '\n Итоговая цена: ', price3)
elif 100 <= pak:
     print('Ваша скидка равняется ', discount4,
    '\n Итоговая цена: ', price4)
else:
    print('У вас нету скидки.')

#num13
ves= float(input('Введите вес вашей посылки: '))
lit = (ves / 100) * 150
med = (ves / 100) * 300
str = (ves / 100) * 400
hard = (ves / 100) * 475
if 0 < ves <= 200:
    print ('Стоимость посылки равняется ', lit)
elif 200 < ves <= 600:
    print ('Стоимость посылки равняется ', med)
elif 600 < ves <= 1000:
    print ('Стоимость посылки равняется ', str)
elif 1000 < ves:
    print ('Стоимость посылки равняется ', hard)
else:
    print('Ошибка ввода')

#num14
hight = float(input('Введите ваш рост '))
wight = float(input('Введите ваш вес '))
IMT = wight / hight
if 18.5 <= IMT <= 25:
    print ('Ваш ИМТ равен : ', format(IMT, '.1f'), ', он в пределе нормы.')
elif 18.5 > IMT:
    print ('Ваш ИМТ равен : ', format(IMT, '.1f'), ', ваш вес меньше нормы')
elif 25 < IMT:
    print ('Ваш ИМТ равен : ', format(IMT, '.1f'), ', ваш вес больше нормы')
else:
    print ('Ошибка ввода.')

#num15
insek = int(input('Введите количество секунд: '))
day = str(insek // 86400)
hour = (insek // 3600) % 24
min = (insek // 60) % 60
sek = insek % 60
print (day , 'д:' , hour , 'ч:' , min , 'м:' , sek , 'с', sep='')

#num16
year = int(input('Введите год, который вы хотите проверить на високосность: '))
if (year/ 100)%1==0 and (year/400)%1==0 or (year/100)%1!=0 and (year/4)%1==0:
    print('В', year ,'году в феврале 29 дней.')
else:
    print('В', year ,'году в феврале 28 дней.')

#num17
print('Перезагрузите компьютер и попробуйте подключиться.')
otvet=str(input('Вы исправили проблему? '))
if otvet=='Нет' or otvet=='нет':ё
    print('Перезагрузите маршрутизатор и попробуйте подключиться.')
    otvet=str(input('Вы исправили проблему? '))
    if otvet=='Нет' or otvet=='нет':
        print('Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены.')
        otvet=str(input('Вы исправили проблему? '))
        if otvet=='Нет' or otvet=='нет':
            print('Переместите маршрутизатор на новое место.')
            otvet=str(input('Вы исправили проблему? '))
            if otvet=='Нет' or otvet=='нет':
                print('Возьмите новый маршрутизатор.')
            else:
                print('Отично, рад был помочь.')
        else:
            print('Отично, рад был помочь.')
    else:
        print('Отично, рад был помочь.')
else:
    print('Отично, рад был помочь.')
"""
#num18
#num19
