import asyncio
import time

async def main():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

asyncio.run(main())