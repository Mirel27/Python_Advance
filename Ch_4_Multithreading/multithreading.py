import time
from concurrent.futures import ThreadPoolExecutor

# def fetch_data(url:str):
#     print("Start fetching data")
#     time.sleep(5)
#     print("Done fetching data")
#     return f"data fetched from {url}"

def fetch_data(tasks:dict):
    print("Start fetching data")
    time.sleep(5)
    print("Done fetching data")
    return f"data fetched from {tasks['url']}"

url = ["https://www.google.com",
       "https://www.facebook.com",
       "https://www.twitter.com",
       "https://www.linkedin.com",
       "https://www.instagram.com",
       "https://www.youtube.com",
       "https://www.reddit.com",
       "https://www.quora.com"]
tasks = []
for i in url:
    tasks.append({"url":i,"delay":5})

#Without thread

# for i in url:
#     data = fetch_data(i)
#     print(data)

#To do it parrallel use multithread Executor

# results= []
# with ThreadPoolExecutor(max_workers=len(url)) as executors:
#     futures = executors.map(fetch_data,url)
#     results.extend(futures)

# print(results)

results= []
with ThreadPoolExecutor(max_workers=len(tasks)) as executors:
    futures = executors.map(fetch_data,tasks)
    results.extend(futures)

print(results)