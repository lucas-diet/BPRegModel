
import numpy as np
import matplotlib.pyplot as plt

from bloodPressure import *
from bodySystem import * 
from heart import *
from sensor import *
from liver import *


#########################
#### Init Parameter #####
#########################

radi = [20000, 4000, 20, 8, 20, 5000, 30000]   # in µm
viscosity = 50                                 # Wert zwischen 0 und 100
heartRate = 70
edv = 110                                      # Enddiastolische Volumen
esv = 60                                       # Endsystolisches Volumen
strokeVolume = edv - esv                       # Schlagvolumen
pres0 = 70                      
maxTime = 30

totalVolume = 70                              # in ml

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300]      # in mm

#### Extra Parameter für Liver ##### 
prop = 'inc'                                   # 'inc' zum erhöhen ; 'dec' zum verringern
interval = 100                                 # Zeitschritte, wo verändert wird
change = 0                                     # Wert um den verändert wird, wenn 0 dann keine Veränderung

##### Extra Parameter für BloodPressure #####
duration = maxTime      # Sekunden
systolic = 120          # TODO: soll noch simuliert werden mit Parametern
diastolic = 80          # TODO: soll noch simuliert werden mit Parametern
###########################

##### Extra Parameter für BodySystem #####
lims = [-17, 17]                            # Für den Achsenbereich, der angezeigt werden soll, wenn Radius der Gefäße geplottet wird.
lumFactor = [1, 1, 1, 1, 1, 1, 1]           # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren
###########################


##################
#### Klassen #####
##################

bp = BloodPressure(duration, heartRate, systolic, diastolic)
h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)
bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)
s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

h.heartSimulation()
bs.vesselSimulator(lens, nums, prop, interval, change)

isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava = bs.getPressurs()
isRV = h.bloodPressure_RV
isLV = h.bloodPressure_LV

isPres = [isRV, isLV, isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava]

s.presPrinter(isPres)
print('\n', '#####', 1)
bs.vpPlotter(lens, nums, prop, interval, change)

#### Soll Größen ####

soHR = [80, 100, 150, 180, 70, 10]
soRadi = []
soLumeFactor = []
soVis = [5, 90, 50, 55, 60, 10]
soStrokeVolume = []
soEDV = []
soESV = []
soTotalVolume = []
mt = []


#####################
for i in range(0, len(soHR)):
    soBP = BloodPressure(duration, soHR[i], systolic, diastolic)
    soH = Heart(radi, soVis[i], soHR[i], strokeVolume, edv, esv, pres0, totalVolume, maxTime)
    soBS = BodySystem(radi, lumFactor, soVis[i], soHR[i], strokeVolume, edv, esv, pres0, totalVolume, maxTime)
    soS = Sensor(radi, soVis[i], soHR[i], strokeVolume, edv, esv, pres0, maxTime)

    soH.heartSimulation()
    soBS.vesselSimulator(lens, nums, prop, interval, change)

    #### Regelstrecke ####

    soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava = soBS.getPressurs()
    soRV = soH.bloodPressure_RV
    soLV = soH.bloodPressure_LV
    soPres = [soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava]

    #soS.presPrinter(soPres)

    #### Regelabweichung ####

    rwRV = soRV - isRV
    rwLV = soLV - isLV
    rwAorta = soAorta - isAorta
    rwArterie = soArterie - isArterie
    rwArteriol = soArteriol - isArteriol
    rwCapillare = soCapillare - isCapillare
    rwVenole = soVenole - isVenole
    rwVene = soVene - isVene
    rwVCava = soVCava - isVCava

    rwPres = [rwRV, rwLV, rwAorta, rwArterie, rwArteriol, rwCapillare, rwVenole, rwVene, rwVCava]
    rwMins = [np.min(rwRV), np.min(rwLV), np.min(rwAorta), np.min(rwArterie), np.min(rwArteriol), np.min(rwCapillare), np.min(rwVenole), np.min(rwVene), np.min(rwVCava)]

    rwP = []

    for j in range(0, len(rwPres)):
        rwP.append(rwPres[j] - rwMins[j])

    s.presPrinter(rwP)
    print('\n', '#####', i+2)
    #s.ppPlotter(rwP[2::])
    plt.figure(figsize=(10, 6), num=f'Simulationsdurchlauf {i+2}')
    plt.title('Simulation des Gefäßsystem')
    plt.plot(bs.time, rwP[2])
    plt.plot(bs.time, rwP[3])
    plt.plot(bs.time, rwP[4])
    plt.plot(bs.time, rwP[5])
    plt.plot(bs.time, rwP[6])
    plt.plot(bs.time, rwP[7])
    plt.plot(bs.time, rwP[8])
    plt.grid(True)
    plt.show()

    isRV = rwRV
    isLV = rwLV
    isAorta = rwAorta
    isArterie = rwArterie
    isArteriol = rwArteriol
    isCapillare = rwCapillare
    isVenole = rwVenole
    isVene = rwVene
    isVCava = rwVCava

