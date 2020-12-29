import tweepy
import json



consumer_key = "7QBptQNO9Ya2XtDzjswaW27uR"
consumer_secret = "HOa8SsMhNgZVfucUUSUaGtlGOvft8goeIflTuAvXM8mCsF7vWK"

access_token = "1022541474238488576-Ap0fc5Y0ZFpmJXmd1OiqxsOkyfwm2M"
access_token_secret = "DDY31UUCQhvfr1UPIZ3RFD9qCPRfZJp2JOJyfhE78mQD5"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAKxcKwEAAAAAF1rQn%2F3yaM%2FAuDUb24CviQVCHGE%3DxwnFkaJM2CJIVzdWAN5twTNRcqkvCf17tE4CrJUOTUjBeREJ9d"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# user = 

public_tweets = api.home_timeline()

intj = api.search_users("INTJ", page=1)

status = public_tweets[0]

user_id = status.user.id

print(user_id)
for i in intj:
    print(i.name, i.id)
print(api.favorites(intj[0].id)[0].text)    
# parse(intj[0])
# parse(api.get_user(user_id))



# for tweet in public_tweets:
#     print("-"*50)
#     print(type(tweet)
#     # print(tweet.)
