import requests
import json
from ebaysdk.finding import Connection as Finding

api = Finding(appid='AlexisMo-pricepre-SBX-5091f4dec-03d3d393', config_file=None)
api.execute('findCompletedItems', {'categoryId': '619'})
print(api.response_dict())