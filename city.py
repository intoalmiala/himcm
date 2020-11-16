import coordinates
import requests

JOBFILE = NotImplemented


class Sim:

    def __init__(self, jobs_amount, people):
        self.jobs = [random_job() for i in range(jobs_amount)]
        self.people = people

    @staticmethod
    def route_time(person, job, mode=None):
        return coordinates.find_route(person["location"], job["location"], mode)["data"]["plan"]["itineraries"]["legs"]["duration"]

    @staticmethod
    def random_job():
        pass

def route_time(person_pos, job_pos, mode=None):
    # etätyö
    if job_pos in (None, "None", ("None", "None"), (None, None)):
        return None
    route_found = False
    while not route_found:
        try:
            routes = coordinates.find_route(person_pos, job_pos, mode)["data"]["plan"]["itineraries"]
            route_found = True
        except:
            print("O-ou")
            continue

    try:
        route = routes[0]["legs"]
    except IndexError:
        return -1
    # palauttaa kaikkien liikennevälineiden kestojen summan
    return sum(map(lambda r: r["duration"], route))

def route_times(person_pos, job_positions, mode):
    route_found = False
    while not route_found:
        try:
            l = [(person_pos, job_pos, mode) for job_pos in job_positions]
            routes = coordinates.find_routes(l)["data"]
            result = []
            for i in range(len(job_positions)):
                try:
                    route = routes[f"plan{i}"]["itineraries"][0]["legs"]
                    result.append(sum(map(lambda r: r["duration"], route)))
                except IndexError:
                    result.append(-1)

            route_found = True
        except requests.ConnectTimeout as E:
            print(E.args)
            print("O-ou")
            continue
    return result

