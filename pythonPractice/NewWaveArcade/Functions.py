import random

#  Dolphin Olympics 2 is an exciting aquatic game that invites you to score as many points as possible in two minutes.
#  The goal is to swim and flip your dolphin. All you have to do is drive the mammal to stellar jumps by building speed
#  and pulling bigger and better tricks. You are to write the function highScore,
#  which will be used to list high scores at the end of the game.
#  This function should be passed three integer values and return the highest of these three scores.
def highScore (x, y, z):
    num = [x, y, z]
    return max(num)
    # you can also utilize for loops



# New Wave Computers occasionally has to close when there is bad weather. Write the function isClosed.
# This function should be passed the boolean isRaining and the double temperature.
# The function should return true if isRaining is true and temperature is below 65 or above if temperature is above 95,
# otherwise it should return false.
def isClosed(isRaining, temperature):
    if isRaining and (temperature < 65 or temperature > 95):
        return True
    else:
        return False

# New Wave Computers has a difficult time attracting customers during the work week.
# In order to attract patrons between Monday and Thursday they have decided to multiply their prize tickets on these days.
# Write the function multiply. This function should be passed integer tickets and String day.
# Return the new amount of tickets using the following multipliers:

# Monday - 2, Tuesday - 3, Wednesday - 2.1, Thursday - 2.5, Friday Saturday and Sunday - 1
def multiply(tickets, day):
    day = day.lower() # for case sensitivity

    if day == "monday":
        return tickets * 2
    elif day == "tuesday":
        return tickets * 3
    elif day == "wednesday":
        return tickets * 2.1
    elif day == "thursday":
        return tickets * 2.5
    elif day == "friday" or day == "saturday" or day == "sunday":
        return tickets * 1
    else:
        return -1  # in case of invalid day

#In the game New Wave Racing a car randomly moves forward between one and five at a time until it has reached the finish line,
# which is 50 spaces away. Write the function racing, which should simulate the number of turns that it would take to reach the finish line.
# The function should return the number of turns that it took for the car to reach the finish line.
# You can generate a random number between 1 and 5 using the code (int)(Math.random() * 5) + 1.
def racing():
    count = 0
    distance = 0
    while distance < 50:
        distance += random.randint(1, 5)
        count += 1

    return count

# In the game of knock down a contestant is given three chances to throw a baseball at five pins.
# In order to win the game, competitors need to knock down all five pins with their three attempts.
# Write the function knockdown.
# This function should use a for loop and Math.random() to determine if the user was able to knock down all five pins.
# A throw should knock down no pins if a number between 0 and 3 is generated, one pin if a number between 4 and 6 is generated,
# two pins if 7 or 8 is generated, three pins if it a 9 is generated and four pins if a 10 is generated.
# Return true if all five pins are knocked down, otherwise return false.
def knockdown():
    pins = 5
    for attempt in range(3): #loop 3 times

        # generate random number between  0 - 10
        throw_result = random.randint(0, 10)

        #  check how many pins were knocked down
        if 0 <= throw_result <= 3:
            knocked_down = 0
        elif 4 <= throw_result <= 6:
            knocked_down = 1
        elif throw_result == 7 or throw_result == 8:
            knocked_down = 2
        elif throw_result == 9:
            knocked_down = 3
        elif throw_result == 10:
            knocked_down = 4

        pins -= knocked_down

        if pins <= 0:
            return True  # if all pins are knocked down

    return False



