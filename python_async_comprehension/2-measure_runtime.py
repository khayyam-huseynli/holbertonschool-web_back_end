#!/usr/bin/env python3
''' Desription: Import async_comprehension from the previous file and write a
                measure_runtime coroutine that will execute async_comprehension
                four times in parallel using asyncio.gather.

                measure_runtime should measure the total runtime and return it.
                Notice that the total runtime is roughly 10 seconds.
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure the runtime of async_comprehension executed 4 times in
        parallel. '''
    start = time.time()
    tasks = []

    for _ in range(4):
        tasks.append(async_comprehension())

    await asyncio.gather(*tasks)

    end = time.time()
    return end - start
