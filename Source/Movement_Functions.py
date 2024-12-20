from Boid_Class import Boid

def Rule1(bs:Boid,boid_population:list):
    """
    Function to calculate the velocity modifier to move the boid towards the centre of mass.

    :param bs: the boid that the movement will be applied to.
    :param boid_population: the other boids that will be used to calculate the centre of mass.
    """

    #start a position total [X,Y]
    position_total=[0,0]

    #for each item in the population
    for b in boid_population:
        #where it is not the same as the current boid
        if bs!=b:
            #add the position to the total
            position_total[0]+=b.position[0]
            position_total[1]+=bs.position[1]
    #get the average x position
    position_total[0]/=(len(boid_population)-1)
    #get the average y position
    position_total[1]/=(len(boid_population)-1)

    #the velocity modifier is the target position subtract the current position and multiplied by the influence modifier.
    velocity_modifier=[(position_total[0]-b.position[0])*0.01,(position_total[1]-b.position[1])*0.01]
    return velocity_modifier

