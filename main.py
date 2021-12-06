import random

guessesTaken = 0
print('Добро пожаловать, в "Числовую Угадайку"! Как тебя зовут?')
myName = input()
number = random.randint(1, 100)
print('Что ж, тогда начнем? ' + myName + ', я загадал число от 1 до 100')
while guessesTaken < 10:
    print('Попробуй отгадать!')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print('Мое число больше твоего')
    if guess > number:
        print('Мое число меньше твоего')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Превосходно ' + myName + '! Ты угадал число с ' + guessesTaken + ' попытки. Твой выигрыш 10 очков.')
if guess != number:
    number = str(number)
    print('Попытки кончились... Мое число было: ' + number + '.Ты проиграл…')
