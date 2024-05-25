

from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *

####################
#### Parameter #####
####################

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
viscocity = 0.1 ## Wie hoch ist der Wasseranteil? Wenn hoch niedriger Druck wenn niedrig höherer Druck
heartRate = 70
strokeVolume = 70
maxElasticity = 2
edv = 110
esv = 60
pres0 = 70
maxTime = 10
dt = 0.01

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300] # in mm
type = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']

##########################
##### Blood Pressure ##### ---> Wie solle es ca. am Ende aussehen. Dient nur als Einstieg.
##########################

duration = 60       # Sekunden
heart_rate = 10     # Schläge pro Minute
systolic = 120      # TODO: soll noch simuliert werden mit Parametern
diastolic = 80      # TODO: soll noch simuliert werden mit Parametern

bpSim = BloodPressure(duration, heart_rate, systolic, diastolic)
#bp = bpSim.simulateBP()

# Plot der simulierten Blutdruckwerte
#bpSim.bpPlotter()

################
#### Heart #####
################

h = Heart(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)
h.hpPlotter()

#######################
##### Body System #####
#######################

lims = [-17, 17]
lumFactor = [1, 1, 1, 1, 1, 1, 1] # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren

bs = BodySystem(radi, lumFactor, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime)
#bs.vesselPlotter(lumFactor, lims)
#bs.resisPrinter(type, lens, radi, lumFactor, nums)
bs.vpPlotter()

##################
##### Sensor #####
##################

data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
types = ['Rechter Ventrikel', 'Linker Ventrikel', 'Aorta', 'Arterie', 'Arteriole', 'Kapillare', 'Venole', 'Vene', 'V. Cava']

s = Sensor(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)

h.heartSimulation()
bs.vesselSimulator()

s.presPlotter(data)
s.presPrinter(dataC, types)
