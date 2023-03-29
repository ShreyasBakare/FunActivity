import math
import numpy as mp

###############################################
# PART 1 : Functions for vector algebra. 
# The number of dimensions is not restricted. (Only spatial dimensions)
# That means, you can try out a hypothetical universe of 35 spatial dimensions.
###############################################

class Vector:
    # vec is simply a list of numbers
    def __init__(self, vec):
        self.vec = vec
    def vector(self):
        return self.vec
    def magnitude(self):
        magsq = 0
        for i in range(len(self.vec)):
            magsq = magsq + self.vec[i]*self.vec[i]
        mag = math.sqrt(magsq)
        return mag
    def direction(self):
        mag = self.magnitude()
        direction = []
        for i in range(len(self.vec)):
            if self.vec[i] == 0 : direction.append(0)
            else : direction.append(self.vec[i]/mag)
        return direction
    def scale(self, scale):
        newvec = []
        for i in range(len(self.vec)):
            newvec.append(self.vec[i]*scale)
        return newvec

def vec_subtract(vec1, vec2):
    #Given two vectors, it returns their subtracted vector
    dvec = []
    len1, len2 = len(vec1.vector()), len(vec2.vector())
    if len1 != len2 : print("Error: Vector size mismatch!")
    else:
        for i in range(len1):
            dvec.append(vec1.vector()[i]-vec2.vector()[i])
    return Vector(dvec)

def vec_scale(vec, num):
    #This scales the vector by some num
    new_vec=[]
    for i in range(len(vec)):
        new_vec.append(vec[i]*num)
    return new_vec
        
def give_vec(mag, direction):
    #Given magnitude and direction, it returns the vector
    vec=[]
    for i in range(len(direction)):
        vec.append(mag * direction[i])
    return Vector(vec)

##########################################
#Part 2 : Properties of the particles
##########################################
class Particle:
    def __init__(self, mass, charge, pos, vel):
        #These are the properties that need user input
        self.mass = mass
        self.charge = charge
        self.pos = pos
        self.vel = vel
        #These are the derived parameters
        self.momentum = Vector(self.vel.scale(self.mass))   #kg m/s
        self.KE = 0.5 *self.mass * (self.vel.magnitude()**2) /(1.602/(10**19)) #eV

#################################################
#Part 3 : The Force acting between the particles
#################################################
def force(part1, part2):
    #Force on particle 1 by particle 2
    #Parameters of the force:
    K = 9*10**9 #Nm^2/Coulomb^2
    q1 = part1.charge
    q2 = part2.charge
    r = vec_subtract(part2.pos, part1.pos)
    rmag = r.magnitude()
    #The law:
    force_dir = r.direction()
    force_mag = -(K*q1*q2)/(rmag**2) #Newtons
    force = give_vec(force_mag, force_dir)
    return force

################################################
# Part 4 : How the system evolves with time
################################################
def nudge(particle, force, dt):
    #Given the force acting on a particle, this calculates the nudge along that direction
    ndim = len(force.vector())
    a, v, f = [], [], []
    x = particle.pos.vector() #initial position
    u = particle.vel.vector() #initial velocity
    F = force.vector() #force components
    m = particle.mass
    for i in range(ndim):
        a.append(F[i]/m)                 # a=F/m
        v.append(u[i]+a[i]*dt)           # v=u+at
        s = u[i]*dt+0.5*a[i]*dt**2       # s=ut+1/2at^2
        f.append(x[i]+s)
    return a, v, f
