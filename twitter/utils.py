import json
import datetime
import os

def parse(obj, printit=True):
    #convert to string
    json_str = json.dumps(obj._json)
    #deserialise string into python object
    parsed = json.loads(json_str)
    prettyParsed = json.dumps(parsed, indent=4, sort_keys=True)
    if(printit==True):
        print(prettyParsed)
    return prettyParsed

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

def create_if_not_json(filename):
    if not os.path.exists(filename):
        a = open(filename, 'w')
        a.write("{ }\n")
        a.close()