
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
maxTime = 10

totalVolume = 70                              # in ml

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300]      # in mm

#### Extra Parameter für Liver ##### 
prop = 'inc'                                   # 'inc' zum erhöhen ; 'dec' zum verringern
interval = 100                                 # Zeitschritte, wo verändert wird
change = 0                                     # Wert um den verändert wird, wenn 0 dann keine Veränderung

##### Extra Parameter für BodySystem #####
lims = [-17, 17]                            # Für den Achsenbereich, der angezeigt werden soll, wenn Radius der Gefäße geplottet wird.
lumFactor = [1, 1, 1, 1, 1, 1, 1]           # array, um den inneren Radius anpassen zu können
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

#s.presPrinter(isPres)
bs.vpPlotter(lens, nums, prop, interval, change)

#### Soll Größen ####

soHR =  [(2, 10), 
         (8, 70)]
soLF =  [(2, [1, 1, 1, 1, 1, 1, 1]), 
         (8, [1, 1, 1, 1, 1, 1, 1])]
soVis = [(2, 10), 
         (8, 50)]
# soStrokeVolume = []
# soEDV = []
# soESV = []
# soTotalVolume = []

time_intervals = sorted(set([t for t, _ in soHR + soLF + soVis]))

#rwRV, rwLV, rwAorta, rwArterie, rwArteriol, rwCapillare, rwVenole, rwVene, rwVCava = [], [], [], [], [], [], [], [], []

for current_time in time_intervals:
    for t, newHR in soHR:
        if t == current_time:
            heartRate = newHR
    for t, newLF in soLF:
        if t == current_time:
            lumFactor = newLF
    for t, newVis in soVis:
        if t == current_time:
            viscosity = newVis

    h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)
    bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)
    s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)
    
    h.heartSimulation()
    bs.vesselSimulator(lens, nums, prop, interval, change)
    
    soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava = bs.getPressurs()
    soRV = h.bloodPressure_RV
    soLV = h.bloodPressure_LV
    soPres = [soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava]

    if all(soRV[k] != isRV[k] and soLV[k] != isLV[k] and soAorta[k] != isAorta[k] and soArteriol[k] != isArteriol[k] and soCapillare[k] != isCapillare[k] and soVenole[k] != isVenole[k] and soVene[k] != isVene[k] and soVCava[k] != isVCava[k] for k in range(len(soRV))):
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

    rwP = [rwPres[j] - rwMins[j] for j in range(len(rwPres))]

    plt.figure(figsize=(11, 7), num=f'Simulationsdurchlauf {current_time}')
    plt.title(f'Simulation des Gefäßsystem bei Zeit {current_time}s; Herzfrequenz: {heartRate}')
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

    isRV, isLV, isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava = soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava
