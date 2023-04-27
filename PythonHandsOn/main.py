# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ClassesPract import Bike
# from ClassesPract import Splender

def print_hi(s, *arg, **kw ):
    # b = Bike()
    # print(b.gear)
    # b.up_gear(20)
    # print(b.gear)
    # print(Bike.gear)
    # Bike.gear = Bike.gear + 1
    # print(b.gear)
    # print(Bike.gear)
    # print(Bike().gear)
    print(Bike._gear)
    print(Bike()._gear)
    # b.down_gear()
    # print(b.gear)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Hi","Hello", max = "Hey")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
