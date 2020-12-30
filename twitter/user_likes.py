import json
import csv
# from twitter.utils import DateTimeEncoder

import utils
import auth
from datetime import datetime
from tqdm import tqdm
import tweepy

class user_likes:
    def __init__(self):
        self.twitter_keys, self.api = auth.auth()

    def all_likes(self, user_id, generic=True):
        max_pages=16
        if not generic:
            json_file = open("users.json","r")
            data = json.load(json_file)
            user = data[user_id]
            # print(user)
            pages = min(int(user["favorites_count:"]/20), max_pages)
            filename = user["query"]+".json"
        else:
            user = self.api.get_user(id=user_id)
            pages = min(int(user.favourites_count/20), max_pages)
            filename = "generic.json"


        for page in tqdm(range(1, pages)):
            self.likes(user_id, page=page, filename=filename)

    def likes(self, user_id, filename="generic.json", page=1):
        # utils.parse(self.api.get_user(user_id))
        c = self.check(user_id, page)
        if c == 1:
            try:
                results = self.api.favorites(id=user_id, page=page, tweet_mode="extended", trim_user=True)
                self.save_posts(user_id, results, filename=filename)
                self.save_queries(user_id, page)
            except Exception as ex:
                print("#######################")
                print(ex)
                print("#######################")

    def save_queries(self, user_id, page, fresh=False):
        if fresh:
            file_handle = open("user_favs.csv", "w")
        else:
            file_handle = open("user_favs.csv", "a")

        with file_handle as csv_file:
                row = [
                    user_id,
                    page,
                    datetime.today(),
                   ]
                writer = csv.writer(csv_file)
                writer.writerow(row)

    def check(self, user_id, page):
        with open("user_favs.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0:2] == [str(user_id), str(page)]:
                    print("already queried")
                    return 0
        return 1

    def save_posts(self, user_id, results, filename="generic.json", fresh=False):
        store = []
        utils.create_if_not_json(filename)
        with open(filename, "r") as json_file:
            data = json.load(json_file)

            if filename!="generic.json":
                json_file2 = open("users.json","r")
                data2 = json.load(json_file2)

            for result in results:

                if result.id_str in data:
                    data[result.id_str]["liked_by"] += [user_id]
                    data[result.id_str]["liked_by"] = list(set(data[result.id_str]["liked_by"]))
                    print("SIMILAR LIKES")
                    print("#######################")
                    continue
                hashtags = []
                media = []
                if "hashtags" in result.entities:
                    hashtags = [hashtag["text"] for hashtag in result.entities["hashtags"]]
                if "media" in result.entities:
                    media = [media["media_url_https"] for media in result.entities["media"]]
                
                dic = {
                    result.id_str:{
                        "creator_id": result.user.id,
                        # "post_id": result.id,
                        "created_at":result.created_at,
                        "liked_by": [user_id],
                        "text": result.full_text,
                        "hashtags": hashtags,
                        "media": media}
                        }
                data.update(dic)

                if filename!="generic.json":
                    data2[user_id]["posts_liked"]+=[result.id_str]
                    data2[user_id]["posts_liked"]=list(set(data2[user_id]["posts_liked"]))
        
        if filename!="generic.json":
            json_file2.close
            json_file2 = open("users.json","w")
            json.dump(data2, json_file2, indent=2, cls=utils.DateTimeEncoder)
            json_file2.close
                    
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4, cls=utils.DateTimeEncoder)


def main():
    s = user_likes()
    s.all_likes("295", generic=False)

    json_file = open("users.json","r")
    data = json.load(json_file)
    json_file.close()
    for id in tqdm(data.keys()):
        s.all_likes(id, generic=False)

if __name__ == "__main__":
    main()
