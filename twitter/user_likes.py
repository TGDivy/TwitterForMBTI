import json
import csv

import utils
import auth
from datetime import datetime
from tqdm import tqdm
import tweepy

class user_likes:
    def __init__(self):
        self.twitter_keys, self.api = auth.auth()

    def search_all(self, query):
        pass

    def likes(self, user_id, page=1):
        # utils.parse(self.api.get_user(user_id))
        # intj = self.api.search_users("INTJ", page=1)
        results = self.api.favorites(id=user_id,page=page)
        utils.parse(results[0])
        print(results[0].text)

    def save_results(self, query, page, results, fresh=False):
        pass

def main():
    s = user_likes()
    s.likes(21755329)

if __name__ == "__main__":
    main()
