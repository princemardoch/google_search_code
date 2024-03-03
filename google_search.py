import requests
import json
from readpage import lect


def google_search(search_term, api_key, cse_id, **kwargs):
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
        'num':1
    }
    params.update(kwargs)
    response = requests.get(service_url, params=params)
    return json.loads(response.text)


def searchh(t):
    results = google_search(t,'AIzaSyBrFiOFCnmBeT57-HZKTBIKfCOCgUQLXDU','027034bd444a24b83')


    for result in results['items']:
        if results['items']:
            url = result['link']
            lect(url)

tt = input('Votre recherche : ')
searchh(tt)