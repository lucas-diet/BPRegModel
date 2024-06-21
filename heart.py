
import numpy as np
import matplotlib.pyplot as plt

class Heart():

    def __init__(self, radi, viscosity, heartRate, strokeVolume, edv, esv, totalVolume, maxTime, pres0=70, dt=0.01,):
        self.radi = radi
        self.viscosity = viscosity
        self.heartRate = heartRate
        self.strokeVolume = strokeVolume
        self.dt = dt
        self.edv = edv
        self.esv = esv
        self.pres0 = pres0
        self.totalVolume = totalVolume
        self.maxTime = maxTime

        self.time = np.arange(0, self.maxTime, dt)
        
        self.bloodPressure_RV = np.zeros_like(self.time)
        self.bloodVolume_RV = np.zeros_like(self.time)

        self.bloodPressure_LV = np.zeros_like(self.time)
        self.bloodVolume_LV = np.zeros_like(self.time)
    
    def normalize(self, data):
        """_summary_
            Normalisiert den Blutdruck auf den Bereich [diastolic, systolic].

        Args:
            data (np.array): Array der Blutdruckwerte, die normalisiert werden sollen.

        Returns:
            np.array: Normalisierte Blutdruckwerte im Bereich [diastolic, systolic].
        """

        max_bp = np.max(data)
        min_bp = np.min(data)
		
        normalized_bp = (data - min_bp) / (max_bp - min_bp)  # Auf [0, 1] normalisieren
        normalized_bp = normalized_bp * (self.esv - self.edv) + self.edv  # Skalieren auf [diastolic, systolic]

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
    
    def rightVentricle(self, ctEDV=[], newEDV=[], ctESV=[], newESV=[], shift=-0.5):
        """_summary_
            Simuliert den rechten Ventrikel des Herzens über die Zeit.

        Args:
            shift (float, optional): Verschiebung in der Zeit für die Elastizitätsberechnung. Default ist -0.5.

        Returns:
            None
        """
        
        viskosityEffect = self.viscosity / 100
        
        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        currentEDV = self.edv
        currentESV = self.esv
        currSV = self.strokeVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentEDV = self.updateParameter(t, ctEDV, newEDV, currentEDV)
            currentESV = self.updateParameter(t, ctESV, newESV, currentESV)
            currSV = currentEDV - currentESV
            print(t, currentEDV, currentESV, currSV)
              
            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * (t - shift) / 60)

            if i == 0:
                self.bloodVolume_RV[i] = currentEDV
            else:
                dVdt = currSV - elasticity * (self.bloodVolume_RV[i-1] - currentESV)
                self.bloodVolume_RV[i] = self.bloodVolume_RV[i-1] + dVdt * self.dt

            self.bloodPressure_RV[i] = elasticity * (self.bloodVolume_RV[i] - currentESV) * 0.15 + volumeEffect + viskosityEffect + 3

    def leftVentricle(self, ctEDV=[], newEDV=[], ctESV=[], newESV=[], shift=0):
        """_summary_
            Simuliert den linken Ventrikel des Herzens über die Zeit.

        Args:
            shift (float, optional): Verschiebung in der Zeit für die Elastizitätsberechnung. Standard ist 0.

        Returns:
            None
        """

        viskosityEffect = self.viscosity / 100
        
        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        currentEDV = self.edv
        currentESV = self.esv
        currSV = self.strokeVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentEDV = self.updateParameter(t, ctEDV, newEDV, currentEDV)
            currentESV = self.updateParameter(t, ctESV, newESV, currentESV)
            currSV = currentEDV - currentESV

            elasticity = 1 + np.sin(2 * np.pi * self.heartRate * (t - shift) / 60)

            if i == 0:
                self.bloodVolume_LV[i] = currentEDV
            else:
                dVdt = currSV - elasticity * (self.bloodVolume_LV[i-1] - currentESV)
                self.bloodVolume_LV[i] = self.bloodVolume_LV[i-1] + dVdt * self.dt

            self.bloodPressure_LV[i] = elasticity * (self.bloodVolume_LV[i] - currentESV) + volumeEffect + viskosityEffect + 10
    
    def heartSimulation(self, ctEDV, newEDV, ctESV, newESV):
        """_summary_
            Simuliert das gesamte Herz, indem es die rechte und linke Herzkammer simuliert.

        Args:
            None
        
        Returns:
            None
        """

        self.rightVentricle(ctEDV, newEDV, ctESV, newESV)
        self.leftVentricle(ctEDV, newEDV, ctESV, newESV)

    def hpPlotter(self, ctEDV, newEDV, ctESV, newESV):
        """_summary_
            Stellt eine Simulation des Herzens dar, indem es den Druck und das Volumen der linken und rechten Herzkammer im Zeitverlauf anzeigt.
            
        Args:
            None
        
        Returns:
            None
        """
        
        plt.figure(figsize=(11, 7))
        
        self.heartSimulation(ctEDV, newEDV, ctESV, newESV)

        plt.plot(self.time, self.bloodPressure_RV, label='Rechter Ventrikel Druck (mmHg)')
        plt.plot(self.time, self.bloodPressure_LV, label='Linker Ventrikel Druck (mmHg)')
        plt.plot(self.time, self.bloodVolume_LV, label='Linker Ventrikel Volumen (ml)')
        
        plt.xlabel('Zeit (s)')
        plt.ylabel('Werte')
        plt.title('Simulation des Herzen')
        plt.grid(True)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})

        plt.show()