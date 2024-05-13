
import numpy as np
from bodySystem import BodySystem
import matplotlib.pyplot as plt

class Heart():

    def __init__(self, radi, vis, heartRate=10, strokeVolume=70, maxElasticity=2, edv=120, esv=50, maxTime=10, dt=0.01,):
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume
        self.dt = dt
        self.maxElasticity = maxElasticity
        self.edv = edv
        self.esv = esv
        self.maxTime = maxTime
        self.radi = radi
        self.vis = vis
        self.viscocity = BodySystem(radi, vis)

        
        self.time = np.arange(0, self.maxTime, dt)
        self.bloodVolume = np.zeros_like(self.time)
        self.bloodPressure = np.zeros_like(self.time)
        self.aortaPressure = np.zeros_like(self.time)

    def checkSlope(self, i1, i2):
        if i1 > i2:
            return True
        return False

    def ventricleSimulation(self, vis, l, r):
        for i in range(0,len(self.time)):
            t = self.time[i]
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * t / 60)
            bs = BodySystem(self.radi, self.vis)
            
            if i == 0:
                self.bloodVolume[i] = self.edv
            else:
                dVdt = self.strokeVolume - elasticity * (self.bloodVolume[i-1] - self.esv)
                self.bloodVolume[i] = self.bloodVolume[i-1] + dVdt * self.dt
            
            self.bloodPressure[i] = elasticity * (self.bloodVolume[i] - self.esv)

            p1 = 120 * np.sin(2 * np.pi * (heartRate / 60) * t)
            p2 = 0.63 * 120 * np.sin(4 * np.pi * (heartRate / 60) * t + (2 / np.pi))
            self.aortaPressure[i] = self.strokeVolume
            
            if self.bloodPressure[i] > self.aortaPressure[i]:
                self.aortaPressure[i] = self.bloodPressure[i]

            
            elif i > 0 and self.bloodPressure[i] != self.aortaPressure[i] and self.checkSlope(self.bloodPressure[i-1], self.bloodPressure[i]) == True:
                for j in range(i, min(i+50, len(self.time))):
                    print(j)
                    p0 = self.aortaPressure[i-1]
                    self.aortaPressure[j] = self.strokeVolume + 1#
                    i += 1

                    
                    
                
                    
                
            
            


    def plotter(self):
        plt.figure(figsize=(10, 6))
		
		# Plot für den linken Ventrikel
        #plt.subplot(2, 1, 1)
        plt.plot(self.time, self.bloodVolume, label='Linkes Ventrikel Volumen (ml)', color='blue')
        plt.plot(self.time, self.bloodPressure, label='Linkes Ventrikel Druck (mmHg)', color='red')
        plt.plot(self.time, self.aortaPressure)
        #plt.plot(self.time, [100 for _ in range(0,len(self.time))])
        plt.xlabel('Zeit (s)')
        plt.ylabel('Werte')
        plt.title('Simulation des linken Ventrikels')
        plt.grid(True)
        plt.legend()

        plt.show()


radi = [20000, 4000, 20, 8, 20, 5000, 30000]
vis = 1
heartRate = 20
strokeVolume = 100
maxElasticity = 2
edv = 110
esv = 50
maxTime = 10
dt = 0.01

h = Heart(radi, vis, heartRate, strokeVolume, maxElasticity, edv, esv, maxTime, dt)
h.ventricleSimulation(1, 200, 20000)
h.plotter()
"""
for i in range(0, len(self.time)):
            t = self.time[i]
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * t / 60)
        
            if i == 0:
                self.bloodVolume[i] = self.edv
            
            else:
                dVdt = self.strokeVolume - elasticity * (self.bloodVolume[i-1] - self.esv)
                self.bloodVolume[i] = self.bloodVolume[i-1] + dVdt * self.dt
            
            self.bloodPressure[i] = elasticity * (self.bloodVolume[i] - self.esv)        
"""
