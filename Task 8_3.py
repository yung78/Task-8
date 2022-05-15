import requests
from pprint import pprint


def py_requests():
    python_requests = []
    params = {'fromdate': 1652486400, 'todate': 1652572800, 'order': 'asc', 'sort': 'creation', 'site': 'stackoverflow'}
    request = requests.get('https://api.stackexchange.com/2.3/questions/', params=params)
    for items in request.json()['items']:
        if 'python' in items['tags']:
            python_requests.append(items)
    pprint(python_requests)


py_requests()
