'''I started learning some of the big packages for Python like numpy, Matplotlib, and pandas. Anyways I randomly got the idea to simulate
snakes and ladders and find a way to incorporate Matplotlib for some practice. At first, I used scatter plots to see the positions that 
would be landed on after 10 dice rolls. Then, I noticed some patterns at certain positions where a snake or ladder would be. I then 
changed the project a bit, so I could see how often snakes and ladders would be landed on in total and for each individual one. Three bar
plots are displayed, showing definitive patterns which you can see for yourself if you run the code. The game board that I simulated comes 
from Yellow Mountain Imports (https://www.ymimports.com/pages/how-to-play-snakes-and-ladders).'''

# importing necessary packages
import numpy as np
import matplotlib.pyplot as plt

# initializes counts for total number of times a snake and ladder is landed on
ladder_count = 0
snake_count = 0

# initializes counts for total number of times each individual snake and ladder is landed on
ladder1_count = 0
ladder4_count = 0
ladder8_count = 0
ladder21_count = 0
ladder28_count = 0
ladder50_count = 0
ladder71_count = 0
ladder80_count = 0
snake32_count = 0
snake36_count = 0
snake48_count = 0
snake62_count = 0
snake88_count = 0
snake95_count = 0
snake97_count = 0

# setting starting position to 0
pos = 0

# simulating 1000 games
for i in range(1000):
    win_condition = 0

    # runs a single game until the win condition is met
    while win_condition == 0:

        # storing the distance from 100
        dist = 100 - pos

        # simulating a roll and changing the position accordingly, storing the position into the list
        roll = np.random.randint(1, 7)
        pos = pos + roll

        # implementing snakes and ladders
        if pos == 1:
            ladder_count = ladder_count + 1
            ladder1_count = ladder1_count + 1
            pos = 38
        if pos == 4:
            ladder_count = ladder_count + 1
            ladder4_count = ladder4_count + 1
            pos = 14
        if pos == 8:
            ladder_count = ladder_count + 1
            ladder8_count = ladder8_count + 1
            pos = 30
        if pos == 21:
            ladder_count = ladder_count + 1
            ladder21_count = ladder21_count + 1
            pos = 42
        if pos == 28:
            ladder_count = ladder_count + 1
            ladder28_count = ladder28_count + 1
            pos = 76
        if pos == 32:
            snake_count = snake_count + 1
            snake32_count = snake32_count + 1
            pos = 10
        if pos == 36:
            snake_count = snake_count + 1
            snake36_count = snake36_count + 1
            pos = 6
        if pos == 48:
            snake_count = snake_count + 1
            snake48_count = snake48_count + 1
            pos = 26
        if pos == 50:
            ladder_count = ladder_count + 1
            ladder_50count = ladder50_count + 1
            pos = 67
        if pos == 62:
            snake_count = snake_count + 1
            snake62_count = snake62_count + 1
            pos = 18
        if pos == 71:
            ladder_count = ladder_count + 1
            ladder71_count = ladder71_count + 1
            pos = 92
        if pos == 80:
            ladder_count = ladder_count + 1
            ladder80_count = ladder80_count + 1
            pos = 99
        if pos == 88:
            snake_count = snake_count + 1
            snake88_count = snake88_count + 1
            pos = 24
        if pos == 95:
            snake_count = snake_count + 1
            snake95_count = snake95_count + 1
            pos = 56
        if pos == 97:
            snake_count = snake_count + 1
            snake97_count = snake97_count + 1
            pos = 78

        # implement winning condition and bounce back rule
        if pos == 100:
            win_condition = 1
        if pos > 100:
            pos = 100 - abs(dist - roll)

# combining snake and ladder data into lists
snake_ladder_total_data = [ladder_count, snake_count]
snake_individual_data = [snake32_count, snake36_count, snake48_count,
                         snake62_count, snake88_count, snake95_count, snake97_count]
ladder_individual_data = [ladder1_count, ladder4_count, ladder8_count,
                          ladder21_count, ladder28_count, ladder50_count, ladder71_count, ladder80_count]

# print out the lists
print(snake_ladder_total_data)
print(snake_individual_data)
print(ladder_individual_data)

# visualizing the total counts using a bar plot
plt.figure(1)
labels_all = ['Ladder Count', 'Snake Count']
plt.bar(labels_all, snake_ladder_total_data)
plt.title('Total Number of Times a Snake or Ladder was Landed on')
plt.xlabel('Values')
plt.ylabel('Frequency')

# visualizing how many times each individual snake was landed on using a bar plot
plt.figure(2)
labels_snake = ['32', '36', '48', '62', '88', '95', '97']
plt.bar(labels_snake, snake_individual_data)
plt.title('Individual Snake Frequency')
plt.xlabel('Snakes (number corresponds to position on board)')
plt.ylabel('Frequency')

# visualizing how many times each individual ladder was landed on using a bar plot
plt.figure(3)
labels_ladder = ['1', '4', '8', '21', '28', '50', '71', '80']
plt.bar(labels_ladder, ladder_individual_data)
plt.title('Individual Ladder Frequency')
plt.xlabel('Ladders (number corresponds to position on board)')
plt.ylabel('Frequency')

# display plots
plt.show()
