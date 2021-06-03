import requests, ujson

from key import token

count = 0

def arc_process(search):
    global count
    try:
        if count <= 5:
            result = requests.get(
                'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates',
                params={
                    'address': search,
                    'token': token,
                    'forStorage': 'false',
                    'sourceCountry': 'ISR',
                    'f': 'pjson'
                }
            ).json()['candidates']

            if len(result):
                count = 0
                result = result[0]['location']
                return {'lat':result['y'], 'lng':result['x']}
            else:
                return None
        else:
            return None
    except:
        count ++ 1
        arc_process(search)