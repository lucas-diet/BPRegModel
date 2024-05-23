

from bloodPressure import *
from heart import * 
from bodySystem import *
from sensor import *

#### Parameter #####

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
viscocity = 1
heartRate = 70
strokeVolume = 70
maxElasticity = 2
edv = 110
esv = 50
pres0 = 70
maxTime = 10
dt = 0.01

lims = [-17, 17]
lumRadiF = [1, 1, 1, 1, 1, 1, 1] # array, um den inneren Radius anpassen zu können -> ein Faktor zu skalieren

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300] # in mm
type = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']

##### BloodPressure #####

duration = 60       # Sekunden
heart_rate = 10     # Schläge pro Minute
systolic = 120      # TODO: soll noch simuliert werden mit Parametern
diastolic = 80      # TODO: soll noch simuliert werden mit Parametern

bpSim = BloodPressure(duration, heart_rate, systolic, diastolic)
#bp = bpSim.simulateBP()

# Plot der simulierten Blutdruckwerte
#bpSim.bpPlotter()

#### Heart #####

h = Heart(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)
#h.hpPlotter()

##### Body System #####

bs = BodySystem(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime)
#bs.vesselPlotter(lumRadiF, lims)
#bs.resisPrinter(type, lens, radi, lumRadiF, nums)

#bs.vpPlotter()

##### Sensor #####

s = Sensor(radi, viscocity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt)
#s.presPlotter()
#s.presPrinter()
