number = 5

if number > 0:
    print('Positive Number')
else:
    print('Negative Number')


if number % 2 == 1:
    print("Odd")
else:
    print("Even")

number_2 = 5

print(number == number_2)
print(number is number_2)

if number > 0:
    print('Positive Number')
elif number < 0:
    print('Negative Number')
else:
    print('Zero')

if not number < 0:
    print('Non-Negative')

if number >= 0:
    print('Non-Negative')