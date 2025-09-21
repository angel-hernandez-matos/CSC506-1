# File: mainCPM2.py
# Written by: Angel Hernandez
# Description: Module 2 - Portfolio Milestone
# Requirement(s): Cache Simulation Framework

import os
from enum import Enum, auto
from collections import deque

class CachePolicy(Enum):
    LRU = auto()
    FIFO = auto()

class CacheSimulator:
    def __init__(self, size, policy):
        self.cache = {}
        self.size = size
        self.order = deque()
        self.policy = policy
        self.access_history = []
        self.misses = self.hits = 0

    def access(self, address):
        self.access_history.append(address)
        if address in self.cache:
            self.hits += 1
            if self.policy == CachePolicy.LRU:
                self.order.remove(address)
                self.order.append(address)
        else:
            self.misses += 1
            if len(self.cache) >= self.size:
                evict = self.order.popleft()
                del self.cache[evict]
            self.cache[address] = True
            self.order.append(address)

    def report(self):
        print(f"Policy: {self.policy.name}")
        print(f"Total Accesses: {len(self.access_history)}")
        print(f"Cache Hits: {self.hits}")
        print(f"Cache Misses: {self.misses}")
        hit_rate = self.hits / len(self.access_history) * 100
        print(f"Hit Rate: {hit_rate:.2f}%")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 2 - Portfolio Milestone ***\n')
        items =  ['Angel', 'John', 'Charles', 'Angel', 'Kate', 'William', 'Angel', 'Sarah']
        cache_policy_operations = [
            ("\n*** LRU Simulation ***", CacheSimulator(size=4, policy=CachePolicy.LRU)),
            ("\n*** FIFO Simulation ***", CacheSimulator(size=4, policy=CachePolicy.FIFO))
        ]

        for label, policy in cache_policy_operations:
            print(label)
            for name in items:
                policy.access(name)
            policy.report()

    except Exception as e:
        print(e)

if __name__ == '__main__': main()
