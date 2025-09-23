# File: mainCT3.py
# Written by: Angel Hernandez
# Description: Module 3 - Critical Thinking
# Requirement(s): Bubble sort and merge sort algorithms

import os
from datetime import datetime

class Patient:
    def __init__(self, name: str, admission_date: str):
        self.name = name
        self.admission_date = datetime.strptime(admission_date, "%Y-%m-%d")

    def __repr__(self):
        return f"{self.name} ({self.admission_date.date()})"

class SortEngine:
    def get_admission_date(self, patient: Patient):
        return patient.admission_date

    # Bubble Sort implementation
    def bubble_sort(self, records, key_func):
        n = len(records)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key_func(records[j]) > key_func(records[j + 1]):
                    records[j], records[j + 1] = records[j + 1], records[j]
        return records

    # Merge Sort implementation
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
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 3 - Critical Thinking ***\n')

        patient_records = [
            Patient("Angel", "2023-06-15"),
            Patient("James", "2023-03-22"),
            Patient("Sarah", "2023-08-01"),
            Patient("John", "2023-01-10")
        ]

        sort_engine = SortEngine()
        print("Bubble Sort Result:")
        sorted_bubble = sort_engine.bubble_sort(patient_records.copy(), sort_engine.get_admission_date)
        for patient in sorted_bubble:
            print(patient)

        print("\nMerge Sort Result:")
        sorted_merge = sort_engine.merge_sort(patient_records.copy(), sort_engine.get_admission_date)
        for patient in sorted_merge:
            print(patient)

    except Exception as e:
        print(e)

if __name__ == '__main__': main()
