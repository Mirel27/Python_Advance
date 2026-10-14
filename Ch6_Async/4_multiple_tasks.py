import asyncio
import time

async def api_call(url:str,delay:int=3):
    print("Starting API call...",{url})
    await asyncio.sleep(delay)  # Simulate a network delay
    print("API call completed.",{url})
    return {"data": "Sample response"}

async def execute():
    print("Executing API call...")
    time.sleep(5)
    print(f"Response received:")

async def transform():
    print("Transforming data...")
    asyncio.sleep(2)  # Simulate transformation delay
    print("Data transformation completed.")

async def main():
    
    urls = ["https://api.example.com/data1", "https://api.example.com/data2", "https://api.example.com/data3"]
    # results =  await asyncio.gather(api_call(urls[0],2),api_call(urls[1],3),api_call(urls[2],1))

    # tasks = [await api_call(url, delay) for url, delay in zip(urls, [2, 3, 1])]
    # responses = await asyncio.gather(*tasks)
    # print(f"Responses received: {tasks}")

    # Create tasks for API calls
    results = await asyncio.gather(api_call("https://api.example.com/data1"),
                                   execute(),
                                   transform())
    print("All tasks completed")
asyncio.run(main())