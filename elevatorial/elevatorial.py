import math
import sys
import re
from twisted.internet import reactor, protocol


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
        for f in xrange(0, int(math.fabs(steps))+1):
            if steps < 0:
                f = -1*f
            print self.get_current_floor() + f
        
        self._current_floor = self.get_current_floor() + steps


class ElevatorController:
    def __init__(self):
        self.elevators = []

    def add(self, elevator):
        self.elevators.append(elevator)

    def getElevator(self, index):
        return self.elevators[index]

def main():
    controller = ElevatorController()

    ec1 = ElevatorCab("First",[0,1,2,3,4,5,6,7,8,9,10,11,12])
    ec2 = ElevatorCab("Second",[0,1,2,3,4,5,6,7,8,9,10,11,12])
    
    controller.add(ec1)
    controller.add(ec2)

    elevator_request = re.compile(r'e\s(\d+)\s(\d+)')
    floor_request = re.compile(r'f\s(\d+)\s(up|down)')
        
    running = True
    while(running):
        instr = sys.stdin.readline()
        if instr.strip() == "quit":
            running = False

        em = elevator_request.match(instr)
        if em:
            elevator_number = int(em.group(1))
            requested_floor = em.group(2)
            if 0 <= elevator_number < len(controller.elevators)+1:
                controller.getElevator(elevator_number).move(int(requested_floor))
            else:
                print "Elevator index out of range"
            
        fm = floor_request.match(instr)
        if fm:
            print fm.group(1)
            print fm.group(2)
        
if __name__ == "__main__":
    main()
