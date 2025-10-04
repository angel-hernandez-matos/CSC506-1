# File: mainPM4.py
# Written by: Angel Hernandez
# Description: Module 4 - Portfolio Milestone
# Requirement(s): Queue implementation

import os

class Messages:
    PEEK = "Peek:"
    SIZE = "Size:"
    ENQUEUED = "Enqueued:"
    DEQUEUED = "Dequeued:"
    QUEUE_CONTENTS = "The queue contents are:"
    EMPTY_QUEUE_PEEK = "The queue is empty. Nothing to peek."
    EMPTY_QUEUE_DEQUEUE = "The queue is empty. Cannot dequeue."

class TestCaseRunner:
    @staticmethod
    def run_test():
        q = Queue()
        # Queuing items and showing them
        q.enqueue("Angel")
        q.enqueue("Sarah")
        q.enqueue("John")
        q.display()
        # Dequeuing and showing after
        q.dequeue()
        q.display()
        # Peeking and then showing size
        print(Messages.PEEK, q.peek())
        print(Messages.SIZE, q.size())

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{Messages.ENQUEUED} {item}")

    def dequeue(self):
        if self.is_empty():
            print(Messages.EMPTY_QUEUE_DEQUEUE)
            return None
        item = self.items.pop(0)
        print(f"{Messages.DEQUEUED} {item}")
        return item

    def peek(self):
        if self.is_empty():
            print(Messages.EMPTY_QUEUE_PEEK)
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print(f"{Messages.QUEUE_CONTENTS}", self.items)

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 4 - Portfolio Milestone ***\n')
        TestCaseRunner.run_test()
    except Exception as e:
        print(e)

if __name__ == '__main__':  main()