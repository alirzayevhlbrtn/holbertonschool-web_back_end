#!/usr/bin/env python3
"""
task 4
"""
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """doc func"""
    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(tasks)
