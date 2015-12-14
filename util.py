
def getPlaces(api, place, granularity="country"):
    places = api.geo_search(query=place, granularity=granularity)
    return places

def getPlaceID(api, place, granularity="country"):
    places = api.geo_search(query=place, granularity=granularity)
    if not places:
        raise ValueError("Bad place name.")
    return places[0].id