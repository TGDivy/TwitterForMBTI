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
        self.saved = 0
        for i in tqdm(range(1, 52)):
            self.search(query, i)
        print("total saved of ",query, self.saved)

    def search(self, query, page=None):
        c = self.check("#"+query, page)
        if c == 1:
            try:
                results = self.api.search_users("#"+query, page=page)
                # utils.parse(results[0])
                self.save_results(query, page, results)
            except Exception as ex:
                print("#######################")
                print(ex)
                print("#######################")

    def save_results(self, query, page, results, fresh=False):
        if fresh:
            json_file = open("users.json", "w")
            json_file2 = open("users_likes.json", "w")
        else:
            json_file = open("users.json", "r")
            json_file2 = open("users_likes.json", "r")

        data = json.load(json_file)
        data2 = json.load(json_file2)
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
                        # "posts_liked":[],
                        # "posts_posted":[],
                        "query":query,
                        "type":query,
                        "page":page,
                        "favorites_count:":result.favourites_count,
                        "statuses_count":result.statuses_count,
                        "location":result.location,
                        "queried_at":datetime.today()}
                }
                dic2 = {result.id_str: {"posts_liked":[], "posts_posted":[] }}
                
                data.update(dic)
                data2.update(dic2)
                self.saved+=1
        json_file.close
        json_file2.close

        with open("users.json", "w") as json_file:
            json.dump(data, json_file, indent=4, cls=utils.DateTimeEncoder)
        with open("users_likes.json", "w") as json_file:
            json.dump(data2, json_file, indent=4, cls=utils.DateTimeEncoder)

    def check(self, query, page):
        with open("users.json", "r") as json_file:
            data = json.load(json_file)
            for id in data.keys():
                if str(data[id]["query"]) == str(query) and str(data[id]["page"]) == str(page):
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
