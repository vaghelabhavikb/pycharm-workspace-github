
class Bike:
    geared = True
    small_wheels = False
    _gear = 0

    # def __init__(self):
    #     geared = True
    #     small_wheels = False
    #     gear = 1

    def up_gear(self):
        self.gear = self.gear + 1

    def up_gear(self, gear_no):
        self.gear = self.gear + gear_no

    def down_gear(self):
        self.gear = self.gear - 1

# class Splender(Bike):
#     child_stand_area = False
#     gear = 0

    def up_gear(self):
        self.gear = self.gear + 2

    def down_gear(self):
        self.gear = self.gear - 2




