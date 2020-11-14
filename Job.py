from random import uniform
import city

class Job:
    def __init__(self, title, pay, hours, physicality, sociality, flexibility, concentration, monotonity, gig, remote, tags, pos):
        self.title = title
        self.pay = pay
        self.hours = hours
        self.phys = physicality
        self.soc = sociality
        self.flex = flexibility
        self.conc = concentration
        self.mono = monotonity
        self.gig = gig
        self.remote = remote
        self.tags = tags
        self.pos = pos

    @classmethod
    def nJob(cls, n, args, coords):
        return [cls(*args, coords[i]) for i in range(n)]

    def __str__(self):
        return f"Job {self.title} at {self.pos}"
