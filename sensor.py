
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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
        """_summary_
            Nimmt die Blutdruckwerde aller Gefäßarten in einem Array und ermittelt daraus den systolischen und diastolischen Druck.
            Da nicht jeder gefundene Peak dem systolischen oder diastolischen Druck entspricht, wird hier nochmal gefiltet.
        Args:
            data (array): Ein Array, der aus den 7 Elementen besteht, wo jedes die Blutdruckwerte einer Gefäßart beseitzt.

        Returns:
            _type_: Punkte der systolische und diastolsche Drücke.
        """
        systolicPeaks, _ = find_peaks(data)
        diastolicPeaks, _ = find_peaks(-data)

        filteredSystolicPeaks = systolicPeaks[0::2]  # Wähle jeden zweiten systolischen Peak
        filteredDiastolicPeaks = diastolicPeaks[1::2]  # Wähle jeden zweiten diastolischen Peak

        return filteredSystolicPeaks, filteredDiastolicPeaks
    
    def calculatePressure(self, data, sPeaks, dPeaks):
        """_summary_

        Args:
            data (array): Ein Array, der aus den 7 Elementen besteht, wo jedes die Blutdruckwerte einer Gefäßart beseitzt.
            sPeaks (_type_): Punkt dür den systolischer Druck
            dPeaks (_type_): Punkt für den diastolischen Druck

        Returns:
            float : Mittlerer Durck 
        """
        meanSys = np.mean(data[sPeaks])
        meanDia = np.mean(data[dPeaks])

        map = meanDia + (1/3) * (meanSys - meanDia)

        return map
    
    def brainSender(self, data):
        """_summary_
            Legt erstamal 3 leere Arrays an, jeweils einen für die systolischen, diastolischen und mittleren Dürcke.
            Dann wird über datagelaufen und für jedes Element in data die Punkte für systolischen und diastolischen Druck bestimmt.
            Dann wird  mit dem Aufruf der Funktion calculatePressure der mittlere Druck bestimmt.

            Anschließen werden alle berechneten Werte in eines der angeleghten Arrays gespeichert.
        Args:
            data (array): Ein Array, der aus den 7 Elementen besteht, wo jedes die Blutdruckwerte einer Gefäßart beseitzt.

        Returns:
            array: 3 Arrays, die jeweils die berechneten Werte der Drücke beseitzt.
        """
        maxs = []
        mins = []
        means = []

        for d in data:
            sys, _ = self.findPeak(d)
            _, dia = self.findPeak(d)
            
            #self.calculatePressure(d, sys, dia)
            map = self.calculatePressure(d, sys, dia)

            maxs.append(np.mean(d[sys]))
            mins.append(np.mean(d[dia]))
            means.append(map)

        return maxs, mins, means
 
    def ppPlotter(self, data):
        """_summary_
            Eine Funktion, die die Peaks im Plot für die Gefäßdrücke markeirt.
        Args:
            data (array): Ein Array, der aus den 7 Elementen besteht, wo jedes die Blutdruckwerte einer Gefäßart beseitzt. 
        """
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

    def findPressureTimePoint(self, presData, timeStemp):
        """_summary_
            Liefert den Druckwert zu einem übergebenen Zeitpunkt.
        Args:
            presData (array): Ein Array mit Druckwerten zu jedem Zeitpunkt i
            timeStemp (int): Eine festgelegter Zeitpunkt

        Returns:
            pressureTime (float) : Druck zum Zeitpunkt timeStemp
        """
        pressureTime = presData[timeStemp]
        return pressureTime
    
    def presPrinter(self, data):
        """_summary_
            Nimmt ein Array und printet für jedes Element den systolischen, diastolsichen und mittleren Druck
        Args:
            data (array): Ein Array, der aus den 9 Elementen besteht, wo jedes die Blutdruckwerte einer Gefäßart beseitzt. 
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

    def printPressureTimePoint(self, presData, timeStemp):
        """_summary_
            Ruft eine Funktion auf und printet dann den Druck zum Zeitpunkt timeStemp
        Args:
            presData (array): Ein Array mit Druckwerten zu jedem Zeitpunkt i
            timeStemp (int): Eine festgelegter Zeitpunkt
        """
        print('\n', '#####', 'Blutdruck zu einem Zeitpunkt', '#####', '\n')
        print(f'Blutdruck bei {self.time[timeStemp]}: ', self.findPressureTimePoint(presData, timeStemp), 'mmHg')

    def detectHeartRate(self):
        return self.heartRate