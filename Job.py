from random import uniform

class Job:
    def __init__(self, title, pay, hours, physicality, sociality, flexibility, concentration, monotonity, gig, remote, tags):
        self.title = title
        self.pay = pay
        self.hours = hours
        self.physicality = physicality
        self.flexibility = flexibility
        self.concentration = concentration
        self.monotonity = monotonity
        self.gig = gig
        self.remote = remote
        self.tags = tags
        if self.remote:
            self.pos = None
        else:
            self.pos = (uniform(60.276, 60.151), uniform(24.855, 25.155))

    @classmethod
    def nJob(cls, n, args):
        return [cls(*args) for _ in range(n)]

    def __str__(self):
        return f"{self.title} at {self.pos}"
