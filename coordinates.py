import json
import requests

NORTH = 60.243872
WEST = 24.859716
EAST = 24.955315
SOUTH = 60.155310
URL = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"

MAPPING = {
    "bicycle": "plan(\
        from: {lat: $lat_a, lon: $lon_a},\
        to: {lat: $lat_b, lon: $lon_b},\
        transportModes: [{mode: BICYCLE}, {mode: WALK}],\
        date: \"2020-11-16\",\
        time: \"08:00:00\"\
    ) {\
        itineraries {\
            legs {\
                duration\
                distance\
                mode\
            }\
          	walkDistance\
        }\
    }",
    "car": "plan(\
        from: {lat: $lat_a, lon: $lon_a},\
        to: {lat: $lat_b, lon: $lon_b},\
        transportModes: [{mode: CAR}, {mode: WALK}],\
        date: \"2020-11-16\",\
        time: \"08:00:00\"\
    ) {\
        itineraries {\
            legs {\
                duration\
                distance\
                mode\
            }\
          	walkDistance\
        }\
    }",
    "walk": "plan(\
        from: {lat: $lat_a, lon: $lon_a},\
        to: {lat: $lat_b, lon: $lon_b},\
        transportModes: [{mode: WALK}],\
        date: \"2020-11-16\",\
        time: \"08:00:00\"\
    ) {\
        itineraries {\
            legs {\
                duration\
                distance\
                mode\
            }\
          	walkDistance\
        }\
    }",
    "public": "plan(\
        from: {lat: $lat_a, lon: $lon_a},\
        to: {lat: $lat_b, lon: $lon_b},\
        transportModes: [{mode: BUS}, {mode: RAIL}, {mode: TRAM}, {mode: SUBWAY}, {mode: WALK}],\
        date: \"2020-11-16\",\
        time: \"08:00:00\"\
    ) {\
        itineraries {\
            legs {\
                duration\
                distance\
                mode\
            }\
          	walkDistance\
        }\
    }"
}


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

def query(i, mode):
    with open(f"{mode}.graphql") as f:
        string = f.read()
    string = string.replace("$lat_", f"$lat_{i}").replace("$lon_", f"$lon_{i}")
    return string

def routes_to_json(triples):
    mapping = lambda i: {f"lat_{i}a": triples[i][0][0], f"lon_{i}a": triples[i][0][1], f"lat_{i}b": triples[i][1][0], f"lon_{i}b": triples[i][1][1]}
    first_part = "query Plan("
    row = ", ".join(f"$lat_{i}a: Float!, $lon_{i}a: Float!, $lat_{i}a: Float!, $lon_{i}: Float!" for i in range(len(triples)))
    data = json.dumps({"query": first_part + ") {\n", "variables": {}})
    data = json.loads(data)
    for i in range(len(triples)):
        data["query"] += f"plan{i}: " + MAPPING[triples[i][2]].replace("$lat_", f"$lat_{i}").replace("$lon_", f"$lon_{i}")
        for k, j in mapping(i).items():
            data["variables"][k] = j
    inputs = ", ".join(["$" + k + ": Float!" for k in data["variables"].keys()])
    data["query"] = data["query"].replace("Plan(", f"Plan({inputs}")
    data["query"] += "\n}" 
    return data

    
def get_data(data, url=URL):
    """
    data: json-objekti ()
    """
    headers = {"Content-type": "application/json"}
    r = requests.post(url, json=data, headers=headers, )
    print("Request handled")
    return r.json()


def find_route(coords_a, coords_b, mode):
    return get_data(route_to_json(coords_a, coords_b, mode))


def find_routes(triples):
    
    return get_data(routes_to_json(triples))

if __name__ == "__main__":
    d = routes_to_json([((60.184305, 24.818452), (60.201002, 24.785552), "car"), ((60.1578212711756,24.9664396778104), (60.198701668464,25.0051405126794), "walk")])
    print(json.dumps(d, indent=2))
    print(get_data(d))
