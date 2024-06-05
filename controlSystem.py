
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

##### Extra Parameter für BodySystem #####
lims = [-17, 17]                            # Für den Achsenbereich, der angezeigt werden soll, wenn Radius der Gefäße geplottet wird.
lumFactor = [1, 1, 1, 1, 1, 1, 1]           # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren
###########################


##################
#### Klassen #####
##################

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

soHR = [80, 100, 120, 150, 10]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]
soVis = [5, 90, 100, 50, 20]
#soStrokeVolume = []
soEDV = []
soESV = []
soTotalVolume = []
mt = []


#####################
for i in range(0, len(soHR)):
    soH = Heart(radi, soVis[i], soHR[i], strokeVolume, edv, esv, pres0, totalVolume, maxTime)
    soBS = BodySystem(radi, soLF[i], soVis[i], soHR[i], strokeVolume, edv, esv, pres0, totalVolume, maxTime)
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
    plt.figure(figsize=(11, 7), num=f'Simulationsdurchlauf {i+2}')
    plt.title('Simulation des Gefäßsystem')
    plt.plot(bs.time, rwP[2], label='Aorta Druck')
    plt.plot(bs.time, rwP[3], label='Arterie Druck')
    plt.plot(bs.time, rwP[4], label='Arteriole Druck')
    plt.plot(bs.time, rwP[5], label='Kapillare Druck')
    plt.plot(bs.time, rwP[6], label='Venole Druck')
    plt.plot(bs.time, rwP[7], label='Vene Druck')
    plt.plot(bs.time, rwP[8], label='V. Cava Druck')
    
    plt.xlabel('Zeit (s)')
    plt.ylabel('mmHg')
    plt.grid(True)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})
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