# Clase in Python
import math

class Robot:
    garantie = 10
    number_of_robots = 0
    def __init__(self, nume, serial_number, hardware, software,age, sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.sleep = sleep
        self.age = age
        # self.identify = nume + '->' + serial_number
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

    @property
    def identify(self):
        return self.nume + '->' + self.serial_number

    @identify.setter
    def identify(self, ident):
        nume, serial = ident.split(' ')
        self.nume = nume
        self.serial_number = serial

    @identify.deleter
    def identify(self):
        print('Delete name and serial_number')
        self.nume = None
        self.serial_number = None

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

    def __repr__(self):
        return f'Robot("{self.nume}", "{self.serial_number}", "{self.hardware}", "{self.software}", {self.garantie}, {self.sleep})'

    def __str__(self):
        return self.nume

    def __add__(self, other):
        return self.age + other.age

class Aspirator(Robot):
    garantie = 15
    def __init__(self,nume, serial_number, hardware, software,age, sleep, power):
        super().__init__(nume, serial_number, hardware, software,age, sleep)
        self.power = power

class MainRobot(Robot):

    def __init__(self, nume, serial_number, hardware, software, age, sleep, robots = []):
        super().__init__(nume, serial_number, hardware, software, age, sleep)
        self.robots = robots

    def add_robot(self, rbt):
        if rbt not in self.robots:
            self.robots.append(rbt)

    def rmv_robot(self,rbt):
        if rbt in self.robots:
            self.robots.remove(rbt)

    def print_existing_robots(self):
        for robot in self.robots:
            print(robot.nume)
        print('-'*10)



r1 = Robot("John", "12333", "i5", "Python", 11, True)
r2 = Robot("Mark", "22333", "i5", "C++", 3, True)
a1 = Aspirator("George", "42333", "i5", "C++", 3, True, '1kw')

print(r1.identify)
r1.nume = 'Johnny'
print(r1.identify)
r1.identify = 'Marcus 123321'
print(r1.nume)
print(r1.serial_number)

del r1.identify
print(r1.nume)
print(r1.serial_number)