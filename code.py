import random
score = 0
level = 1
print('Welcome to the Guessing Game!!!')
print('You will be given a number and asked to guess whether the next number will be higher or lower than the current number.')
print('If you guess correctly, you will gain 1 point but if you lose you will have to start again')

User_name = input(' Please enter your name:')

for i in range(11):
    if score==5:
        break
    print(f'Level: {level}')
    random_num = random.randint(0,100)
    print(f"Your first number is {random_num}")
    user_guess= input(f'{User_name} please enter your guess (higher/lower): ')
    random_num2 =random.randint(0,100)
    if random_num2>random_num and user_guess =='higher':
        print(f'Well done {User_name}! You have guessed correctly!')
        score+=1
        print(f'Your score is: {score}')
        level+=1

    elif random_num2<random_num and user_guess =='lower':
        print('Well done! You have guessed correctly!')
        score+=1
        print(f'Your score is: {score}')
        level+=1
    

    else:
        print('Oh No! You have guessed incorrectly!')
        Replay = input('Would you like to replay? y/n : ')
        if Replay == 'n':
            print(f'Score = {score} ')
            print('Thank you for playing')
            break
        else:
            level =1
   
            

