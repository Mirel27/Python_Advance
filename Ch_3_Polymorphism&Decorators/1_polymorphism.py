class api_fetch:
    def fetch(self):
        print(" Fetching data from api......")


class database_fetch:
    def fetch(self):
        print(" Fetching data from db......")


class s3_fetch:
    def fetch(self):
        print(" Fetching data from s3......")

obj = database_fetch()
obj.fetch()