import json
import csv

# import utils
import auth
from datetime import datetime
from tqdm import tqdm
import tweepy

class search:
    def __init__(self):
        self.twitter_keys, self.api = auth.auth()

    def search_all(self, query):
        for i in tqdm(range(1, 52)):
            self.search(query, i)

    def search(self, query, page=None):
        c = self.check(query, page)
        if c == 1:
            results = self.api.search_users(query, page=page)
            # utils.parse(results[0])
            self.save_results(query, page, results)

    def save_results(self, query, page, results, fresh=False):
        if fresh:
            file_handle = open("users.csv", "w")
        else:
            file_handle = open("users.csv", "a")

        with file_handle as csv_file:
            for result in results:
                if self.profile_validity(query, result):
                    row = [
                        query,
                        page,
                        datetime.now(),
                        result.id,
                        result.screen_name,
                        result.name,
                        result.description,
                    ]
                    writer = csv.writer(csv_file)
                    writer.writerow(row)

    def check(self, query, page):
        with open("users.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0:2] == [str(query), str(page)]:
                    print("already queried")
                    return 0
        return 1

    def profile_validity(self, query, result):
        query = query.lower()
        name = result.name.lower()
        display_name = result.screen_name.lower()
        description = result.description.lower()
        return query not in name and query not in display_name and query in description


def main():
    s = search()
    keywords = [
        "INTJ",
        "INTP",
        "ENTP",
        "ENTJ",
        "INFJ",
        "INFP",
        "ENFP",
        "ENFJ",
        "ISTJ",
        "ISFJ",
        "ESTJ",
        "ESFJ",
        "ISTP",
        "ISFP",
        "ESTP",
        "ESFP",
    ]
    for keyword in keywords:
        s.search_all(keyword)


if __name__ == "__main__":
    main()
