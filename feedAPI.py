import requests

def feed_it(artist, date):
    url = 'http://localhost/api/v1/events'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization':  "Bearer " + '2|MDybuSA2L23uICjpYchwoqF07enRpwvuuiYD11Y32f517b7a', 'accept': 'application/json'}
    data = {'name': artist, 'place_id': '1', 'organizer_id': '1', 'day': date,'timeofday': '20.00', 'link': 'https://fasching.se'}
    requests.post(url,headers=headers, data=data)