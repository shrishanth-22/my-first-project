import random

secret_num = random.randint(1,9)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess number between 1 to 9 : '))
    guess_count += 1
    if guess == secret_num:
        print('You Won!🎉')
        break
    elif guess < secret_num:
        print("Too low")
    elif guess > secret_num:
        print("Too high")
else:
    print('you lost')
    print('correct number is ' + str(secret_num))
