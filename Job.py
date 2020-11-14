from random import uniform

class Job:
    def __init__(self, title, pay, hours, physicality, sociality, flexibility, concentration, monotonity, gig, remote, tags):
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
        if self.remote:
            self.pos = None
        else:
            self.pos = (uniform(60.276, 60.151), uniform(24.855, 25.155))
        self.args = (title, pay, hours, physicality, sociality, flexibility, concentration, monotonity, gig, remote, tags)

    @classmethod
    def nJob(cls, n, args):
        return [cls(*args) for _ in range(n)]

    def __str__(self):
        return f"Job {self.title} at {self.pos}"
