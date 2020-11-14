class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.vehicle = args[1]
        self.pay, self.payw = args[2]
        self.hours, self.hoursw = args[3]
        self.physicality, self.physicalityw = args[4]
        self.sociality, self.socialityw = args[5]
        self.flexibility, self.flexibilityw = args[6]
        self.concentration, self.concentrationc = args[7]
        self.monotonity, self.monotonityc = args[8]
        self.gig, self.gigc = args[9]
        self.remote, self.remotec = args[10]
        self.tags = args[11]
        self.pos = (uniform(60.276, 60.151), uniform(24.855, 25.155))

