# Clase in Python

class Robot:
    def __init__(self, nume, serial_number, hardware, software, sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.sleep = sleep

    def turn_on(self):
        if self.sleep == False:
            return f'{self.nume} is already running'
        else:
            self.sleep = False
            return f'{self.nume} turned on'



r1 = Robot("John", "12333", "i5", "Python", True)
print(r1.serial_number)
print(r1.sleep)
# print(r1.turn_on())
print(Robot.turn_on(r1))
print(r1.sleep)





# r1 = Robot()
# r2 = Robot()
# print(r1)
# print(r2)
# r1.nume = "John"
# r1.serial_number = "12333"
# r1.hardware = "i5"
# r1.software = "python"
#
# r2.nume = "mark"
# r2.serial_number = "22333"
# r2.hardware = "i5"
# r2.software = "C++"
#
# print(r1.serial_number)