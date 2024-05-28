
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
viscosity = 0.1 ## 0 keine Auswirkung; 1 die Amplitude der ist vollständig reduzieren. -> != 0
heartRate = 70
strokeVolume = 70
maxElasticity = 2
edv = 110
esv = 60
pres0 = 70
maxTime = 5
dt = 0.01

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300] # in mm
type = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']

#####################
##### Blutdruck ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
#####################

duration = maxTime      # Sekunden
heart_rate = 10         # Schläge pro Minute
systolic = 120          # TODO: soll noch simuliert werden mit Parametern
diastolic = 80          # TODO: soll noch simuliert werden mit Parametern

bpSim = BloodPressure(duration, heart_rate, systolic, diastolic)

#bpSim.bpPlotter()       # Plot der simulierten Blutdruckwerte

###############
#### Herz #####
###############

h = Heart(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)

#h.hpPlotter()

########################
##### Körpersystem #####
########################

lims = [-17, 17]
lumFactor = [1, 1, 1, 1, 1, 1, 1] # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren

bs = BodySystem(radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime)

#bs.vesselPlotter(lumFactor, lims)
#bs.resisPrinter(type, lens, nums)
#bs.vpPlotter(type, lens, nums)

##################
##### Sensor #####
##################

data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
types = ['Rechter Ventrikel', 'Linker Ventrikel', 'Aorta', 'Arterie', 'Arteriole', 'Kapillare', 'Venole', 'Vene', 'V. Cava']

s = Sensor(radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)

h.heartSimulation()
bs.vesselSimulator(type, lens, nums)

#s.ppPlotter(data)
#s.presPrinter(dataC, types)

################
##### Hirn #####
################

targetPres = 10
activity = 10

b = brain(targetPres, heartRate, activity, radi, lumFactor, viscosity, strokeVolume, edv, esv, pres0, maxTime)

#s.brainSender(data)
#b.setPressure(data, targetPres)

#################
##### Leber #####
#################

l = Liver(viscosity, maxTime)

l.viscositySimulate('inc', 10, 0.1)