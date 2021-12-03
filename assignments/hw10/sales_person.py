"""
Harrison Penley
sales_person.py

problem: Create a sales person class to be able to keep track of the data surrounding an individual sales person.

I certify that this is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for i in self.sales:
            acc = acc + i
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        return 0

    def __str__(self):
        return str(str(self.get_id()) + "-" + self.get_name() + ": "
                   + str(self.total_sales()))
    