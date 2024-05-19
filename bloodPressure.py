
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
            
        Returns:
            Ein Array, um den mittleren Blutdruck zu simulieren.
        """

        # Zeitachse
        t = np.linspace(0, self.duration, int(self.duration * 10))  # Abtastung mit 100 Hz

        # Simuliere Herzfrequenz mit summierter Sinusfunktion
        p1 = systolic * np.sin(2 * np.pi * (self.heartRate / 60) * t)
        p2 = 0.63 * systolic * np.sin(4 * np.pi * (self.heartRate / 60) * t + (2 / np.pi))

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
            Normalisiert den durchschnuttlichen Blutdruck, indem im ersten Schritt auf [0,1]
            skaliert wird und im zweiten Schritt auf [diastolic, systolic].
        Args:
            mean_bp: Durchschnittlicher Blutdruck 

        Returns:
            _type_: _description_
        """
        # Normalisiere die Blutdruckwerte
        max_bp = np.max(mean_bp)
        min_bp = np.min(mean_bp)
		
        normalized_bp = (mean_bp - min_bp) / (max_bp - min_bp)  # Auf [0, 1] normalisieren
        normalized_bp = normalized_bp * (systolic - diastolic) + diastolic  # Skalieren auf [diastolic, systolic]
		
        return normalized_bp

# Simulation des Blutdruck
duration = 60       # Sekunden
heart_rate = 10     # Schläge pro Minute
systolic = 120      # TODO: soll noch simuliert werden mit Parametern
diastolic = 80      # TODO: soll noch simuliert werden mit Parametern
'''
bp_sim = BloodPressure(duration, heart_rate, systolic, diastolic)
bp = bp_sim.simulateBP()

# Plot der simulierten Blutdruckwerte
plt.plot(np.linspace(0, duration, len(bp)), bp, label='Blutdruck (mmHg)')
plt.xlabel('Zeit (s)')
plt.ylabel('mmHg')
plt.grid(True)
plt.ylim(diastolic-5, systolic+5)
plt.show()
'''