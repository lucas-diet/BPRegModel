

from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *
from liver import *
from controlSystem import * 

#############################
#### Initiale Parameter #####
#############################

radi = [20000, 4000, 20, 8, 20, 5000, 30000]   # in µm
viscosity = 5                                # Wert zwischen 0 und 100
heartRate = 70
edv = 110                                      # Enddiastolische Volumen
esv = 60                                       # Endsystolisches Volumen
strokeVolume = edv - esv                       # Schlagvolumen                     
maxTime = 100

totalVolume = 70                              # in ml

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300]      # in mm

##### Extra Parameter für BodySystem #####
lims = [-17, 17]                            # Für den Achsenbereich, der angezeigt werden soll, wenn Radius der Gefäße geplottet wird.
lumFactor = [1, 1, 1, 1, 1, 1, 1]           # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren
##########################################

###############################
#### Dynamische Parameter #####
###############################

ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV = [], [], [], [], [], [], [], [], [], [], [], []

# Herzfrequenz
#ctHR = [2, 4, 60]
#newHR = [40, 90, 170]

# Viskosität
#ctVis = [2, 4, 6]
#newVis = [10, 50, 100]

# Radius
#ctRadius = [2, 4, 6]
#newRadius = [0.1, 0.1, 0.1]

# Gesamtvolumen
#ctVol = [2, 4, 6]
#newVol = [100, 200, 300]

############
# Folgende Parameter müssen alle aktiv oder inaktiv sein 
############

# Enddiastolsiches Volumen
#ctEDV = [2, 4, 6] 
#newEDV = [100, 200, 100]

# Endsystolisches Volumen
#ctESV = [2, 4, 6]
#newESV = [20, 40, 50]

#####################
##### Blutdruck ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
#####################

duration = maxTime      # Sekunden
systolic = 120
diastolic = 80       

## Klasse ##
bpSim = BloodPressure(duration, heartRate, systolic, diastolic)

#bpSim.bpPlotter()      # Ausführbare Funktion

###############
#### Herz #####
###############

## Klasse ##
h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, totalVolume, maxTime)

#h.hpPlotter(ctEDV, newEDV, ctESV, newESV)          # Ausführbare Funktion

########################
##### Körpersystem #####
########################

## Klasse ##
bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, totalVolume, maxTime)

#bs.vesselPlotter(lumFactor, lims)                  # Ausführbare Funktion
#bs.resisPrinter(lens, nums)                        # Ausführbare Funktion
#bs.vpPlotter(lens, nums, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV)    # Ausführbare Funktion

##################
##### Sensor #####
##################

##### Extra Parameter ##### (Sind fest und sollten nicht verändert werden!)
data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
###########################

## Klasse ##
s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, maxTime)

h.heartSimulation(ctEDV, newEDV, ctESV, newESV)
bs.vesselSimulator(lens, nums, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)

#s.ppPlotter(data)                                  # Ausführbare Funktion
#s.presPrinter(dataC)                                # Ausführbare Funktion

### Findet den Blutdruck zu einem bestimmten Zeitpunkt ###
presData = data[0]                              # data[x] x = {0,1,2,3,4,5,6}
timeStemp = 1

#s.printPressureTimePoint(presData, timeStemp)          # Ausführbare Funktion

######################
##### Regelkreis #####
######################

soHR = [71, 72, 73]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]
soVis = [50, 50, 50]
soTV = [70, 70, 70]
soEDV = [110, 110, 110]
soESV = [60, 60, 60]
apply = 3
currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV, ctEDV, newEDV, ctESV, newESV]

sys = Regelkreis(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, totalVolume, maxTime)

#sys.controlSystem(currVals, soHR, soLF, soVis, soTV, soEDV, soESV, apply, lens, nums)