
def get_places(api, place, granularity="country"):
    places = api.geo_search(query=place, granularity=granularity)
    if not places:
        raise ValueError("Bad place name.")
    return places

def get_place_id(api, place, granularity="country"):
    places = api.geo_search(query=place, granularity=granularity)
    if not places:
        raise ValueError("Bad place name.")
    return places[0].id

