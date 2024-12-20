# Import the boid class
from Boid_Class import Boid

# Import pre-requesities
import random #for initialising random velocities and positions for the boids
import math #used to calculate the distances between boids

# ------- Editable Constants --------------------
# Please change these constants to adjust for performance on different devices
BOID_COUNT=100 #number of boids displayed
DISPLAY_SIZE=(1680,1050) #resolution for full screen on an M1 Macbook Air
BOID_MAX_VELOCITY=2.0 #maximum velocity for a boid (combination of X and Y)

#-------- Required Variables --------------------

boid_population=[]


#-------- Initialise boid population ------------

for i in range(BOID_COUNT):
    temp_position=[random.randint(0,DISPLAY_SIZE[0]), random.randint(0,DISPLAY_SIZE[1])] #provide a random position within the given bounds
    temp_velocity=[random.uniform(-BOID_MAX_VELOCITY,BOID_MAX_VELOCITY),random.uniform(-BOID_MAX_VELOCITY,BOID_MAX_VELOCITY)] #provide a random velocity between the max and min velocity
    # although some of the values will amount to be larger than the maximum velocity once combined using pythagoras theorem, this will be resolved through the use of a limiting function in the main loop.
    temp_boid=Boid(temp_position,temp_velocity) #create a temp boid object which holds these newly generated positions and velocities.
    boid_population.append(temp_boid) #add this temp boid to the population.


