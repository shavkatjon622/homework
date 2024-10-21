# first task
# 1. Shaxsiy ma'lumotlar tizimi: Foydalanuvchidan ismi, yoshi, manzili va telefon raqamini kiriting. Agar foydalanuvchi 18 yoshdan kichik bo'lsa, unga bu tizimdan foydalanish cheklanganligi haqida xabar bering. Agar foydalanuvchi kiritgan ma'lumotlar to'liq bo'lmasa (biror narsa kiritilmasa), foydalanuvchiga "Ma'lumot to'liq emas!" xabarini qaytaring. To'liq va mos keladigan ma'lumotlar kiritilganda, ularni dictionaryda saqlang va foydalanuvchi uchun profil yarating.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
number = input("Enter your phone number: ")
profile = {}
if age < 18:
    print("Your age is less than 18. You don't use this website")
elif name == None and age == None and location == None and number == None:
    print("Information isn't complate")
else:
    profile['name'] = name
    profile['age'] = age
    profile['location'] = location
    profile['number'] = number
    print('Profile made successfully')


#second task
#2. Tartiblangan ism va yoshlar ro'yxati: Foydalanuvchidan 5 ta odamning ismi va yoshi kiritilishini so'rang. Bu ma'lumotlarni dictionaryda saqlang va yoshi bo'yicha tartiblangan holda chop eting.

people = []
for i in range(5):
    person = {}
    name = input(f'Enter {i+1}-person name: ')
    age = input(f'Enter {i+1}-person age: ')
    person["name"] = name
    person["age"] = int(age)
    people.append(person)
new = sorted(people, key=lambda x : x['age'])
for person in new:
    print(person)


#Third task
#Fibonacci sonlari: Foydalanuvchidan raqam kiriting va shu raqamgacha bo'lgan Fibonacci ketma-ketligining sonlarini chop eting. Fibonacci sonlarini hisoblashda while tsiklidan foydalaning.

final = int(input("Enter a number: "))
first = 0
second = 1
print(first)
while second <= final:
    print(second)
    first, second = second, first + second


#Fourth task
#Elektron pochta tasdiqlash: Foydalanuvchidan elektron pochta manzilini so'rang. Agar pochta manzili "@gmail.com", "@yahoo.com", yoki "@outlook.com" bilan tugasa, foydalanuvchi provayderini aniqlang va tegishli xabar chop eting. Agar pochta manzili kiritishda "@" belgisi bo'lmasa yoki noto'g'ri formatda kiritilgan bo'lsa, "Noto'g'ri elektron pochta manzili" degan xabar chiqaring.

mail = input('Enter your email: ')
if '@gmail.com' in mail:
    print('You use gmail')
elif '@yahoo.com' in mail:
    print('You use yahoo')
elif '@outlook.com' in mail:
    print("You use outlook")
else:
    print('Mistake email')


#Fiveth task
#Mahsulotlar va narxlar: Foydalanuvchidan mahsulotlarning nomi va narxini kiriting, bularni dictionaryda saqlang. Keyin foydalanuvchiga jami narxni hisoblang va chop eting. Agar mahsulot narxi 100 mingdan yuqori bo'lsa, ularga chegirma qo'llang (masalan, 10%).

products = []
loop = True
while loop:
    product = {}
    name = input('Enter product name: ')
    cost = float(input('Enter product cost: '))
    question = input('do you want to add another product? (y/enter): ')
    product['name'] = name
    product['cost'] = cost
    products.append(product)
    if question == 'y':
        continue
    else:
        loop = False
cost = 0
for product in products:
    cost += product['cost']
if cost >= 100000:
    cost = cost - (cost / 10)
print(f"Your shopping cost is {cost}")


#Sixth task
#Takrorlanmas raqamlar ro'yxati: Foydalanuvchidan 10 ta raqam kiriting, bu raqamlar orasida takrorlanishlar bo'lishi mumkin. Ushbu raqamlar ichida faqat takrorlanmas raqamlarni toping va alohida chop eting. Buning uchun set va listlardan foydalaning.

numbers1 = []
for i in range(10):
    number = input("Enter a number: ")
    numbers1.append(number)
set_list = set(numbers1)
for number in set_list:
    numbers1.remove(number)
for number in numbers1:
    if number in set_list:
        set_list.remove(number)
    else:
        pass
print(set_list)


#Seventh task
#Xarajatlar rejasi: Foydalanuvchidan har oyda qilinadigan 5 ta asosiy xarajatni va har birining narxini so'rang. Ushbu ma'lumotlarni list va dictionaryda saqlang. Xarajatlarning jami narxini hisoblang va agar foydalanuvchi kiritgan jami narx 1 milliondan oshsa, ularga byudjetdan chiqayotganliklarini ko'rsating va byudjetni qayta ko'rib chiqish taklifini bering.

products = []
loop = 1
while loop<=5:
    product = {}
    name = input('Enter product name: ')
    cost = float(input('Enter product cost: '))
    product['name'] = name
    product['cost'] = cost
    products.append(product)
    loop += 1
cost = 0
for product in products:
    cost += product['cost']
if cost >= 1000000:
    print(f"Your financial score is not good")


#eighth task
#Talabalar bahosi: 5 ta talabalar va ularning baholarini kiriting. Har bir talabani bahosiga qarab quyidagi izohlar bilan chop eting:
# 90 dan yuqori – "A'lo baho"
# 80 dan yuqori – "Yaxshi baho"
# 70 dan yuqori – "Qoniqarli"
# 70 dan past – "Yomon baho".

students = []
loop = 1
while loop<=5:
    student = {}
    name = input('Enter student name: ')
    grade = float(input('Enter student grade: '))
    student['name'] = name
    student['grade'] = grade
    students.append(student)
    loop += 1
for student in students:
    if student['grade'] > 100:
        print(f'something wrong with {student["name"]}')
    elif student['grade'] >= 90:
        print(f'{student["name"]} has a high grade.')
    elif student['grade'] >= 80:
        print(f'{student["name"]} has a good grade.')
    elif student['grade'] >= 70:
        print(f'{student["name"]} has a middle grade.')
    elif student['grade'] >= 0:
        print(f'{student["name"]} has a low grade.')
    else:
        print(f'something wrong with {student["name"]}')


#nineth task
#Raqamlar filtri: Foydalanuvchidan 10 ta raqam kiriting. Ushbu raqamlar orasidan faqat juft va toq sonlarni alohida chop eting. Agar raqam manfiy bo'lsa, ularni e'tiborsiz qoldiring. Bularni for tsikli yordamida filtrlab ko'rsating.

numbers = []
for i in range(10):
    num = int(input(f"Enter {i+1}-number: "))
    numbers.append(num)
even_number = []
odd_number = []
for number in numbers:
    if number <= 0:
        continue
    elif number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)
print(even_number)
print(odd_number)


# tenth task
#Takrorlanmalarni aniqlash: Foydalanuvchidan bir nechta so'zlarni kiriting (kamida 10 ta). Ushbu so'zlardan takrorlanganlarini toping va faqat takrorlangan so'zlarni chop eting. Buning uchun set va listlardan foydalaning.

words = []
for i in range(10):
    name = input(f'Enter {i+1}-word: ')
    words.append(name)
set_words = set(words)
for word in set_words:
    words.remove(word)
print(set(words))


# eleventh task
#Til bilimi: Foydalanuvchidan qaysi dasturlash tillarini bilishini so'rang va ularni dictionaryda saqlang. Foydalanuvchi qaysi tillarni bilishini kiritgandan keyin, agar foydalanuvchi "Python" tilini bilsa, "Siz Python bo'yicha dasturchisiz" deb xabar bering. Agar "JavaScript"ni bilsa, "Veb dasturchi" ekanini ayting. Aks holda, "Siz dasturchi emassiz" degan xabar chop eting.

info = {}
a = 1
name = input("What is your name? ")
languages = []
while a:
    language = input('Enter programming language: (for stop 0) ')
    languages.append(language.lower())
    if language == '0':
        break
info['name'] = languages
if 'python' in info['name']:
    print('You are a Python programmer')
elif 'javascript' in info['name']:
    print('You are a web programmer')
else:
    print('You are not a programmer')


# twelveth task
#Xaridlar ro'yxati: Mahsulotlar va ularning narxlarini lug'at shaklida kiritib, jami narxni hisoblang. Keyin foydalanuvchiga jami narx bo'yicha chegirma imkoniyatini ko'rsating:
# 500 mingdan oshsa 5% chegirma.
# 1 milliondan oshsa 10% chegirma.
# Chegirmadan keyin jami narxni chop eting.

products = []
loop = True
while loop:
    product = {}
    name = input('Enter product name: ')
    cost = float(input('Enter product cost: '))
    question = input('do you want to add another product? (y/enter): ')
    product['name'] = name
    product['cost'] = cost
    products.append(product)
    if question == 'y':
        continue
    else:
        loop = False
cost = 0
for product in products:
    cost += product['cost']
print(f'Your total cost is {cost}')
if cost >= 500000:
    print('You have a 5% chance for a discount!')
    cost = cost - (cost / 20)
    print(f"Your shopping cost is {cost}")
elif cost >= 1000000:
    print('You have a 10% chance for a discount!')
    cost = cost - (cost / 10)
    print(f"Your shopping cost is {cost}")


# thirteenth task
#Takrorlanuvchi raqamlar: Foydalanuvchidan 10 ta raqam kiriting va ulardan takrorlanganlarini topib, chop eting. Takrorlanmagan raqamlarni alohida ko'rsating. Buning uchun for tsikli va listdan foydalaning.

numbers1 = []
repeated = []
for i in range(10):
    number = input("Enter a number: ")
    numbers1.append(number)
set_list = set(numbers1)
for number in set_list:
    numbers1.remove(number)
for number in numbers1:
    if number in set_list:
        repeated.append(number)
        set_list.remove(number)
    else:
        pass
print(f"unrepeat numbers {set_list}")
print(f"repeat numbers {repeated}")


#fourteenth task
#Fibonacci sonlarining uzunligi: Foydalanuvchidan Fibonacci ketma-ketligidagi nechta sonni ko'rsatish kerakligini so'rang va ushbu sonlarni ro'yxat shaklida chop eting. Ketma-ketlikni yaratishda while tsiklidan foydalaning.

finish = int(input("Enter the number of fibonacci numbers: "))
first = 0
second = 1
print(first)
print(second)
n = 2
while True:
    first, second = second, first + second
    n += 1
    print(second)
    if n == finish:
        break


#Fifteenth task
#Juft va toq sonlar ajratish: Foydalanuvchidan 10 ta son kiriting va bu sonlarni juft va toq sonlar ro'yxatiga ajrating. Har bir ro'yxatni alohida chop eting.

odd_numbers = []
even_numbers = []
for i in range(10):
    number = int(input(f"Enter {i+1}-number: "))
    if number <= 0:
        continue
    elif number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(odd_numbers)
print(even_numbers)