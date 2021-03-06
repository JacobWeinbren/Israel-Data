import requests
from key import token

"""
Geocodes using ArcGIS Credits
"""

def arc_process(search):
    try:
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
        else:
            return None
    except Exception as e: 
        print(e)
        return None