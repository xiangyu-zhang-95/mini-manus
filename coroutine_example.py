import asyncio
import time
from typing import List

# Regular (synchronous) implementation
def fetch_data_sync(url: str) -> str:
    # Simulate network delay
    time.sleep(1)
    return f"Data from {url}"

def process_urls_sync(urls: List[str]) -> List[str]:
    results = []
    for url in urls:
        result = fetch_data_sync(url)
        results.append(result)
    return results

# Coroutine (asynchronous) implementation
async def fetch_data_async(url: str) -> str:
    # Simulate network delay
    await asyncio.sleep(1)
    return f"Data from {url}"

async def process_urls_async(urls: List[str]) -> List[str]:
    # Create tasks for all URLs
    tasks = [fetch_data_async(url) for url in urls]
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    return results

# Example usage
def main():
    urls = [
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/3",
        "http://example.com/4",
        "http://example.com/5"
    ]

    # Test synchronous version
    start_time = time.time()
    sync_results = process_urls_sync(urls)
    sync_duration = time.time() - start_time
    print(f"Synchronous version took {sync_duration:.2f} seconds")

    # Test asynchronous version
    start_time = time.time()
    async_results = asyncio.run(process_urls_async(urls))
    async_duration = time.time() - start_time
    print(f"Asynchronous version took {async_duration:.2f} seconds")

if __name__ == "__main__":
    main()
    # Expected output:
    # Synchronous version took 5.00 seconds
    # Asynchronous version took 1.00 seconds

