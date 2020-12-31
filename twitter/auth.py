import tweepy


def auth(index):

    auth = tweepy.OAuthHandler(keys[index]['consumer_key'], keys[index]['consumer_secret'])
    auth.set_access_token(keys[index]['access_token_key'], keys[index]['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return keys[index], api

if __name__ == "__main__":
    pass


keys_dict1 = {
        'consumer_key':        '7QBptQNO9Ya2XtDzjswaW27uR',
        'consumer_secret':     'HOa8SsMhNgZVfucUUSUaGtlGOvft8goeIflTuAvXM8mCsF7vWK',
        'access_token_key':    '1022541474238488576-Ap0fc5Y0ZFpmJXmd1OiqxsOkyfwm2M',
        'access_token_secret': 'DDY31UUCQhvfr1UPIZ3RFD9qCPRfZJp2JOJyfhE78mQD5'
    }

keys_dict2 = {
        'consumer_key':        'W17CnbLI4u4Ps6B1Zt6jyUyna',
        'consumer_secret':     'm78TPkFj2J79rfZzcv27By2S6hkTSCexGA0bYL8nYrARPmnNNC',
        'access_token_key':    '1022541474238488576-I95xhptviU3mPzuAg5JnyYaQY3XXCz',
        'access_token_secret': 'd8CCr2NGMuKeY4WGbpbEvGJQqOdVPEMq5Oon9gCXjyvWC'
    }

keys_dict3 = {
        'consumer_key':        'Vg9KeBpK7nUSCK3RsmuVLUQe9',
        'consumer_secret':     'Uj4fPOyGA2JyeSD9X3Y2CanmHhNMgSfq0U6EFrka2YBPLDbAGb',
        'access_token_key':    '1022541474238488576-P9BIEUlD2jK0WMJ9kvLlrkY7pUjVa5',
        'access_token_secret': 'ryvuxzTr0CiS5I2KJZShcY3xZT6uzwukunBgMpHYgQzds'
    }

keys_dict4 = {
        'consumer_key':        'C9sToGtPeptYwtpOvik5DWDVp',
        'consumer_secret':     'MmuLr8L8eVS60gp3RDyGLgFCuUKGhGuKs8wIRhbXZ9x11B52qr',
        'access_token_key':    '1022541474238488576-U6VhHoEBw57EjfH1Ag0iJws9PLdzj5',
        'access_token_secret': '1dtsmHEhNZHcKsMnHNAoDop2zLcJA0RuM2O2QKYpWmffP'
    }

keys = [keys_dict1, keys_dict2, keys_dict3, keys_dict4]
