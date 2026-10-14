class company:

    title:str = 'consultancy'
    def __init__(self, company_name):
        self.company_name:str = company_name

    def info(self):
        print(f"The company name is {self.company_name}")
        return self.company_name

class client_company():
        
    title:str = 'client_company'
    def __init__(self, client_company_name):
        self.client_company_name:str = client_company_name

    def info(self):
        print(f"The client company name is {self.client_company_name}")
        return self.client_company_name

class employee(company,client_company):

    def __init__(self, company_name,client_company_name,employee_name):
        self.company_name = company_name
        self.client_company_name = client_company_name
        self.employee_name = employee_name

    def info(self):
        response1 = company.info(self)
        response2 = client_company.info(self)
        return f" Employee Name : {self.employee_name} Client Company {response2} Company Name {response1}"

obj1 = employee('InfoTech','Apple','John Doe')
obj1.info()

        