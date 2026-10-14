class company():

    def __init__(self,company_name):
        self.company_name = company_name

    def info(self):
        return self.company_name 


class manager(company):

    def __init__(self,company_name,manager_name):
        self.company_name = company_name
        self.manager_name = manager_name 

    def info(self):
        response = company.info(self)
        return f"company name {response} and manager name {self.manager_name}"

class employee(manager):

    def __init__(self, company_name, manager_name,employee_name):
        self.company_name=company_name
        self.manager_name=manager_name
        self.employee_name=employee_name

    def info(self):
        response = manager.info(self)
        return f" employee name {self.employee_name} {response}"

obj1 = employee("Titan" , "Joe Doe" , "James Doe")

print(obj1.info())