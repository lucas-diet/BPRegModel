
from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *
from liver import *
from controlSystem import * 

#############################
#### Initiale Parameter #####
#############################

radi = [20000, 4000, 20, 8, 20, 5000, 30000]    # in µm

viscosity = 50                                  # Wert zwischen 0 und 100
heartRate = 60
edv = 70                                        # Enddiastolische Volumen
esv = 20                                        # Endsystolisches Volumen
strokeVolume = edv - esv                        # Schlagvolumen                     
maxTime = 30                                    # in Sekunden

# Stress: 30s
# Schock: 60s
# Verengung: 300s
# Niere: 60s

totalVolume = 5000                               # in ml

nums = [1, 2, 4, 16, 4, 2, 1]                   # Anzhale der Gefäße
lens = [200, 150, 100, 50, 100, 150, 300]       # in mm :: Längen der Gefäße

##### Extra Parameter für BodySystem #####
lims = [-17, 17]                                # Achsenlänge; Radienplot
lumFactor = [1, 1, 1, 1, 1, 1, 1]               # Faktor zum skalieren von Radien
##########################################

###############################
#### Dynamische Parameter #####
###############################

ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV = [], [], [], [], [], [], [], [], [], [], [], []

# Herzfrequenz
#ctHR = [2, 4, 6, 9]; newHR = [40, 90, 80, 50]

# Stress: 
ctHR = [5, 10, 20, 25]; newHR = [50, 54, 50, 51]
# Schock: 
#ctHR = [2, 7, 20, 45]; newHR = [50, 57, 60, 51]
# Verengung:
#ctHR = [1, 140, 210, 280]; newHR = [60, 67, 60, 60]
# Niere
#ctHR = [2, 15, 20, 40]; newHR = [60, 57, 66, 61]

# Viskosität
#ctVis = [5, 15, 20, 25]; newVis = [50, 60, 55, 50]

# Stress: 
ctVis = [5, 10, 20, 25]; newVis = [30, 35, 30, 30]
# Schock: 
#ctVis = [2, 32, 40, 50]; newVis = [50, 55, 50, 50]
# Verengung:
#ctVis = [70, 140, 210, 280]; newVis = [50, 50, 50, 50]
# Niere
#ctVis = [2, 15, 20, 40]; newVis = [50, 60, 55, 50]

# Radius
#ctRadius = [2, 5, 7, 18]; newRadius = [0.9, 0.6, 0.4, 0.1]

# Gesamtvolumen
#ctVol = [3, 5, 7, 8]; newVol = [5050, 6200, 7450, 5000]

#Niere:
#ctVol = [3, 5, 7, 8]; newVol = [5000, 5000, 5000, 5000]

############
# Folgende Parameter müssen alle aktiv oder inaktiv sein 
############

# Enddiastolsiches Volumen
#ctEDV = [5, 15, 20, 25]; newEDV = [50, 70, 70, 60]

# Stress: 
ctEDV = [5, 10, 20, 25]; newEDV = [70, 70, 70, 70]
# Schock: 
#ctEDV = [2, 32, 40, 50]; newEDV = [110, 120, 125, 110]
# Niere:
#ctEDV = [2, 15, 20, 40]; newEDV = [70, 75, 70, 70]

# Endsystolisches Volumen
#ctESV = [5, 15, 20, 25]; newESV = [60, 30, 45, 60]

# Stress: 
ctESV = [5, 10, 20, 25]; newESV = [30, 25, 25, 30]
# Schock: 
#ctESV = [2, 32, 40, 50]; newESV = [60, 50, 55, 60]
# Niere:
#ctESV = [2, 15, 20, 40]; newESV = [20, 20, 25, 25]

#####################
##### Blutdruck ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
#####################

duration = maxTime      # in Sekunden
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

##### Extra 'Parameter' ##### (Sind fest und sollten nicht verändert werden!)
data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]

#(Nicht verändern!) -> Simulieren das Herz und die Gefäße indem sie alle wichtigen Funktionen verwenden.
h.heartSimulation(ctEDV, newEDV, ctESV, newESV)
bs.vesselSimulator(lens, nums, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
#############################

## Klasse ##
s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, maxTime)

#s.ppPlotter(data)                                      # Ausführbare Funktion
s.presPrinter(dataC)                                   # Ausführbare Funktion

# Extra Parameter -> Können angepasst werden#
# Findet den Blutdruck zu einem bestimmten Zeitpunkt #
presData = data[0]                                      # data[x] x = {0,1,2,3,4,5,6}
timeStemp = 1
#s.printPressureTimePoint(presData, timeStemp)          # Ausführbare Funktion

######################
##### Regelkreis #####
######################

#### Soll Parameter #####

'''
soHR = [90, 147, 79, 60]
soVis = [50, 55, 50, 50]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]
soTV = [5000, 5000, 5000, 5000]
soEDV = [110, 120, 125, 110]
soESV = [60, 50, 55, 60]
apply = 4
ctSim = [2, 5, 7, 9]
'''
### Simulationsstudien - Parameter ###

# Kurzzeitiger Stress

soHR = [70, 160, 100, 80]
soVis = [50, 65, 60, 60]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [1, 1, 1, 1, 1, 1, 1]]
soTV = [5000, 7000, 6000, 5000]
soEDV = [130, 130, 130, 130]
soESV = [40, 40, 40, 40]
apply = 4
ctSim = [5, 10, 20, 25]
''''''

# Schocksituation
'''
soHR = [50, 80, 90, 100]
soVis = [75, 75, 75 ,75]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]
soTV = [5000, 4500, 4000, 3500]
soEDV = [100, 100, 100, 100]
soESV = [60, 71, 72, 73]
apply = 4
ctSim = [10, 20, 30, 35]
'''

# Verengen der Blutgefäße
'''
soHR = [60, 50, 55, 62]
soVis = [75, 75, 75, 75]
soLF = [[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
        [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]
soTV = [5000, 5000, 5000, 5000]
soEDV = [110, 110, 110, 110]
soESV = [50, 50, 50, 50]
apply = 4
ctSim = [40, 140, 210, 280]
'''

# Niereninsuffizienz
'''
soHR = [65, 70, 90, 80]
soVis = [50, 40, 35, 30]
soLF = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]
soTV = [5000, 7000, 9000,11000]
soEDV = [70, 75, 80, 90]
soESV = [10, 10, 15, 20]
apply = 4
ctSim = [2, 15, 20, 40]
'''

sys = Regelkreis(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, totalVolume, maxTime)

currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV]
sys.controlSystem(currVals, soHR, soLF, soVis, soTV, soEDV, soESV, apply, lens, nums, ctSim)
