# Clase in Python
import math

class Robot():
    garantie = 10
    number_of_robots = 0
    def __init__(self, nume, serial_number, hardware, software,age, sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.sleep = sleep
        self.age = age
        Robot.number_of_robots += 1

    def turn_on(self):
        if self.sleep == False:
            return f'{self.nume} is already running'
        else:
            self.sleep = False
            return f'{self.nume} turned on'


    def end_of_life(self):
        if self.age > self.garantie:
            print(f'{self.nume} is end of life')
        else:
            print(f'{self.nume} has {self.garantie - self.age} years till end of life')

    @classmethod
    def seteaza_garantie(cls, ani):
        cls.garantie = ani

    @classmethod
    def from_list(cls, lst):
        nume, serial_number, hardware, software, age, sleep = lst
        return cls(nume, serial_number, hardware, software, age, sleep)

    @staticmethod
    def dimesiuni_cerc(raza):
        return 2*math.pi*raza, math.pi*raza*raza

r1 = Robot("John", "12333", "i5", "Python", 11, True)
r2 = Robot("Mark", "22333", "i5", "C++", 3, True)

Robot.seteaza_garantie(7)
print(Robot.garantie)
print(r1.garantie)
print(r2.garantie)

robot_attributes = ['Michal', '33333', 'i7', 'Python', 1, True]
nume, serial_number, hardware, software, age, sleep = robot_attributes
r3 = Robot(nume, serial_number, hardware, software, age, sleep)
print(r3.serial_number)

r4 = Robot.from_list(robot_attributes)
print(r4.nume)

print(Robot.dimesiuni_cerc(10))