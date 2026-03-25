import random

secret_num = random.randint(1,9)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess number between 1 to 9 : '))
    guess_count += 1
    if guess == secret_num:
        print('you won!')
        break
else:
    print('you lost')
    print('correct number is ' + str(secret_num))
