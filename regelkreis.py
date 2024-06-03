
from bloodPressure import *
from bodySystem import * 
from heart import *
from sensor import *
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


##### Extra Parameter für Sensor ##### (Sind fest und sollten nicht verändert werden!)
data = [bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
dataC = [h.bloodPressure_RV, h.bloodPressure_LV,  bs.aortaPressure, bs.arteriePressure, bs.arteriolPressure, bs.capillarePressure, bs.venolePressure, bs.venePressure, bs.vCavaPressure]
###########################
###########################

h.heartSimulation()
bs.vesselSimulator(lens, nums, prop, interval, change)

#### Regelstrecke ####

aorta, arterie, arteriol, capillare, venole, vene, vCava = bs.getPressurs()

#bs.vpPlotter(lens, nums, prop, interval, change)

#### Regelabweichung ####

#### Untersystem ####

