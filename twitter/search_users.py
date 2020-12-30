import json
import csv

import utils
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
            file_handle = open("users.json", "w")
        else:
            file_handle = open("users.json", "r")

        with file_handle as json_file:
            data = json.load(json_file)
            for result in results:
                if result.id_str in data:
                    continue

                if self.profile_validity(query, result):
                    dic = {
                        result.id_str:
                           {"screen_name":result.screen_name,
                            "name":result.name,
                            "bio":result.description,
                            "MBTI type":"",
                            "posts_liked":[],
                            "posts_posted":[],
                            "query":query,
                            "page":page,
                            "favorites_count:":result.favourites_count,
                            "statuses_count":result.statuses_count,
                            "location":result.location,
                            "queried_at":datetime.today()}
                    }
                    data.update(dic)

        with open("users.json", "w") as json_file:
            json.dump(data, json_file, indent=4, cls=utils.DateTimeEncoder)

    def check(self, query, page):
        with open("users.json", "r") as json_file:
            data = json.load(json_file)
            for id in data.keys():
                if data[id]["query"] == str(query) and data[id]["page"] == str(page):
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
