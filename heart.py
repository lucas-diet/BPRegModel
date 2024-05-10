
import numpy as np
from bodySystem import BodySystem as bp
import matplotlib.pyplot as plt

class Heart():

    def __init__(self, heartRate=10, strokeVolume=70, maxElasticity=2, edv=120, esv=50, maxTime=10, dt=0.01):
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume
        self.dt = dt
        self.maxElasticity = maxElasticity
        self.edv = edv
        self.esv = esv
        self.maxTime = maxTime
        
        self.time = np.arange(0, self.maxTime, dt)
        self.bloodVolume = np.zeros_like(self.time)
        self.bloodPressure = np.zeros_like(self.time)
        self.aortaPressure = np.zeros_like(self.time)
    
    def ventricleSimulation(self):
        for i in range(0,len(self.time)):
            t = self.time[i]
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * t / 60)
            
            if i == 0:
                self.bloodVolume[i] = self.edv

            else:
                dVdt = self.strokeVolume - elasticity * (self.bloodVolume[i-1] - self.esv)
                self.bloodVolume[i] = self.bloodVolume[i-1] + dVdt * self.dt
                
            self.bloodPressure[i] = elasticity * (self.bloodVolume[i] - self.esv)   
            


    def plotter(self):
        plt.figure(figsize=(10, 6))
		
		# Plot für den linken Ventrikel
        #plt.subplot(2, 1, 1)
        plt.plot(self.time, self.bloodVolume, label='Linkes Ventrikel Volumen (ml)', color='blue')
        plt.plot(self.time, self.bloodPressure, label='Linkes Ventrikel Druck (mmHg)', color='red')
        plt.plot(self.time, [80 for _ in range(0,len(self.time))]) 
        plt.xlabel('Zeit (s)')
        plt.ylabel('Werte')
        plt.title('Simulation des linken Ventrikels')
        plt.grid(True)
        plt.legend()

        plt.show()



heartRate = 20
strokeVolume = 80
maxElasticity = 2
edv = 110
esv = 50
maxTime = 10
dt = 0.01

h = Heart(heartRate, strokeVolume, maxElasticity, edv, esv, maxTime, dt)
h.ventricleSimulation()
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
