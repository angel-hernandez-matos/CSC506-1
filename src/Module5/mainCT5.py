# File: mainCT5.py
# Written by: Angel Hernandez
# Description: Module 4 - Portfolio Milestone
# Requirement(s): Hashtable implementation

import os
import random


class HashTable:
    def __init__(self, size=500):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __iter__(self):
        return iter(self.table)

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

class TestCaseRunner:
    @staticmethod
    def run_test():
        users = HashTable()
        recommended_content = HashTable()
        preferences = [["politics", "music", "movies"], ["sports","stock market", "science"],
                       ["technology", "gaming", "live events"]]
        available_posts = [["technology", "ai", "r&d"], ["live events", "sports", "baseball"],
                           ["stock market", "politics", "corporate"], ["music", "concert", "rock"],
                           ["science", "computers", "cloud"]]
        for _ in range(0,5,1):
            user = f"user{_ + 1}"
            users.insert(user, preferences[random.randint(0, len(preferences)-1)])
            recommended_content.insert(f"page{_+1}", available_posts[random.randint(0, len(available_posts)-1)])

        recommendation_engine = RecommendationEngine(users, recommended_content)

        for user in users:
            print(f"\nRecommendations for {user}")
            for c in recommendation_engine.recommend(user):
                print(c)

class RecommendationEngine:
    def __init__(self, users, recommended_content):
        self.users = users
        self.recommended_content = recommended_content

    def recommend(self, user_id):
        recommendations = []
        prefs = self.users.get(user_id)
        for i in range(self.recommended_content.size):
            for k, t in self.recommended_content.table[i]:
                if any(tag in prefs for tag in t):
                    recommendations.append(k)
        return recommendations

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    try:
        clear_screen()
        print('*** Module 5 - Critical Thinking ***\n')
        TestCaseRunner.run_test()

    except Exception as e:
        print(e)

if __name__ == '__main__':  main()