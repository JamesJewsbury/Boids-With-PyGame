class Boid:

    
    def __init__(self, position:list, velocity:list) -> None:
        """
        Initialise a Boid.

        :param position: The position for this boid [X,Y].
        :param velocity: The velocity (change in position per frame) for this boid [X,Y].
        :return: None.
        """
        self.__position=position
        self.__velocity=velocity
    
    def GetPosition(self)->list:
        """
        Returns the current position for this boid.

        :return: A position in the form of a list [X,Y]
        """
        return self.__position
    
    def SetPosition(self, position:list)->None:
        """
        Set the position of the boid.
        :param position: the new position [X,Y]
        """
        self.__position=position
    
    def GetVelocity(self)->list:
        """
        Return the current velocity for this boid.

        :return: A velocity in the form of [X,Y]
        """
        return self.__velocity
    
    def SetVelocity(self, velocity:list)->None:
        """
        Set the velocity of the boid
        :param velocity: the new velocity [X,Y]
        """
        self.__velocity=velocity

        