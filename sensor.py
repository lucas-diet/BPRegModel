
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from heart import *

class Sensors():

    def __init__(self):
        pass

    def findPeak(self, data):
        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        return systolicPeaks, diastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])
        map = (meanSys + 2 * meanDia) / 3
        
        print(meanSys, meanDia)
        
        return map
            

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
vis = 1
heartRate = 70
strokeVolume = 70
maxElasticity = 2
edv = 130
esv = 100
maxTime = 5
dt = 0.01

h = Heart(radi, vis, heartRate, strokeVolume, edv, esv, maxTime, dt)
h.heartSimulation()

s = Sensors()
sys, _ = s.findPeak(h.bloodPressure_LV)
_, dia = s.findPeak(h.bloodPressure_LV)

plt.plot(h.time, h.bloodPressure_LV)
plt.plot(h.time[sys], h.bloodPressure_LV[sys], 'r.')
plt.plot(h.time[dia], h.bloodPressure_LV[dia], 'b.')

map = s.calculatePressure(h.bloodPressure_LV, sys, dia)
print(map)

plt.show()



