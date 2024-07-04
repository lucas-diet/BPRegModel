
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

class Sensor():

    def __init__(self, radi, viscosity, heartRate, strokeVolume, edv, esv, maxTime, pres0=70, dt=0.01):
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
        """_summary_
            Ermittelt systolische und diastolische Druckspitzen aus den Blutdruckwerten aller Gefäßarten.

        Args:
            data (array): Ein Array mit den Blutdruckwerten der 7 Gefäßarten.

        Returns:
            filteredSystolicPeaks (array): Array mit den Punkten der systolischen Druckspitzen.
            filteredDiastolicPeaks (array): Array mit den Punkten der diastolischen Druckspitzen.
        """

        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        filteredSystolicPeaks = systolicPeaks[0::2]  # Wähle jeden zweiten systolischen Peak
        filteredDiastolicPeaks = diastolicPeaks[1::2]  # Wähle jeden zweiten diastolischen Peak

        return filteredSystolicPeaks, filteredDiastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        """_summary_
            Berechnet den mittleren arteriellen Druck (MAP) aus den Blutdruckwerten einer Gefäßart.

        Args:
            data (array): Ein Array mit den Blutdruckwerten der Gefäßart.
            sPeaks (array): Indizes der systolischen Druckspitzen.
            dPeaks (array): Indizes der diastolischen Druckspitzen.

        Returns:
            float: Mittlerer arterieller Druck (MAP).
        """

        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])

        map = meanDia + (1/3) * (meanSys - meanDia)

        return map
    
    def ppPlotter(self, data):
        """_summary_
            Plottet die Blutdruckwerte aller Gefäßarten und markiert die systolischen und diastolischen Peaks.

        Args:
            data (array): Ein Array, das die Blutdruckwerte aller Gefäßarten enthält.

        Returns:
            None
        """
        #data = [data1, data2, data3, data4, data5, data6, data7]
        plt.figure(figsize=(11, 7))
        for d in data:
            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)
            
            plt.plot(self.time, d)

            plt.plot(self.time[sys], d[sys], 'r.', label='Systolischer Druck')
            plt.plot(self.time[dia], d[dia], 'b.', label='Diastolischer Druck')

        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.grid(True)
        plt.show()

    def findPressureTimePoint(self, presData, timeStemp):
        """_summary_
            Gibt den Druckwert zum angegebenen Zeitpunkt zurück.

        Args:
            presData (array): Ein Array mit Druckwerten zu jedem Zeitpunkt.
            timeStemp (int): Ein bestimmter Zeitpunkt.

        Returns:
            pressureTime (float): Druckwert zum Zeitpunkt timeStemp.
        """

        pressureTime = presData[timeStemp]
        return pressureTime
    
    def presPrinter(self, data):
        """_summary_
            Nimmt ein Array und gibt für jede Gefäßart den systolischen, diastolischen und mittleren Druck aus.

        Args:
            data (array): Ein Array mit 9 Elementen, wobei jedes Element die Blutdruckwerte einer Gefäßart enthält.
        
        Returns:
            None
        """

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
        print()

    def printPressureTimePoint(self, presData, timeStemp):
        """_summary_
            Ruft die Funktion findPressureTimePoint auf und gibt den Druck zum Zeitpunkt timeStemp aus.

        Args:
            presData (array): Ein Array mit Druckwerten zu jedem Zeitpunkt i.
            timeStemp (int): Der festgelegte Zeitpunkt.

        Returns:
            None
        """

        print('\n', '#####', 'Blutdruck zu einem Zeitpunkt', '#####', '\n')
        print(f'Blutdruck bei {self.time[timeStemp]}: ', self.findPressureTimePoint(presData, timeStemp), 'mmHg')
