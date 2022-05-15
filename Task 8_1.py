import requests


def most_intelligence():
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    intel = 0
    most_intelligence_hero = ''
    for name in hero_list:
        url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        resp = requests.get(url)
        resp_results = resp.json()['results'][0]
        if int(resp_results['powerstats']['intelligence']) > intel:
            intel = int(resp_results['powerstats']['intelligence'])
            most_intelligence_hero = resp_results['name']
    print(f'Самый умный супергерой - {most_intelligence_hero}. Его интеллект(intelligence) = {intel}')


most_intelligence()
