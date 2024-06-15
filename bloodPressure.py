
import numpy as np
import matplotlib.pyplot as plt

class BloodPressure():

    def __init__(self, duration=10, heartRate=50, systolic=120, diastolic=80):
        self.duration = duration
        self.heartRate = heartRate
        self.systolic = systolic
        self.diastolic = diastolic

    def simulateBP(self):
        """_summary_
            Simuliert den Blutdruck über eine bestimmte Dauer basierend auf der Herzfrequenz.
    
        Args:
            Keine expliziten Argumente, verwendet Klassenattribute.
            
        Returns:
            Ein Array, das den simulierten mittleren Blutdruck über die Zeit darstellt.
        """

        # Zeitachse
        t = np.linspace(0, self.duration, int(self.duration * 100))  # Abtastung mit 100 Hz

        # Simuliere Herzfrequenz mit summierter Sinusfunktion
        p1 = self.systolic * np.sin(2 * np.pi * (self.heartRate / 60) * t)
        p2 = 0.63 * self.systolic * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))

        heartRateSignal = p1 + p2
        
        # systolic_factor = systolic / 100 -> um zu skalieren
        # diastolic_factor = diastolic / 100 -> um zu skalieren
        diastolicPressure = (self.diastolic / 100) * heartRateSignal
        systolicPressure = (self.systolic / 100) * heartRateSignal

        mean_bp = diastolicPressure + (1/3) * (systolicPressure - diastolicPressure)
        
        bp = self.normalizeBP(mean_bp)

        return bp
    
    def normalizeBP(self, mean_bp):
        """_summary_
            Normalisiert den durchschnittlichen Blutdruck, indem er im ersten Schritt auf [0,1]
            skaliert wird und im zweiten Schritt auf [diastolic, systolic].
        
        Args:
            mean_bp: Durchschnittlicher Blutdruck als Array.
            
        Returns:
            normalized_bp: Normalisierter Blutdruck als Array, skaliert auf den Bereich [diastolic, systolic].
        """
        
        max_bp = np.max(mean_bp)
        min_bp = np.min(mean_bp)
		
        normalized_bp = (mean_bp - min_bp) / (max_bp - min_bp)  # Auf [0, 1] normalisieren
        normalized_bp = normalized_bp * (self.systolic - self.diastolic) + self.diastolic  # Skalieren auf [diastolic, systolic]
		
        return normalized_bp
    
    def bpFunction(self, t, heartRate):
        """_summary_
            Liefert die Grundstruktur für die Kurve des Blutdrucks.
        
        Args:
            t (array-like): Zeitachse.
            heartRate (int): Herzfrequenz in Schlägen pro Minute.

        Returns:
            tuple: Zwei Arrays, die die Grundstrukturen der Blutdruckkurve repräsentieren.
        """
        
        p1 = np.sin(2 * np.pi * (heartRate / 60) * t)
        p2 = 0.63 * np.sin(4 * np.pi * (heartRate / 60) * t + (2 / np.pi))
        
        return p1, p2
    
    def bpPlotter(self):
        """_summary_
            Plottet die basierend auf den Parametern die Grundstruktur einer Blutdruckkurve.
        
        Args:
            None
        
        Returns:
            None
        """
        
        bp_sim = BloodPressure(self.duration, self.heartRate, self.systolic, self.diastolic)
        bp = bp_sim.simulateBP()

        plt.figure(figsize=(11, 7))
        plt.plot(np.linspace(0, self.duration, len(bp)), bp, label='Blutdruck')
        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.grid(True)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})
        plt.ylim(self.diastolic-5, self.systolic+5)
        plt.show()