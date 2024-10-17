
class Drug:

    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str, drugs=[], employees=[]):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append(
            {
                'first_name': first_name,
                'last_name': last_name,
                'age': age
            }
        )

    def total_value(self) -> int:
        return sum([d.amount*d.price for d in self.drugs])

    def employees_summary(self) -> str:
        e = "Employees:\n"
        for ind, emp in enumerate(self.employees):
            e += f"The employee number {ind+1} is {emp['first_name']} {emp['last_name']} who is {emp['age']} years old.\n"
        return (e)
