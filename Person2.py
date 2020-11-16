from random import uniform
import consts
import city

N = 60

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.vehicle = ("walk", "bicycle", "public", "car")[int(args[1])]
        self.dist, self.distw = args[2]*30, args[3]
        self.pay, self.payw = args[4], args[5]
        self.hours, self.hoursw = args[6], args[7]
        self.phys, self.physw = args[8], args[9]
        self.soc, self.socw = args[10], args[11]
        self.flex, self.flexw = args[12], args[13]
        self.conc, self.concw = args[14], args[15]
        self.mono, self.monow = args[16], args[17]
        self.gig, self.gigw = args[18], args[19]
        self.remote, self.remotew = args[20], args[21]
        self.pos = args[22], args[23]
        self.tags = set(args[24])

    def __str__(self):
        return f"Person {self.name} at {self.pos}"

    def scores(self, jobs):
        n = 10
        scores = []
        job_positions = list(filter(lambda x: "None" not in str(x), [job.pos for job in jobs]))
        route_times = []
        for i in range(0, len(job_positions), N):
            lim = min(i+N, len(job_positions))
            route_times.extend(city.route_times(self.pos, job_positions[i:lim], self.vehicle))
        i = 0
        for job in jobs:
            score = 0
            if job.remote == True:
                n -= 1
            else:
                dur = route_times[i]
                score += sqerr(self.distw, self.dist, max(self.dist, dur*consts.PERSON_FACTOR_WEIGHTS[1]))
                i += 1
            score += sqerr(self.payw, self.pay, min(self.pay, job.pay))
            score += sqerr(self.hoursw, self.hours, job.hours)
            score += sqerr(self.physw, self.phys, job.phys)
            score += sqerr(self.socw, self.soc, job.soc)
            score += sqerr(self.flexw, self.flex, job.flex)
            score += sqerr(self.concw, self.conc, job.conc)
            score += sqerr(self.monow, self.mono, job.mono)
            score += sqerr(self.gigw, self.gig, job.gig)
            score += sqerr(self.remotew, self.remote, job.remote)
            scores.append(score/n)
        return scores
    
def sqerr(w, y, y_hat):
    return w * (y - y_hat)**2
