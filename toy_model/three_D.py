import numpy as np

class Effusion():
    count = 0

    def __init__(self, file):
        self.trajectory = file
        self.effusion = []
        self.block = False
        self.bottom = 0.04
        self.channel_width = []

    def parse_cordinates(self, n, f):
        fluid = []
        piston = []
        channel_up = []
        for i in range(n):
            line = f.readline()
            clean = [float(i) for i in line.split()]

            if clean[1] == 1.0:
                piston.append(clean[-1])
            if clean[1] == 3.0 or clean[1] == 4.0:
                fluid.append(clean[-1])
            if clean[1] == 2.0 and clean[-1] > self.bottom:
                channel_up.append(clean[-1])

        piston_height = sum(piston)/len(piston)
        escaped_atom = [i for i in fluid if i < self.bottom or i > piston_height]
        self.effusion.append(len(escaped_atom))
        channel_up = np.array(channel_up)

        self.channel_width.append(channel_up.mean())



    def header(self, f):
        for i in range(2):
            f.readline()
        n = int(f.readline())

        for i in range(5):
            a = f.readline()

        assert(a == "ITEM: ATOMS id type xs ys zs\n")
        self.parse_cordinates(n, f)

    def run(self):
        self.effusion = []
        with open(self.trajectory, 'r') as rad:
            while True:
                line = rad.readline()

                if not line:
                    break
                assert(line == "ITEM: TIMESTEP\n")
                self.header(rad)
    @property
    def effusion_rate(self):
        eff = self.effusion[20:]
        time = [i for i in range(len(eff))]
        k, _ = np.polyfit(time, eff, 1)
        return k
<<<<<<< HEAD
    
=======
    
>>>>>>> 52ff74fc71cdaebc5e77eb82f8687ce840a2d7d2
