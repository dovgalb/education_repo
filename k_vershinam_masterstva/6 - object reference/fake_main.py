from bycycle import Bycycle
from car import Car
from main import print_ride


bycycle = Bycycle()
car = Car()

rider_list: list = [bycycle, car]

for i in rider_list:
    print_ride(i)