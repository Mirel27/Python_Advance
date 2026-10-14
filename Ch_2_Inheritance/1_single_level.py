class company:

    title:str = 'consultancy'
    def __init__(self, company_name):
        self.company_name:str = company_name

    def info(self):
        print(f"The company name is {self.company_name}")
        return self.company_name

# obj2 = Company('Tech Solutions')
# obj2.info()

class employee(company):
    def __init__(self,employee_name,company_name):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = company.info(self) #response = super.info(self)
        print(f"the employee {self.employee_name} works at {response}")

obj1 = employee("John Doe", "Infotech")
obj1.employee_info()