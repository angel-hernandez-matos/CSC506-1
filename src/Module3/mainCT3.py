# File: mainCT3.py
# Written by: Angel Hernandez
# Description: Module 3 - Critical Thinking
# Requirement(s): Bubble sort and merge sort algorithms

import os
import time
from enum import Enum
from datetime import datetime

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class SortKey(Enum):
    NAME = "name"
    SURNAME = "surname"
    PATIENT_ID = "patient_id"
    GENDER = "gender"
    ADMISSION_DATE = "admission_date"

class Patient:
    def __init__(self, name: str, surname: str, patient_id: int, gender: Gender, admission_date: str):
        self.name = name
        self.surname = surname
        self.patient_id = patient_id
        self.gender = gender
        self.admission_date = datetime.strptime(admission_date, "%Y-%m-%d")

    def __repr__(self):
        return (
            f"{self.name} {self.surname} | ID: {self.patient_id} "
            f"| Gender: {self.gender.value} | Date: {self.admission_date.date()}"
        )

class SortEngine:
    def get_key_func(self, sort_key: SortKey):
        return {
            SortKey.NAME: lambda p: p.name,
            SortKey.SURNAME: lambda p: p.surname,
            SortKey.PATIENT_ID: lambda p: p.patient_id,
            SortKey.GENDER: lambda p: p.gender.value,
            SortKey.ADMISSION_DATE: lambda p: p.admission_date
        }[sort_key]

    def bubble_sort(self, records, key_func):
        n = len(records)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key_func(records[j]) > key_func(records[j + 1]):
                    records[j], records[j + 1] = records[j + 1], records[j]
        return records

    def merge_sort(self, records, key_func):
        if len(records) <= 1:
            return records

        mid = len(records) // 2
        left = self.merge_sort(records[:mid], key_func)
        right = self.merge_sort(records[mid:], key_func)

        return self.merge(left, right, key_func)

    def merge(self, left, right, key_func):
        retval = []
        i = j = 0

        while i < len(left) and j < len(right):
            if key_func(left[i]) <= key_func(right[j]):
                retval.append(left[i])
                i += 1
            else:
                retval.append(right[j])
                j += 1

        retval.extend(left[i:])
        retval.extend(right[j:])
        return retval

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 3 - Critical Thinking ***\n')

        patient_records = [
            Patient("Angel", "Hernandez", 101, Gender.MALE, "2025-06-15"),
            Patient("James", "Smith", 102, Gender.MALE, "2025-03-22"),
            Patient("Sarah", "Johnson", 103, Gender.FEMALE, "2025-08-01"),
            Patient("John", "Doe", 104, Gender.MALE, "2025-01-10")
        ]

        sort_engine = SortEngine()

        sort_keys = [SortKey.ADMISSION_DATE, SortKey.PATIENT_ID, SortKey.GENDER, SortKey.ADMISSION_DATE, SortKey.NAME,
                     SortKey.SURNAME]

        print("Sort keys available")
        print('*' * 19)

        for x,k in enumerate(sort_keys, start=1):
            print(f"Press {x}: to sort by {k}")

        selected_sort = int(input("\nWhich sort key would you like to use? "))
        sort_by = sort_keys[selected_sort - 1] if 1 <= selected_sort <= len(sort_keys) else SortKey.PATIENT_ID
        key_func = sort_engine.get_key_func(sort_by)
        print(f"\nSorting by: {sort_by.name}\n")

        sort_ops = [("Bubble Sort Result", sort_engine.bubble_sort, "Bubble Sort Time"),
                    ("Merge Sort Result", sort_engine.merge_sort, "Merge Sort Time")]

        for sort, callback, execution in sort_ops:
            start = time.perf_counter()
            sorted_records = callback(patient_records.copy(), key_func)
            end = time.perf_counter()
            print(f"\n{sort}:")
            print('*' * len(sort))
            for patient in sorted_records:
                print(patient)
            print(f"\n{execution}: {end - start:.6f} seconds.\n")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()