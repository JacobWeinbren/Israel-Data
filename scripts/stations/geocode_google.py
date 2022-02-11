from key import gmaps

def google_process(search):
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