class Stone:
    def __init__(self, input):
        p,v = input.split('@')
        self.input = input
        self.pos = tuple(int(i) for i in p.split(','))
        self.vel = tuple(int(i) for i in v.split(','))
    
    def __str__(self):
        return self.input
    
    def pos(self, t):
        return (self.vel[0]*t + self.pos[0], self.vel[1]*t + self.pos[2], self.vel[2]*t + self.pos[2])