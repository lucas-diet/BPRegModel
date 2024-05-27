
from sensor import *

class brain():
    
    def __init__(self, targetPres, heartRate, activity, radi, lumFactor, viscocity, strokeVolume, edv, esv, pres0, maxTime):
        self.targetPres = targetPres
        self.heartRate = heartRate
        self.activity = activity

        self.radi = radi 
        self.lumFactor = lumFactor, 
        self.viscocity = viscocity 
        self.strokeVolume = strokeVolume 
        self.edv = edv
        self.esv = esv
        self.pres0 = pres0
        self.maxTime = maxTime


    def getPressure(self, data):
        s = Sensor(self.radi, self.viscocity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.maxTime)
        return s.brainSender(data)
    
    def setPressure(self, data, targetPres):
        isPres = self.getPressure(data)
        
        maxs = isPres[0]
        mins = isPres[1]
        means = isPres[2]

        print(maxs)
        print(mins)
        print(means)

        if self.activity == 1:
            self.heartRate = 0
        
        elif self.activity == 2:
            self.heartRate = 0
        
        elif self.activity == 3:
            self.heartRate = 0

        elif self.activity == 4:
            self.heartRate = 0

        elif self.activity == 5:
            self.heartRate = 0

        elif self.activity == 6:
            self.heartRate = 0

        elif self.activity == 7:
            self.heartRate = 0

        