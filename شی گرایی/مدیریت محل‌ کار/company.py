# YOUR IMPORTS GO HERE
from work_place import WorkPlace, Consts


class Company(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise="company"
    
    def calc_capacity(self):
        self.capacity = int(self.level)

    def calc_costs(self):
        return(Consts.BASE_PLACE_COST * self.level)



