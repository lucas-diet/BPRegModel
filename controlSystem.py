
import numpy as np
import matplotlib.pyplot as plt

from bloodPressure import *
from bodySystem import * 
from heart import *
from sensor import *
from liver import *

class Regelkreis():
    
    def __init__(self, radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv,  totalVolume, maxTime, pres0=70, dt=0.01):
        self.radi = radi        
        self.lumFactor = lumFactor
        self.viscosity = viscosity
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume 
        self.edv = edv 
        self.esv = esv 
        self.pres0 = pres0
        self.totalVolume = totalVolume
        self.maxTime = maxTime
        self.time = np.arange(0, maxTime, dt)

    def controlSystemPlotter(self, rw, time):
        """_summary_
            Plottet die Druckwerte verschiedener Gefäßarten über die Zeit.

        Args:
            iteration (int): Iterationsnummer der Simulation.
            vessel_pressures (list): Liste von Druckwerten für Aorta, Arterie, Arteriole,
                                    Kapillare, Venole, Vene und Vena Cava.
            heart_rate (str): Herzfrequenz oder anderer relevanter Titel für den Plot.
            time (array): Zeitpunkte, über die die Druckwerte geplottet werden sollen.

        Returns:
            None
        """
        plt.figure(figsize=(11, 7))
        plt.title(f'Simulation des Gefäßsystem')
        plt.plot(time, rw[2], label='Aorta Druck')
        plt.plot(time, rw[3], label='Arterie Druck')
        plt.plot(time, rw[4], label='Arteriole Druck')
        plt.plot(time, rw[5], label='Kapillare Druck')
        plt.plot(time, rw[6], label='Venole Druck')
        plt.plot(time, rw[7], label='Vene Druck')
        plt.plot(time, rw[8], label='V. Cava Druck')

        xticks = np.arange(0, 11)  # Originale Ticks von 0 bis 10
        xticks = xticks[xticks != 5]
        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.grid(True)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})
        plt.show()

    def updateParameter(self, t, changeTimes, newValues, currentValue):
        """_summary_
            Aktualisiert einen Parameter basierend auf den Änderungszeiten und neuen Werten.

        Args:
            t (float): Aktuelle Zeit, zu der der Parameter aktualisiert werden soll.
            changeTimes (list): Liste von Zeitpunkten, zu denen sich der Parameter ändern soll.
            newValues (list): Liste von neuen Werten für den Parameter entsprechend den changeTimes.
            currentValue: Aktueller Wert des Parameters.

        Returns:
            currentValue: Aktualisierter Wert des Parameters nach den Änderungen.
        """

        for j, changeTime in enumerate(changeTimes):
            if t >= changeTime:
                currentValue = newValues[j]
            else:
                break

        return currentValue

    def controlSystem(self, currVals, soHR, soLF, soVis, soTV, soEDV, soESV, runs, lens, nums, ctSim):
        """_summary_
            Simuliert und regelt das Gefäßsystem für mehrere Durchläufe.

        Args:
            currVals (list): Liste der aktuellen Werte für Herzfrequenz, Viskosität, Radiusfaktor und Volumen.
            soHR (list): Liste der Herzfrequenzen für jeden Durchlauf.
            soLF (list): Liste der Radiusfaktoren für jeden Durchlauf.
            soVis (list): Liste der Viskositäten für jeden Durchlauf.
            soTV (list): Liste der Volumina für jeden Durchlauf.
            soEDV (list): Liste der EDV-Werte für jeden Durchlauf. 
            soESV (list): Liste der ESV-Werte für jeden Durchlauf.
            runs (int): Anzahl der Durchläufe.
            lens (array): Längen der verschiedenen Gefäßarten.
            nums (array): Anzahl der verschiedenen Gefäßarten.
        
        Returns:
            None
        """
        
        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.totalVolume, self.maxTime)
        bs = BodySystem(self.radi, self.lumFactor, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.totalVolume, self.maxTime)
        #s = Sensor(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.maxTime)

        h.heartSimulation(currVals[8], currVals[9], currVals[10], currVals[11])
        bs.vesselSimulator(lens, nums, currVals[0], currVals[1], currVals[2], currVals[3], currVals[4], currVals[5], currVals[6], currVals[7])
        
        isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava = bs.getPressurs()
        isRV = h.bloodPressure_RV
        isLV = h.bloodPressure_LV
        #currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV]
    
        isPres = [isRV, isLV, isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava]
        rwNorm = []
        rwP = []
        
        if len(currVals[1]) == 0:
            pass
        else:
            self.heartRate = currVals[1][0]
        
        tHR = [self.heartRate] + soHR
        tVis = [self.viscosity] + soVis
        tLF = [self.lumFactor] + soLF
        tTV = [self.totalVolume] + soTV
        tEDV = [self.edv] + soEDV
        tESV = [self.esv] + soESV
        tSim = [ctSim[0]] + ctSim
        
        for i in range(0, runs):
            #print(tHR[i], tSim[i])
            nHR = tHR[i]
            nVis = tVis[i]
            nLF = tLF[i]
            nTV = tTV[i]
            nEDV = tEDV[i]
            nESV = tESV[i]

            soH = Heart(self.radi, nVis, nHR, self.strokeVolume, nEDV, nESV, nTV, self.maxTime)
            soBS = BodySystem(self.radi, nLF, nVis, nHR, self.strokeVolume, nEDV, nESV, nTV, self.maxTime)
            soS = Sensor(self.radi, nVis, nHR, self.strokeVolume, nEDV, nESV, self.maxTime)

            #soS = Sensor(self.radi, nVis, nHR, self.strokeVolume, nEDV, nESV, self.maxTime)
            #currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV]
            
            #soH.heartSimulation(currVals[10], soESV, currVals[8], soEDV)
            #soBS.vesselSimulator(lens, nums, ctSim, soHR, ctSim, soVis, currVals[4], nLF, ctSim, soTV)

            soH.heartSimulation(ctSim, soEDV, ctSim, soESV)
            soBS.vesselSimulator(lens, nums, ctSim, soHR, ctSim, soVis, currVals[4], currVals[5], ctSim, soTV)

            #### Regelstrecke ####
    
            soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava = soBS.getPressurs()
            soRV = soH.bloodPressure_RV
            soLV = soH.bloodPressure_LV
            soPres = [soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava]

            #### Regelabweichung ####
            if i == 0:
                rwRV  = np.copy(soRV)
                rwLV = np.copy(soLV)
                rwAorta = np.copy(soAorta)
                rwArterie = np.copy(soArterie)
                rwArteriol = np.copy(soArteriol)
                rwCapillare = np.copy(soCapillare)
                rwVenole = np.copy(soVenole)
                rwVene = np.copy(soVene)
                rwVCava = np.copy(soVCava)

            t = tSim[i]
            rwRV[t:t+1] = soRV[t:t+1] - isRV[t:t+1]
            rwLV[t:t+1] = soLV[t:t+1] - isLV[t:t+1]
            rwAorta[t:t+1] = soAorta[t:t+1] - isAorta[t:t+1]
            rwArterie[t:t+1] = soArterie[t:t+1] - isArterie[t:t+1]
            rwArteriol[t:t+1] = soArteriol[t:t+1] - isArteriol[t:t+1] 
            rwCapillare[t:t+1] = soCapillare[t:t+1] - isCapillare[t:t+1] 
            rwVenole[t:t+1] = soVenole[t:t+1] - isVenole[t:t+1]
            rwVene[t:t+1] = soVene[t:t+1] - isVene[t:t+1]
            rwVCava[t:t+1] = soVCava[t:t+1] - isVCava[t:t+1]
            
            rwPres = [rwRV, rwLV, rwAorta, rwArterie, rwArteriol, rwCapillare, rwVenole, rwVene, rwVCava]
            rwMins = [np.min(rwRV), np.min(rwLV), np.min(rwAorta), np.min(rwArterie), np.min(rwArteriol), np.min(rwCapillare), np.min(rwVenole), np.min(rwVene), np.min(rwVCava)]
           
            for j in range(len(rwPres)):
                normalized_array = []
                array_length = len(rwPres[j])
                for k, l in enumerate(rwPres[j]):
                    diff = l - rwMins[j]
                    if diff != 0:
                        normalized_array.append(diff)
                    else:
                        # Den Mittelwert der benachbarten Elemente berechnen
                        if k == 0:  # Erstes Element
                            new_value = (rwPres[j][k + 1] - rwMins[j]) / 2
                        elif k == array_length - 1:  # Letztes Element
                            new_value = (rwPres[j][k - 1] - rwMins[j]) / 2
                        else:  # Mittelwert der beiden Nachbarn
                            new_value = ((rwPres[j][k - 1] - rwMins[j]) + (rwPres[j][k + 1] - rwMins[j])) / 2
                        normalized_array.append(new_value)
                rwNorm.append(normalized_array)
                
            isRV = rwRV
            isLV = rwLV
            isAorta = rwAorta
            isArterie = rwArterie
            isArteriol = rwArteriol
            isCapillare = rwCapillare
            isVenole = rwVenole
            isVene = rwVene
            isVCava = rwVCava
        
       
        for i in rwNorm[0:9]:
            rwP.append(np.array(i))

        soS.presPrinter(rwP)
        print('\n', '#####')     
        self.controlSystemPlotter(rwP, bs.time)









        '''
        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.totalVolume, self.maxTime)
        bs = BodySystem(self.radi, self.lumFactor, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.totalVolume, self.maxTime)
        s = Sensor(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.maxTime)

        h.heartSimulation(currVals[8], currVals[9], currVals[10], currVals[11])
        bs.vesselSimulator(lens, nums, currVals[0], currVals[1], currVals[2], currVals[3], currVals[4], currVals[5], currVals[6], currVals[7])
        
        isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava = bs.getPressurs()
        isRV = h.bloodPressure_RV
        isLV = h.bloodPressure_LV

        isPres = [isRV, isLV, isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava]
        rwNorm = []

        soRV = np.copy(isRV)
        soLV = np.copy(isLV) 
        soAorta = np.copy(isAorta)
        soArterie = np.copy(isArterie)
        soArteriol = np.copy(isArteriol)
        soCapillare = np.copy(isCapillare) 
        soVenole = np.copy(isVenole)
        soVene = np.copy(isVene)
        soVCava = np.copy(isVCava)

        isHR = self.heartRate
        isVis = self.viscosity

        adjustment_factor = 0.0005

        for i in range(0, len(self.time)):
            t = self.time[i]

            if t in ctSim:
                for j in range(0, len(soHR)):
                    errorHR = soHR[j] - isHR
                    errorVis = soVis[j] - isVis
                
                    if errorHR > 0:
                        soRV[i:] += adjustment_factor * errorHR * isRV[i]
                        soLV[i:] += adjustment_factor * errorHR * isLV[i]
                        soAorta[i:] += adjustment_factor * errorHR * isAorta[i]
                        soArterie[i:] += adjustment_factor * errorHR * isArterie[i]
                        soArteriol[i:] += adjustment_factor * errorHR * isArteriol[i]
                        soCapillare[i:] += adjustment_factor * errorHR * isCapillare[i]
                        soVenole[i:] += adjustment_factor * errorHR * isVenole[i]
                        soVene[i:] += adjustment_factor * errorHR * isVene[i]
                        soVCava[i:] += adjustment_factor * errorHR * isVCava[i]
                    
                    elif errorHR < 0:
                        soRV[i:] -= adjustment_factor * errorHR * isRV[i]
                        soLV[i:] -= adjustment_factor * errorHR * isLV[i]
                        soAorta[i:] -= adjustment_factor * errorHR * isAorta[i]
                        soArterie[i:] -= adjustment_factor * errorHR * isArterie[i]
                        soArteriol[i:] -= adjustment_factor * errorHR * isArteriol[i]
                        soCapillare[i:] -= adjustment_factor * errorHR * isCapillare[i]
                        soVenole[i:] -= adjustment_factor * errorHR * isVenole[i]
                        soVene[i:] -= adjustment_factor * errorHR * isVene[i]
                        soVCava[i:] -= adjustment_factor * errorHR * isVCava[i]

                    
                    isHR = errorHR
                    isVis = errorVis
                    print(soHR[j], isHR, errorHR, t)
                    break
            

        

        soPres = [soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava]
        s.presPrinter(soPres)
        self.controlSystemPlotter(soPres, bs.time)
        '''
    

