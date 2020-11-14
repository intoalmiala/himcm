from random import uniform
import city

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.vehicle = ("walk", "bicycle", "public", "car")[args[1]]
        self.dist, self.distw = args[3], args[3]
        self.pay, self.payw = args[3], args[4]
        self.hours, self.hoursw = args[5], args[6]
        self.phys, self.physw = args[7], args[8]
        self.soc, self.socw = args[9], args[10]
        self.flex, self.flexw = args[11], args[12]
        self.conc, self.concw = args[13], args[14]
        self.mono, self.monow = args[15], args[16]
        self.gig, self.gigw = args[17], args[18]
        self.remote, self.remotew = args[19], args[20]
        self.tags = args[21]
        self.pos = (uniform(60.276, 60.151), uniform(24.855, 25.155))

    def __str__(self):
        return f"Person {self.name} at {self.pos}"

    def score(self, job):
        dur = city.route_time(self, job, self.vehicle)
        score = sqerr(self.distw, self.dist*60, max(self.dist*60, dur))
        score += sqerr(self.payw, self.pay, min(self.pay, job.pay))
        score += sqerr(self.hoursw, self.hours, job.hours)
        score += sqerr(self.physw, self.phys, job.phys)
        score += sqerr(self.socw, self.soc, job.soc)
        score += sqerr(self.flexw, self.flex, job.flex)
        score += sqerr(self.concw, self.sc, job.conc)
        score += sqerr(self.monow, self.sc, job.mono)
        score += sqerr(self.gigw, self.sc, job.gig)
        score += sqerr(self.remotew, self.sc, job.remote)
        return score
    
    @staticmethod
    def sqerr(w, y, y_hat):
        return w * (y - y_hat)**2
