#Israel
#34.2654333839, 29.5013261988, 35.8363969256, 33.2774264593

#Palestine
#31.2201289  32.5521479  34.0689732  35.5739235

from key import gmaps

def geocode_process(search):
    result = gmaps.geocode(
        search, 
        components={"country": ['IL', 'PS']}, 
        bounds={"southwest": (29.159416, 33.947754),"northeast": (33.705577, 36.365314)}, 
        region="il"
    )
    if len(result):
        return result[0]['geometry']['location']
    else:
        return None

#print(geocode_process('רבי צדוק,12 ‭'))