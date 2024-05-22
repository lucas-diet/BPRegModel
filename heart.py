
import numpy as np
import matplotlib.pyplot as plt

from bodySystem import BodySystem
from bloodPressure import BloodPressure

class Heart():

    def __init__(self, radi, vis, heartRate=10, strokeVolume=70, edv=120, esv=50, pres0=70, maxTime=10, dt=0.01,):
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume
        self.dt = dt
        #self.maxElasticity = maxElasticity
        self.edv = edv
        self.esv = esv
        self.pres0 = pres0
        self.maxTime = maxTime
        self.radi = radi
        self.vis = vis
        self.viscocity = BodySystem(radi, vis)

        self.time = np.arange(0, self.maxTime, dt)
        
        self.bloodPressure_RV = np.zeros_like(self.time)
        self.bloodVolume_RV = np.zeros_like(self.time)

        self.bloodPressure_LV = np.zeros_like(self.time)
        self.bloodVolume_LV = np.zeros_like(self.time)

        self.aortaPressure = np.zeros_like(self.time)
        self.arteriePressure = np.zeros_like(self.time)
        self.arteriolPressure = np.zeros_like(self.time)
        self.capillarePressure = np.zeros_like(self.time)

    def checkSlope(self, i1, i2):
        if i1 > i2:
            return True
        return False
    
    def findIndex(self, arr, val):
        idx = None
        for i in range(0, len(arr)):
            if arr[i] == val:
                idx = i
                break
        return idx
    
    def normalize(self, data):
        max_bp = np.max(data)
        min_bp = np.min(data)
		
        normalized_bp = (data - min_bp) / (max_bp - min_bp)  # Auf [0, 1] normalisieren
        normalized_bp = normalized_bp * (self.esv - self.edv) + self.edv  # Skalieren auf [diastolic, systolic]
    
    def rightVentricle(self, shift):
        for i in range(0,len(self.time)):
            t = self.time[i]
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * (t - shift) / 60)

            p1 = np.sin(2 * np.pi * (self.heartRate / 60) * t)
            p2 = 0.63 * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))
            
            if i == 0:
                self.bloodVolume_RV[i] = self.edv
            else:
                dVdt = self.strokeVolume - elasticity * (self.bloodVolume_RV[i-1] - self.esv)
                self.bloodVolume_RV[i] = self.bloodVolume_RV[i-1] + dVdt * self.dt
            
            self.bloodPressure_RV[i] = elasticity * (self.bloodVolume_RV[i] - self.esv) * 0.15 + 3 * (p1 + p2) # ist noch keine schöne Lösung!!

    def leftVentricle(self, shift=0):
        for i in range(0, len(self.time)):
            t = self.time[i]
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * (t - shift) / 60)
            
            if i == 0:
                self.bloodVolume_LV[i] = self.edv

            else:
                dVdt = self.strokeVolume - elasticity * (self.bloodVolume_LV[i-1] - self.esv)
                self.bloodVolume_LV[i] = self.bloodVolume_LV[i-1] + dVdt * self.dt
            
            self.bloodPressure_LV[i] = elasticity * (self.bloodVolume_LV[i] - self.esv) + 5
    
    def aortaPresSim(self):
        for i in range(0, len(self.time)):
            t = self.time[i]

            p1 = np.sin(2 * np.pi * (self.heartRate / 60) * t)
            p2 = 0.63 * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))
            
            self.aortaPressure[i] = self.pres0

            if self.bloodPressure_LV[i] > self.aortaPressure[i]:
                self.aortaPressure[i] = self.bloodPressure_LV[i]

            else:
                idx = self.findIndex(self.time, self.time[i-1])

                if self.aortaPressure[idx] > self.pres0:
                    self.aortaPressure[i] += 20 * (p1 + p2)

    def arteriePresSim(self):
        for i in range(0, len(self.time)):
            t = self.time[i]

            p1 = np.sin(2 * np.pi * (self.heartRate / 60) * t)
            p2 = 0.63 * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))

            self.arteriePressure[i] = self.pres0 - 3

            if self.aortaPressure[i] > self.arteriePressure[i]:
                self.arteriePressure[i] = self.aortaPressure[i] - 3

            else:
                idx = self.findIndex(self.time, self.time[i-1])

                if self.arteriePressure[idx] > self.pres0 - 3:
                    self.arteriePressure[i] += 20 * (p1 + p2)

    def arteriolePresSim(self):
        for i in range(0, len(self.time)):
            t = self.time[i]

            p1 = np.sin(2 * np.pi * (self.heartRate / 60) * t)
            p2 = 0.63 * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))

            self.arteriolPressure[i] = self.pres0 - 6

            if self.arteriePressure[i] > self.arteriolPressure[i]:
                self.arteriolPressure[i] = self.arteriePressure[i] - 6

            else:
                idx = self.findIndex(self.time, self.time[i-1])

                if self.arteriolPressure[idx] > self.pres0 - 6:
                    self.arteriolPressure[i] += 20 * (p1 + p2)

    def capillarePresSim(self):
        for i in range(0, len(self.time)):
            t = self.time[i]

            p1 = np.sin(2 * np.pi * (self.heartRate / 60) * t)
            p2 = 0.63 * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))

            self.capillarePressure[i] = self.pres0 - 45

            if self.capillarePressure[i] > self.arteriolPressure[i]:
                self.arteriolPressure[i] = self.capillarePressure[i] - 45

            else:
                idx = self.findIndex(self.time, self.time[i-1])

                if self.arteriolPressure[idx] > self.pres0 - 45:
                    self.capillarePressure[i] += 20 * (p1 + p2) * 0.6

    
    def heartSimulation(self):
        self.rightVentricle(shift=-0.5)
        self.leftVentricle()

    
    def plotter(self):
        plt.figure(figsize=(10, 6))
        
        self.heartSimulation()
        self.aortaPresSim()
        self.arteriePresSim()
        self.arteriolePresSim()
        self.capillarePresSim()

        plt.plot(self.time, self.bloodPressure_RV, label='Rechter Ventrikel Druck (mmHg)')
        #plt.plot(self.time, self.bloodVolume_RV, label='Rechter Ventrikel Volumen')

        plt.plot(self.time, self.bloodPressure_LV, label='Linkes Ventrikel Druck (mmHg)')
        plt.plot(self.time, self.bloodVolume_LV, label='Linkes Ventrikel Volumen')
        
        plt.plot(self.time, self.aortaPressure, label='Aorta Druck (mmHg)')
        plt.plot(self.time, self.arteriePressure, label='Arterie Druck (mmHg)')
        plt.plot(self.time, self.arteriolPressure, label='Arteriole Druck (mmHg)')
        plt.plot(self.time, self.capillarePressure, label='Kapilare Druck (mmHg)')
        
        #plt.plot(self.time, [70 for _ in range(0,len(self.time))])
        plt.xlabel('Zeit (s)')
        plt.ylabel('Werte')
        plt.title('Simulation des linken Ventrikels')
        plt.grid(True)
        plt.legend()

        plt.show()


radi = [20000, 4000, 20, 8, 20, 5000, 30000]
vis = 1
heartRate = 70
strokeVolume = 70
maxElasticity = 2
edv = 110
esv = 50
pres0 = 70
maxTime = 5
dt = 0.01

h = Heart(radi, vis, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)

h.plotter()
""""""
