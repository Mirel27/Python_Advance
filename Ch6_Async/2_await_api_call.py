import asyncio

async def api_call():
    print("Starting API call...")
    await asyncio.sleep(2)  # Simulate a network delay
    print("API call completed.")
    return {"data": "Sample response"}

async def execute():
    print("Executing API call...")
    response = await api_call()
    print(f"Response received: {response}")

asyncio.run(execute())