import random
import math
'''
#OneHundredHats on a scale of 10 Prisiners

ColorChoices = ["red", "black"]
EveryPrisiner = []

class Prisiner:
    def __init__(self, hatColor):
        self.hatColor = hatColor

for i in range(100):
    name = "prisiner" + str(i)
    print(name)
    name = Prisiner(random.choice(ColorChoices))
    print(name.hatColor)
    PrisinerArr = []
    PrisinerArr.append(name)
    EveryPrisiner.append(PrisinerArr)

print("-----------------------------------")
print(EveryPrisiner)'''

def solve_prisoner_riddle(hat_colors):
    total_prisoners = len(hat_colors)
    result = []

    # Determine the color each prisoner should guess
    red_count = hat_colors.count("red")
    even_reds = red_count % 2 == 0

    for i in range(total_prisoners):
        if i == total_prisoners - 1:
            result.append("red" if even_reds else "black")
        elif i == total_prisoners - 2:
            result.append("red" if even_reds else "black")
        else:
            result.append("red" if hat_colors[i] == "red" else "black")

    return result

# Example usage
ColorChoices = ["red", "black"]
hat_colors = []
for i in range(100):
    hat_colors.append(random.choice(ColorChoices))

prisoner_guesses = solve_prisoner_riddle(hat_colors)
print("Prisiner Guesses:", prisoner_guesses)

print("-----------------------------")
print(hat_colors)
print("-----------------------------")

incorrect_guesses = []
for i in range(len(hat_colors)):
    if hat_colors[i] != prisoner_guesses[i]:
        incorrect_guesses.append(i)

if not incorrect_guesses:
    print("Congratulations, the strategy worked perfectly!")
else:
    print("There were wrong guesses:")
    for i in incorrect_guesses:
        print(f'Guess {i} was wrong. The guess was {prisoner_guesses[i+1]}, but the correct hat color was {hat_colors[i+1]}')