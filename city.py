import coordinates

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

def route_time(person, job, mode=None):
    # etätyö
    if job.pos is None:
        return 0
    route = coordinates.find_route(person.pos, job.pos, mode)["data"]["plan"]["itineraries"][0]["legs"]
    # palauttaa kaikkien liikennevälineiden kestojen summan
    return sum(map(lambda r: r["duration"], route))


p = {"location": (60.184305, 24.818452)}
j = {"location": (60.201002, 24.785552)}
print(route_time(p, j, "public"))