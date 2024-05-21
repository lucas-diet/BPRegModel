
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from heart import *
from bloodPressure import *

class Sensors():

    def findPeak(self, data):
        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        return systolicPeaks, diastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])
        map = meanDia + (1/3) * (meanSys - meanDia)

        return map
            

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
vis = 1
heartRate = 80
strokeVolume = 70
maxElasticity = 6
edv = 110
esv = 70
maxTime = 6
dt = 0.01

h = Heart(radi, vis, heartRate, strokeVolume, edv, esv, maxTime, dt)
h.heartSimulation()
h.aortaPresSim()

b = BloodPressure()
data = b.simulateBP()

s = Sensors()

plt.plot(h.time, h.bloodPressure_LV)
plt.plot(h.time, h.aortaPressure)
plt.plot(h.time, h.bloodPressure_RV)

##### Rechter Ventrikle #####
print()
print('Rechter Ventrikle')
print()

sysRV, _ = s.findPeak(h.bloodPressure_RV)
_, diaRV = s.findPeak(h.bloodPressure_RV)

mapRV = s.calculatePressure(h.bloodPressure_RV, sysRV, diaRV)
print('Systolischer Druck: ', np.mean(h.bloodPressure_RV[sysRV]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.bloodPressure_RV[diaRV]), 'mmHg')
print('Mittlerer Druck', mapRV, 'mmHg')

##### Linker Ventrikle #####
print()
print('Linker Ventrikle')
print()

sysLV, _ = s.findPeak(h.bloodPressure_LV)
_, diaLV = s.findPeak(h.bloodPressure_LV)

mapLV = s.calculatePressure(h.bloodPressure_LV, sysLV, diaLV)
print('Systolischer Druck: ', np.mean(h.bloodPressure_LV[sysLV]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.bloodPressure_LV[diaLV]), 'mmHg')
print('Mittlerer Druck', mapLV, 'mmHg')

##### Aorta #####
print()
print('Aorta')
print()
sysA, _ = s.findPeak(h.aortaPressure)
_, diaA = s.findPeak(h.aortaPressure)

mapA = s.calculatePressure(h.aortaPressure, sysA, diaA)
print('Systolischer Druck: ', np.mean(h.aortaPressure[sysA]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.aortaPressure[diaA]), 'mmHg')
print('Mittlerer Druck', mapA, 'mmHg')

plt.plot(h.time[sysLV], h.bloodPressure_LV[sysLV], 'r.')
plt.plot(h.time[diaLV], h.bloodPressure_LV[diaLV], 'b.')
plt.grid(True)

plt.show()