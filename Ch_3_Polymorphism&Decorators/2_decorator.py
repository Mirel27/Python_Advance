def my_decorator(func):

    def mainfunc(*args):
        print("Before calling the function")

        response = func(*args)

        print("After calling the function")

        return response
    return mainfunc

@my_decorator
def fetchdata(url:str,path:str):
    return f"Fetching data from {url} to {path}"


response = fetchdata('url', 'jseioknfbhesj')
print(response)