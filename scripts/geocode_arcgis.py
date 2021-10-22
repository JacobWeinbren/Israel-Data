import requests

from key import token

def arc_process(search):
    result = requests.get(
        'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates',
        params={
            'address': search,
            'token': token,
            'forStorage': 'false',
            'sourceCountry': 'ISR',
            'f': 'pjson'
        }
    )

    result = result.json()['candidates']

    if len(result):
        result = result[0]['location']
        return {'lat':result['y'], 'lng':result['x']}