def pandas_decorator(fx):

    def mainfunc(*args):
        response = fx(*args)
        response.to_parquet("temp.parquet")
        return response
    return mainfunc


@pandas_decorator
def csv_to_parquet(filepath):
    import pandas as pd
    df = pd.read_csv(filepath)
    return df

df = csv_to_parquet('Ch_3_Polymorphism&Decorators\orders.csv')