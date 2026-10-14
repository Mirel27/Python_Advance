import asyncio

async def api_call(url:str,delay:int):
    print("Starting API call...",{url})
    await asyncio.sleep(delay)  # Simulate a network delay
    print("API call completed.",{url})
    return {"data": "Sample response"}

async def main():
    
    urls = ["https://api.example.com/data1", "https://api.example.com/data2", "https://api.example.com/data3"]
    # results =  await asyncio.gather(api_call(urls[0],2),api_call(urls[1],3),api_call(urls[2],1))

    tasks = [await api_call(url, delay) for url, delay in zip(urls, [2, 3, 1])]
    responses = await asyncio.gather(*tasks)
    print(f"Responses received: {tasks}")

asyncio.run(main())