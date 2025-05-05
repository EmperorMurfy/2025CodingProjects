
from Functions import highScore, isClosed, multiply, racing, knockdown

# high score
print("High Score: " + str(highScore(1, 2, 3))) # should display 3
print("High Score: " + str(highScore(10, 43, 2))) # should display 43

# isClosed, multiply, racing, knockdown
print("Store is Closed: " + str(isClosed(True, 60))) # should display true
print("Store is Closed: " + str(isClosed(True, 75))) # should display false
print("Store is Closed: " + str(isClosed(False, 100))) #should display false

# multiply
print("Tickets: " + str(multiply(10, "monday" ))) # should display 20
print("Tickets: " + str(multiply(15, "thursday" ))) # should display 37.5

# racing
print("Race completed in " + str(racing()) + " turns")

# knockdown
print("Knockdown? " + str(knockdown()))



