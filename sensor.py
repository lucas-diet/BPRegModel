
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from bloodPressure import *
from heart import *
from bodySystem import *


class Sensor():

    def __init__(self, radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt=0.01):
        self.radi = radi
        self.viscocity = viscocity
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume 
        self.edv = edv 
        self.esv = esv 
        self.pres0 = pres0 
        self.maxTime = maxTime
        self.dt = dt
        self.time = np.arange(0, maxTime, dt)

    def findPeak(self, data):
        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        return systolicPeaks, diastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])

        map = meanDia + (1/3) * (meanSys - meanDia)
        return map
    
    def presPlotter(self, data):
        #data = [data1, data2, data3, data4, data5, data6, data7]

        for d in data:
            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)

            plt.plot(self.time, d)

            plt.plot(self.time[sys], d[sys], 'r.')
            plt.plot(self.time[dia], d[dia], 'b.')

        plt.grid(True)
        plt.show()
    
    def presPrinter(self, data, types):
        type = iter(types)

        for d in data:
            print('\n', '#####  ', next(type) , '  #####', '\n')

            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)

            map = self.calculatePressure(d, sys, dia)
            print('Systolischer Druck: ', np.mean(d[sys]), 'mmHg')
            print('Diastolischer Druck: ', np.mean(d[dia]), 'mmHg')
            print('Mittlerer Druck', map, 'mmHg')

            
'''
radi = [20000, 4000, 20, 8, 20, 5000, 30000]
viscocity = 1
heartRate = 70
strokeVolume = 70
maxElasticity = 6
edv = 110
esv = 70
pres0 = 70
maxTime = 10
dt = 0.01

h = Heart(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)
h.heartSimulation()

bs = BodySystem(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime)
bs.vesselSimulator()

plt.plot(h.time, h.bloodPressure_RV)
plt.plot(h.time, h.bloodPressure_LV)
plt.plot(h.time, bs.aortaPressure)
plt.plot(h.time, bs.arteriePressure)
plt.plot(h.time, bs.arteriolPressure)
plt.plot(h.time, bs.capillarePressure)
plt.plot(h.time, bs.venolePressure)
plt.plot(h.time, bs.venePressure)
plt.plot(h.time, bs.vCavaPressure)

s = Sensor(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime)
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
types = ['Rechter Ventrikel', 'Linker Ventrikel', 'Aorta', 'Arterie', 'Arteriole', 'Kapillare', 'Venole', 'Vene', 'V. Cava']
s.presPrinter(dataC, types)

data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
#s.presPlotter(data)
'''