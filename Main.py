
from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *
from brain import *
from liver import *

####################
#### Parameter #####
####################

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
viscosity = 0.5                 # 0 keine Auswirkung; 1 die Amplitude ist vollständig reduzieren. -> != 0
heartRate = 70
strokeVolume = 70               # Schlagvolumen 
edv = 110                       # Enddiastolische Volumen
esv = 60                        # Endsystolisches Volumen
pres0 = 70                      
maxTime = 5

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300] # in mm

prop = 'inc'                    # 'inc' zum erhöhen ; 'dec' zum verringern
interval = 3                    # Zeitschritte, wo verändert wird
change = 0.1                    # Wert um den verändert wird

#####################
##### Blutdruck ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
#####################

duration = maxTime      # Sekunden
heart_rate = 10         # Schläge pro Minute
systolic = 120          # TODO: soll noch simuliert werden mit Parametern
diastolic = 80          # TODO: soll noch simuliert werden mit Parametern

## Klasse ##
bpSim = BloodPressure(duration, heart_rate, systolic, diastolic)

#bpSim.bpPlotter()      # Plot der simulierten Blutdruckwerte

###############
#### Herz #####
###############

## Klasse ##
h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

#h.hpPlotter()

########################
##### Körpersystem #####
########################

##### Extra Parameter #####
lims = [-17, 17]
lumFactor = [1, 1, 1, 1, 1, 1, 0.1]           # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren
###########################

## Klasse ##
bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

#bs.vesselPlotter(lumFactor, lims)
#bs.resisPrinter(lens, nums)
bs.vpPlotter(lens, nums, prop, interval, change)

##################
##### Sensor #####
##################

data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]

## Klasse ##
s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

h.heartSimulation()
bs.vesselSimulator(lens, nums, prop, interval, change)

#ås.ppPlotter(data)
s.presPrinter(dataC)

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