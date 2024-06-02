
#TODO: Noch in das System einbinden!!

from sensor import *

class Liver():
    
    def __init__(self, viscosity, maxTime, dt=0.01):
        self.viscosity = viscosity
        self.time = np.arange(0, maxTime, dt)

    def getViscosity(self):
        return self.viscosity

    def setViscosity(self, vis):
        self.viscosity = vis
    
    def increaseViscosity(self, inc):
        self.viscosity += inc
        self.viscosity = round(self.viscosity, 2)
        #if self.viscosity <= 0:
        #    self.viscosity = 1
        #elif self.viscosity >= 100:
        #    self.viscosity = 100

    def decreaseViscosity(self, dec):
        self.viscosity -= dec
        self.viscosity = round(self.viscosity, 2)
        #if self.viscosity <= 0:
        #    self.viscosity = 1
        #elif self.viscosity >= 100:
        #    self.viscosity = 100
    
    def viscositySimulate(self, prop, interval, change):
        if interval != 0:
            if prop == 'inc':
                for i in range(interval, len(self.time), interval):
                    self.increaseViscosity(change)
                    #print(f"Time: {self.time[i]}, Viskosität erhöht zu: {self.viscosity}")
                    return self.viscosity

            elif prop == 'dec':
                for i in range(interval, len(self.time), interval):
                    self.decreaseViscosity(change)
                    #print(f"Time: {self.time[i]}, Viskosität reduziert zu: {self.viscosity}")
                    return self.viscosity
        
        else:
            pass