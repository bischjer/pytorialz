import math

class ElevatorCab:
    def __init__(self, id, floors=[]):
        self._id = id
        self._current_floor = 0
        self.floors = floors
        self.travelling_time_between_floors = 4

        self.sigma= 0.5
        self.mju = 5

        #TODO: fix proper accelleration
        self.accelleration = lambda x: (1/(self.sigma * math.sqrt(2 * math.pi))) * math.pow(math.e, -math.pow(x-self.mju,2) / ( 2 * math.pow(self.sigma, 2) ) )

        
    def get_current_floor():
        return self._current_floor
        
    def move(floor):
        steps = floor - self.get_current_floor()


class ElevatorController:
    def __init__(self, number_of_elevators):
        self.number_of_elevators = number_of_elevators











        
