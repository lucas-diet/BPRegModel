
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
heartRate = 70
strokeVolume = 70
maxElasticity = 6
edv = 110
esv = 70
pres0 = 70
maxTime = 10
dt = 0.01

h = Heart(radi, vis, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)
h.heartSimulation()
h.aortaPresSim()
h.arteriePresSim()
h.arteriolePresSim()
h.capillarePresSim()

b = BloodPressure()
data = b.simulateBP()

s = Sensors()

plt.plot(h.time, h.bloodPressure_RV)
plt.plot(h.time, h.bloodPressure_LV)
plt.plot(h.time, h.aortaPressure)
plt.plot(h.time, h.arteriePressure)
plt.plot(h.time, h.arteriolPressure)
plt.plot(h.time, h.capillarePressure)


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

##### Arterien #####
print()
print('Arterien')
print()

sysAr, _ = s.findPeak(h.arteriePressure)
_, diaAr = s.findPeak(h.arteriePressure)

mapAr = s.calculatePressure(h.arteriePressure, sysAr, diaAr)
print('Systolischer Druck: ', np.mean(h.arteriePressure[sysAr]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.arteriePressure[diaAr]), 'mmHg')
print('Mittlerer Druck', mapAr, 'mmHg')

##### Arteriole #####
print()
print('Arteriole')
print()

sysArt, _ = s.findPeak(h.arteriolPressure)
_, diaArt = s.findPeak(h.arteriolPressure)

mapArt = s.calculatePressure(h.arteriolPressure, sysArt, diaArt)
print('Systolischer Druck: ', np.mean(h.arteriolPressure[sysArt]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.arteriolPressure[diaArt]), 'mmHg')
print('Mittlerer Druck', mapArt, 'mmHg')

##### Arteriole #####
print()
print('Kapillare')
print()

sysC, _ = s.findPeak(h.capillarePressure)
_, diaC = s.findPeak(h.capillarePressure)

mapC = s.calculatePressure(h.capillarePressure, sysC, diaC)
print('Systolischer Druck: ', np.mean(h.capillarePressure[sysC]), 'mmHg')
print('Diastolischer Druck: ', np.mean(h.capillarePressure[diaC]), 'mmHg')
print('Mittlerer Druck', mapC, 'mmHg')

##### Peaks #####
plt.plot(h.time[sysLV], h.bloodPressure_LV[sysLV], 'r.')
plt.plot(h.time[diaLV], h.bloodPressure_LV[diaLV], 'b.')

plt.plot(h.time[sysRV], h.bloodPressure_RV[sysRV], 'r.')
plt.plot(h.time[diaRV], h.bloodPressure_RV[diaRV], 'b.')

plt.plot(h.time[sysA], h.aortaPressure[sysA], 'r.')
plt.plot(h.time[diaA], h.aortaPressure[diaA], 'b.')

plt.plot(h.time[sysAr], h.arteriePressure[sysAr], 'r.')
plt.plot(h.time[diaAr], h.arteriePressure[diaAr], 'b.')

plt.plot(h.time[sysArt], h.arteriolPressure[sysArt], 'r.')
plt.plot(h.time[diaArt], h.arteriolPressure[diaArt], 'b.')

plt.plot(h.time[sysC], h.capillarePressure[sysC], 'r.')
plt.plot(h.time[diaC], h.capillarePressure[diaC], 'b.')

plt.grid(True)
plt.show()