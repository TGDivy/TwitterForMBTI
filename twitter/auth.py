import tweepy

keys_dict = {
        'consumer_key':        '7QBptQNO9Ya2XtDzjswaW27uR',
        'consumer_secret':     'HOa8SsMhNgZVfucUUSUaGtlGOvft8goeIflTuAvXM8mCsF7vWK',
        'access_token_key':    '1022541474238488576-Ap0fc5Y0ZFpmJXmd1OiqxsOkyfwm2M',
        'access_token_secret': 'DDY31UUCQhvfr1UPIZ3RFD9qCPRfZJp2JOJyfhE78mQD5'
    }

def auth():

    auth = tweepy.OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
    auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return keys_dict, api

if __name__ == "__main__":
    pass