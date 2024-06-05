
from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *
from brain import *
from liver import *

####################
#### Parameter #####
####################

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

#### Parameter für die Leber ##### 
prop = 'inc'                                   # 'inc' zum erhöhen ; 'dec' zum verringern
interval = 200                                 # Zeitschritte, wo verändert wird
change = 0                                     # Wert um den verändert wird, wenn 0 dann keine Veränderung

#####################
##### Blutdruck ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
#####################

duration = maxTime      # Sekunden
systolic = 120          # TODO: soll noch simuliert werden mit Parametern
diastolic = 80          # TODO: soll noch simuliert werden mit Parametern

## Klasse ##
bpSim = BloodPressure(duration, heartRate, systolic, diastolic)

#bpSim.bpPlotter()      # Ausführbare Funktion

###############
#### Herz #####
###############

## Klasse ##
h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)

#h.hpPlotter()

########################
##### Körpersystem #####
########################

##### Extra Parameter #####
lims = [-17, 17]                            # Für den Achsenbereich, der angezeigt werden soll, wenn Radius der Gefäße geplottet wird.
lumFactor = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]           # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren
###########################

## Klasse ##
bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime)

#bs.vesselPlotter(lumFactor, lims)                  # Ausführbare Funktion
#bs.resisPrinter(lens, nums)                        # Ausführbare Funktion
bs.vpPlotter(lens, nums, prop, interval, change)    # Ausführbare Funktion

##################
##### Sensor #####
##################

##### Extra Parameter ##### (Sind fest und sollten nicht verändert werden!)
data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
###########################

## Klasse ##
s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

h.heartSimulation()
bs.vesselSimulator(lens, nums, prop, interval, change)

#s.ppPlotter(data)                                  # Ausführbare Funktion
s.presPrinter(dataC)                                # Ausführbare Funktion

### Findet den Blutdruck zu einem bestimmten Zeitpunkt ###
presData = data[0]                              # data[x] x = {0,1,2,3,4,5,6}
timeStemp = 1

s.printPressureTimePoint(presData, timeStemp)          # Ausführbare Funktion

################
##### Hirn #####
################

targetPres = 10
activity = 10

## Klasse ##
b = brain(targetPres, heartRate, activity, radi, lumFactor, viscosity, strokeVolume, edv, esv, pres0, maxTime)

s.brainSender(data)
b.setPressure(data, targetPres)

maxs, mins, means = b.getPressure(data)

#################
##### Leber #####
#################

## Klasse ##
l = Liver(viscosity, maxTime)

#l.viscositySimulate('inc', 50, 0.1)