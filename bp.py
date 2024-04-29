
import numpy as np
import matplotlib.pyplot as plt

class BloodPressure():

    def __init__(self, duration=10, heart_rate=50, systolic=120, diastolic=80):
        self. duration = duration
        self.heart_rate = heart_rate
        self.systolic = systolic

    def simulate_blood_pressure(self, systolic_factor=1.2, diastolic_factor=0.8):
        """
        Simuliert den Blutdruck über eine bestimmte Dauer basierend auf der Herzfrequenz.
        
        Args:
            duration (float): Simulationsdauer in Sekunden.
            heart_rate (int): Herzschläge pro Minute (Beats Per Minute).
            systolic_factor (float): Faktor zur Skalierung des systolischen Drucks (Standard: 1.2).
            diastolic_factor (float): Faktor zur Skalierung des diastolischen Drucks (Standard: 0.8).
        
        Returns:
            Ein Array, um den mittleren Blutdruck zu simulieren.
        """
        duration = self.duration
        heart_rate = self.heart_rate
        systolic = self.systolic

        # Zeitachse
        t = np.linspace(0, duration, int(duration * 100))  # Abtastung mit 100 Hz

        # Simuliere Herzfrequenz mit summierter Sinusfunktion
        p1 = systolic * np.sin(2 * np.pi * (heart_rate/60) * t)
        p2 = 0.63 * systolic * np.sin(4 * np.pi * (heart_rate / 60) * t + (2 / np.pi))

        heart_rate_signal = systolic + diastolic + p1 + p2
        
        diastolic_pressure = diastolic_factor * heart_rate_signal
        systolic_pressure = systolic_factor * heart_rate_signal

        mean_blood_pressure = diastolic_pressure + (1/3) * (systolic_pressure - diastolic_pressure)

        # Normalisiere die Blutdruckwerte
        max_bp = np.max(mean_blood_pressure)
        min_bp = np.min(mean_blood_pressure)
		
        normalized_bp = (mean_blood_pressure - min_bp) / (max_bp - min_bp)  # Auf [0, 1] normalisieren
        normalized_bp = normalized_bp * (systolic - diastolic) + diastolic  # Skalieren auf [diastolic, systolic]
		
        return normalized_bp

# Simulation des Blutdruck
duration = 10       # Sekunden
heart_rate = 50     # Schläge pro Minute
systolic = 120
diastolic = 80   

bp_sim = BloodPressure(duration, heart_rate, systolic, diastolic)
bp = bp_sim.simulate_blood_pressure()
print(np.max(bp))
print(np.min(bp))

# Plot der simulierten Blutdruckwerte
plt.plot(np.linspace(0, duration, len(bp)), bp, label='Blutdruck (mmHg)')
plt.xlabel('Zeit (s)')
plt.ylabel('mmHg')
plt.grid(True)
plt.ylim(diastolic-5, systolic+5)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
plt.show()
