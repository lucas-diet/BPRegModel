
import numpy as np
import matplotlib.pyplot as plt

from bloodPressure import *
from bodySystem import * 
from heart import *
from sensor import *
from liver import *


class Regelkreis():
    
    def __init__(self, radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime, dt=0.01):
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

    def controlSystemPlotter(self, i, rw, hr, time):
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
        
        plt.figure(figsize=(11, 7), num=f'Simulationsdurchlauf {i+2}')
        plt.title(f'Simulation des Gefäßsystem; {hr}')
        plt.plot(time, rw[2], label='Aorta Druck')
        plt.plot(time, rw[3], label='Arterie Druck')
        plt.plot(time, rw[4], label='Arteriole Druck')
        plt.plot(time, rw[5], label='Kapillare Druck')
        plt.plot(time, rw[6], label='Venole Druck')
        plt.plot(time, rw[7], label='Vene Druck')
        plt.plot(time, rw[8], label='V. Cava Druck')

        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.grid(True)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})
        plt.show()

    def controlSystem(self, currVals, soHR, soLF, soVis, soTV, runs, lens, nums):
        """_summary_
            Simuliert und regelt das Gefäßsystem für mehrere Durchläufe.

        Args:
            currVals (list): Liste der aktuellen Werte für Herzfrequenz, Viskosität, Radiusfaktor und Volumen.
            soHR (list): Liste der Herzfrequenzen für jeden Durchlauf.
            soLF (list): Liste der Radiusfaktoren für jeden Durchlauf.
            soVis (list): Liste der Viskositäten für jeden Durchlauf.
            soTV (list): Liste der Volumina für jeden Durchlauf.
            runs (int): Anzahl der Durchläufe.
            lens (array): Längen der verschiedenen Gefäßarten.
            nums (array): Anzahl der verschiedenen Gefäßarten.
        
        Returns:
            None
        """
        #currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol]

        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.totalVolume, self.maxTime)
        bs = BodySystem(self.radi, self.lumFactor, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.totalVolume, self.maxTime)
        s = Sensor(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.maxTime)

        h.heartSimulation()
        bs.vesselSimulator(lens, nums, currVals[0], currVals[1], currVals[2], currVals[3], currVals[4], currVals[5], currVals[6], currVals[7])

        isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava = bs.getPressurs()
        isRV = h.bloodPressure_RV
        isLV = h.bloodPressure_LV

        isPres = [isRV, isLV, isAorta, isArterie, isArteriol, isCapillare, isVenole, isVene, isVCava]

        for i in range(0, runs):
            nHR = soHR[i]
            nVis = soVis[i]
            nLF = soLF[i]
            nTV = soTV[i]

            soH = Heart(self.radi, nVis, nHR, self.strokeVolume, self.edv, self.esv, self.pres0, nTV, self.maxTime)
            soBS = BodySystem(self.radi, nLF, nVis, nHR, self.strokeVolume, self.edv, self.esv, self.pres0, nTV, self.maxTime)
            soS = Sensor(self.radi, nVis, nHR, self.strokeVolume, self.edv, self.esv, self.pres0, self.maxTime)

            #currVals = [ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol]
            
            soH.heartSimulation()
            soBS.vesselSimulator(lens, nums, currVals[0], soHR, currVals[2], soVis, currVals[4], currVals[5], currVals[6], soTV)

            #### Regelstrecke ####
    
            soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava = soBS.getPressurs()
            soRV = soH.bloodPressure_RV
            soLV = soH.bloodPressure_LV
            soPres = [soRV, soLV, soAorta, soArterie, soArteriol, soCapillare, soVenole, soVene, soVCava]

            soS.presPrinter(soPres)

            #### Regelabweichung ####
            rwRV = soRV - isRV
            rwLV = soLV - isLV
            rwAorta = soAorta - isAorta
            rwArterie = soArterie - isArterie
            rwArteriol = soArteriol - isArteriol
            rwCapillare = soCapillare - isCapillare
            rwVenole = soVenole - isVenole
            rwVene = soVene - isVene
            rwVCava = soVCava - isVCava

            rwPres = [rwRV, rwLV, rwAorta, rwArterie, rwArteriol, rwCapillare, rwVenole, rwVene, rwVCava]
            rwMins = [np.min(rwRV), np.min(rwLV), np.min(rwAorta), np.min(rwArterie), np.min(rwArteriol), np.min(rwCapillare), np.min(rwVenole), np.min(rwVene), np.min(rwVCava)]

            rwP = []

            for j in range(0, len(rwPres)):
                rwP.append(rwPres[j] - rwMins[j])

            #s.presPrinter(rwP)
            print('\n', '#####', i+1)
            self.controlSystemPlotter(i, rwP, nHR, bs.time)
            
            isRV = rwRV
            isLV = rwLV
            isAorta = rwAorta
            isArterie = rwArterie
            isArteriol = rwArteriol
            isCapillare = rwCapillare
            isVenole = rwVenole
            isVene = rwVene
            isVCava = rwVCava
