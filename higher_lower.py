import random

from data import data

score = 0

should_continue = True

acc_b = random.choice(data)

while should_continue:

    acc_a = acc_b
    acc_b = random.choice(data)
    while acc_a == acc_b:
        acc_b = random.choice(data)

    print("Compare A: {}, {}, from {}.".format(acc_a['name'], acc_a['description'], acc_a['country']))
    print("Compare B: {}, {}, from {}.".format(acc_b['name'], acc_b['description'], acc_b['country']))

    user = input("Who has more followers? Type A or B: ").lower()

    if acc_a['follower_count'] > acc_b['follower_count'] and user == 'a':
        score += 1
        print("You've guessed it right!!. Current score: {}".format(score))

    elif acc_a['follower_count'] < acc_b['follower_count'] and user == 'b':
        score += 1
        print("You've guessed it right!!. Current score: {}\n".format(score))

    else:
        should_continue = False
        print("You've guessed it wrong!!. Final score: {}\n".format(score))
