
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from bloodPressure import *
from heart import *
from bodySystem import *


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

bs = BodySystem(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime)


bs.aortaPresSim()
bs.arteriePresSim()
bs.arteriolePresSim()
bs.capillarePresSim()
bs.venolePresSim()
bs.venePresSim()
bs.vCavaPresSim()

#b = BloodPressure()
#data = b.simulateBP()

plt.plot(h.time, h.bloodPressure_RV)
plt.plot(h.time, h.bloodPressure_LV)
plt.plot(h.time, bs.aortaPressure)
plt.plot(h.time, bs.arteriePressure)
plt.plot(h.time, bs.arteriolPressure)
plt.plot(h.time, bs.capillarePressure)
plt.plot(h.time, bs.venolePressure)
plt.plot(h.time, bs.venePressure)
plt.plot(h.time, bs.vCavaPressure)

s = Sensors()

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

sysA, _ = s.findPeak(bs.aortaPressure)
_, diaA = s.findPeak(bs.aortaPressure)

mapA = s.calculatePressure(bs.aortaPressure, sysA, diaA)
print('Systolischer Druck: ', np.mean(bs.aortaPressure[sysA]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.aortaPressure[diaA]), 'mmHg')
print('Mittlerer Druck', mapA, 'mmHg')

##### Arterien #####
print()
print('Arterien')
print()

sysAr, _ = s.findPeak(bs.arteriePressure)
_, diaAr = s.findPeak(bs.arteriePressure)

mapAr = s.calculatePressure(bs.arteriePressure, sysAr, diaAr)
print('Systolischer Druck: ', np.mean(bs.arteriePressure[sysAr]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.arteriePressure[diaAr]), 'mmHg')
print('Mittlerer Druck', mapAr, 'mmHg')

##### Arteriole #####
print()
print('Arteriole')
print()

sysArt, _ = s.findPeak(bs.arteriolPressure)
_, diaArt = s.findPeak(bs.arteriolPressure)

mapArt = s.calculatePressure(bs.arteriolPressure, sysArt, diaArt)
print('Systolischer Druck: ', np.mean(bs.arteriolPressure[sysArt]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.arteriolPressure[diaArt]), 'mmHg')
print('Mittlerer Druck', mapArt, 'mmHg')

##### Arteriole #####
print()
print('Kapillare')
print()

sysC, _ = s.findPeak(bs.capillarePressure)
_, diaC = s.findPeak(bs.capillarePressure)

mapC = s.calculatePressure(bs.capillarePressure, sysC, diaC)
print('Systolischer Druck: ', np.mean(bs.capillarePressure[sysC]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.capillarePressure[diaC]), 'mmHg')
print('Mittlerer Druck', mapC, 'mmHg')

##### Venole #####
print()
print('Venole')
print()

sysV, _ = s.findPeak(bs.venolePressure)
_, diaV = s.findPeak(bs.venolePressure)

mapV = s.calculatePressure(bs.venolePressure, sysV, diaV)
print('Systolischer Druck: ', np.mean(bs.venolePressure[sysV]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.venolePressure[diaV]), 'mmHg')
print('Mittlerer Druck', mapV, 'mmHg')

##### Vene #####
print()
print('Vene')
print()

sysVe, _ = s.findPeak(bs.venePressure)
_, diaVe = s.findPeak(bs.venePressure)

mapVe = s.calculatePressure(bs.venePressure, sysVe, diaVe)
print('Systolischer Druck: ', np.mean(bs.venePressure[sysVe]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.venePressure[diaVe]), 'mmHg')
print('Mittlerer Druck', mapVe, 'mmHg')

##### V. Cava #####
print()
print('V. Cava')
print()

sysVC, _ = s.findPeak(bs.vCavaPressure)
_, diaVC = s.findPeak(bs.vCavaPressure)

mapVC = s.calculatePressure(bs.vCavaPressure, sysVC, diaVC)
print('Systolischer Druck: ', np.mean(bs.vCavaPressure[sysVC]), 'mmHg')
print('Diastolischer Druck: ', np.mean(bs.vCavaPressure[diaVC]), 'mmHg')
print('Mittlerer Druck', mapVC, 'mmHg')

##### Peaks #####
plt.plot(h.time[sysLV], h.bloodPressure_LV[sysLV], 'r.')
plt.plot(h.time[diaLV], h.bloodPressure_LV[diaLV], 'b.')

plt.plot(h.time[sysRV], h.bloodPressure_RV[sysRV], 'r.')
plt.plot(h.time[diaRV], h.bloodPressure_RV[diaRV], 'b.')

plt.plot(h.time[sysA], bs.aortaPressure[sysA], 'r.')
plt.plot(h.time[diaA], bs.aortaPressure[diaA], 'b.')

plt.plot(h.time[sysAr], bs.arteriePressure[sysAr], 'r.')
plt.plot(h.time[diaAr], bs.arteriePressure[diaAr], 'b.')

plt.plot(h.time[sysArt], bs.arteriolPressure[sysArt], 'r.')
plt.plot(h.time[diaArt], bs.arteriolPressure[diaArt], 'b.')

plt.plot(h.time[sysC], bs.capillarePressure[sysC], 'r.')
plt.plot(h.time[diaC], bs.capillarePressure[diaC], 'b.')

plt.plot(h.time[sysV], bs.venolePressure[sysV], 'r.')
plt.plot(h.time[diaV], bs.venolePressure[diaV], 'b.')

plt.plot(h.time[sysVe], bs.venePressure[sysVe], 'r.')
plt.plot(h.time[diaVe], bs.venePressure[diaVe], 'b.')

plt.plot(h.time[sysVC], bs.vCavaPressure[sysVC], 'r.')
plt.plot(h.time[diaVC], bs.vCavaPressure[diaVC], 'b.')

plt.grid(True)
plt.show()