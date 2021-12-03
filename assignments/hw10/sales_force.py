"""
Harrison Penley
sales_force.py

problem: create a class that uses the data from sales_person.py and organizes it into a list.

I certify that is entirely my own work.
"""

from sales_person import SalesPerson

class SalesForce:
    def __init__(self, sales_people):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        for line in infile:
            lines = line.split(", ")
            person = SalesPerson(int(lines[0]), lines[1])
            sales = lines[2].split()
            for i in sales:
                person.enter_sale(float(i))
            self.sales_people.append(person)

    def quota_report(self, quota):
        infile = open(file_name, "r")
        for line in infile:
            lines = line.split(", ")
            sales = list(lines[2].split())
            sales_values = SalesPerson(sales[0], sales[2])
            if sales_values >= quota:
                return True
            else:
                return False

    def top_seller(self):
        for i in self.sales_people:




    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if SalesPerson.get_id(i) != employee_id:
                return None
            if SalesPerson.get_id(i) == employee_id
                return SalesPerson.get_name(i)

