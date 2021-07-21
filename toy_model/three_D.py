class Effusion():
    count = 0

    def __init__(self, file):
        self.trajectory = file
        self.effusion = []
        self.effusion_rate = 0
        self.block = False
        self.bottom = 0.04

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



    def header(self, f):
        for i in range(2):
            f.readline()
        n = int(f.readline())

        for i in range(5):
            a = f.readline()

        assert(a == "ITEM: ATOMS id type xs ys zs\n")
        self.parse_cordinates(n, f)

    def run(self):
        self.effusion_rate = 0
        self.effusion = []
        with open(self.trajectory, 'r') as rad:
            while True:
                line = rad.readline()

                if not line:
                    break
                assert(line == "ITEM: TIMESTEP\n")
                self.header(rad)