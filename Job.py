from random import uniform
import city

class Job:
    def __init__(self, title, id_num,  pay, hours, physicality, sociality, flexibility, concentration, monotonity, gig, remote, tags, coords):
        self.title = title
        self.id = int(id_num)
        self.pay = pay
        self.hours = hours
        self.phys = physicality
        self.soc = sociality
        self.flex = flexibility
        self.conc = concentration
        self.mono = monotonity
        self.gig = gig
        self.remote = remote
        self.tags = set(tags)
        self.pos = coords

    @classmethod
    def nJob(cls, n, args, coords):
        return [cls(*args, pos=coords[i]) for i in range(n)]

    def __str__(self):
        return f"Job {self.title}#{self.id} at {self.pos}"
