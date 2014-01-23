import math

class ElevatorCab:
    def __init__(self, id, floors=[]):
        self._id = id
        self._current_floor = 0
        self.floors = floors
        self.travelling_time_between_floors = 4

        self.sigma= 0.5
        self.mju = 5

    def __repr__(self):
        return "%s:%i [%i]" % (self._id,
                               len(self.floors),
                               self.get_current_floor())
        
        #TODO: fix proper accelleration
        self.accelleration = lambda x: (1/(self.sigma * math.sqrt(2 * math.pi))) * math.pow(math.e, -math.pow(x-self.mju,2) / ( 2 * math.pow(self.sigma, 2) ) )

        
    def get_current_floor(self):
        return self._current_floor
        
    def move(self, floor):
        steps = floor - self.get_current_floor()
        print steps

        self._current_floor = self.get_current_floor() + steps


class ElevatorController:
    def __init__(self):
        self.elevators = []

    def add(self, elevator):
        self.elevators.append(elevator)


if __name__ == "__main__":
    controller = ElevatorController()

    ec1 = ElevatorCab("First",[0,1,2,3,4,5,6,7,8,9,10,11,12])
    ec2 = ElevatorCab("Second",[0,1,2,3,4,5,6,7,8,9,10,11,12])
    
    controller.add(ec1)
    controller.add(ec2)

    from random import randrange
    
    for i in xrange(0,10):
        print ec1
        print ec2
        ec1.move(randrange(0,13))
        ec2.move(randrange(0,13))
