
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from bloodPressure import *
from heart import *
from bodySystem import *

class Sensor():

    def __init__(self, radi, viscosity, heartRate, strokeVolume, edv, esv, pres0, maxTime, dt=0.01):
        self.radi = radi
        self.viscosity = viscosity
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume 
        self.edv = edv 
        self.esv = esv 
        self.pres0 = pres0 
        self.maxTime = maxTime
        self.dt = dt
        self.time = np.arange(0, maxTime, dt)

    def findPeak(self, data):
        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        filteredSystolicPeaks = systolicPeaks[0::2]  # Wähle jeden zweiten systolischen Peak
        filteredDiastolicPeaks = diastolicPeaks[1::2]  # Wähle jeden zweiten diastolischen Peak

        return filteredSystolicPeaks, filteredDiastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])

        map = meanDia + (1/3) * (meanSys - meanDia)

        return map
    
    def brainSender(self, data):

        maxs = []
        mins = []
        means = []

        for d  in data:

            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)
            
            self.calculatePressure(d, sys, dia)
            map = self.calculatePressure(d, sys, dia)

            maxs.append(np.mean(d[sys]))
            mins.append(np.mean(d[dia]))
            means.append(map)

        return maxs, mins, means
 
    def ppPlotter(self, data):
        #data = [data1, data2, data3, data4, data5, data6, data7]

        for d in data:
            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)

            plt.plot(self.time, d)

            plt.plot(self.time[sys], d[sys], 'r.')
            plt.plot(self.time[dia], d[dia], 'b.')

        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.grid(True)
        plt.show()
    
    def presPrinter(self, data):
        types = ['Rechter Ventrikel', 'Linker Ventrikel', 'Aorta', 'Arterie', 'Arteriole', 'Kapillare', 'Venole', 'Vene', 'V. Cava']
        type = iter(types)

        for d in data:
            print('\n', '#####  ', next(type) , '  #####', '\n')

            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)

            map = self.calculatePressure(d, sys, dia)
            print('Systolischer Druck: ', np.mean(d[sys]), 'mmHg')
            print('Diastolischer Druck: ', np.mean(d[dia]), 'mmHg')
            print('Mittlerer Druck', map, 'mmHg')