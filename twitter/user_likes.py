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

    def all_likes(self, user_id):
        user = self.api.get_user(id=user_id)
        # utils.parse(user)
        pages = min(int(user.favourites_count/20), 15)
        for page in tqdm(range(1, pages)):
            self.likes(user_id, page)

    def likes(self, user_id, page=1):
        # utils.parse(self.api.get_user(user_id))
        # intj = self.api.search_users("INTJ", page=1)
        results = self.api.favorites(id=user_id, page=page, tweet_mode="extended", trim_user=True)
        # utils.parse(results[0])   
        # print(results[0].full_text)
        self.save_posts(user_id, results)

    def save_queries(self, user_id, page, fresh=False):
        if fresh:
            file_handle = open("user_favs.csv", "w")
        else:
            file_handle = open("user_favs.csv", "a")

        with file_handle as csv_file:
                row = [
                    user_id,
                    page,
                    datetime.now(),
                   ]
                writer = csv.writer(csv_file)
                writer.writerow(row)

    def save_posts(self, user_id, results, filename="generic.json", fresh=False):
        store = []
        with open(filename, "r") as json_file:
            data = json.load(json_file)

            for result in results:

                if result.id_str in data:
                    data[result.id_str]["liked_by"] += [user_id]
                    data[result.id_str]["liked_by"] = list(set(data[result.id_str]["liked_by"]))
                    print("#######################")
                    print("SIMILAR LIKES")
                    print("#######################")
                    continue

                hashtags = []#[hashtag.text for hashtag in result.entities.hashtags]
                media = []#[media.media_url_https for media in result.entities.media]
                
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

        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4, cls=utils.DateTimeEncoder)

def main():
    s = user_likes()
    s.all_likes(75483520)

if __name__ == "__main__":
    main()
