import json
import requests

NORTH = 60.276
WEST = 24.855
EAST = 25.166
SOUTH = 60.151
URL = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"

def route_to_json(coords_a, coords_b, mode=None):
    """
    coords_a: (float, float)
    coords_b: (float, float)
    mode: joko 'walk', 'car', 'public' tai 'bicycle' (str)
    """
    # 
    mapping = {"lat_a": coords_a[0], "lon_a": coords_a[1], "lat_b": coords_b[0], "lon_b": coords_b[1]}
    # valitsee, minkä tiedoston avaa
    filename = {None: "walk.graphql", "walk": "walk.graphql", "car": "car.graphql", "public": "publictransport.graphql", "bicycle": "bicycle.graphql"}[mode]
    
    with open(filename) as f:

        data = json.dumps({"query": f.read(), "variables": {}})
        data = json.loads(data)
        
    for k, i in mapping.items():
        data["variables"][k] = str(i)
    
    return data
    
def get_data(data, url=URL):
    """
    data: json-objekti ()
    """
    headers = {"Content-type": "application/json"}
    r = requests.post(url, json=data, headers=headers)
    return r.json()

def find_route(coords_a, coords_b, mode):
    return get_data(route_to_json(coords_a, coords_b, mode))




if __name__ == "__main__":
    print(find_route((60.184305, 24.818452), (60.201002, 24.785552), "car"))
    
