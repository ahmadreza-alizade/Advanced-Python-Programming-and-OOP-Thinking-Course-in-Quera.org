class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    instances = []

    def __init__(self, name: str, level=1, expertise="", employees=[], capacity=1):
        self.name = name
        self.level = level
        self.expertise = expertise
        self.employees = employees
        self.capacity = capacity
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return (Consts.BASE_PRICE[self.expertise])

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return (self.expertise)

    def calc(self) -> int:
        return(-1 * self.calc_costs())

    @staticmethod
    def calc_all() -> int:
        return(sum([WorkPlace.calc(ins) for ins in WorkPlace.instances]))








