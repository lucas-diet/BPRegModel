
import math
import numpy as np
import matplotlib.pyplot as plt

class BloodPressure():

    def __init__(self, duration=10, heart_rate=50, systolic=120):
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
            noise_level (float): Niveau des Rauschens in der Simulation (Standard: 0.2).
        
        Returns:
            tuple: Zwei Arrays für den simulierten systolischen und diastolischen Blutdruck.
        """
        duration = self.duration
        heart_rate = self.heart_rate
        systolic = self.systolic

        # Zeitachse
        t = np.linspace(0, duration, int(duration * 100))  # Abtastung mit 100 Hz

        # Simuliere Herzfrequenz mit Sinusfunktion
        heart_rate_signal = systolic * np.sin(2 * np.pi * (heart_rate/60) * t) + 0.63 * systolic * np.sin(4 * np.pi * (heart_rate / 60) * t + (2 / np.pi))
        
        diastolic_pressure = diastolic_factor * heart_rate_signal
        systolic_pressure = systolic_factor * heart_rate_signal

        mean_blood_pressure = diastolic_pressure + (1/3) * (systolic_pressure - diastolic_pressure)
        
        return mean_blood_pressure

# Simuliere Blutdruck mit einer Herzfrequenz von 75 Schlägen pro Minute für 60 Sekunden
duration = 10  # Sekunden
heart_rate = 50  # Schläge pro Minute
systolic = 120

bp_sim = BloodPressure(duration, heart_rate, systolic)
bp = bp_sim.simulate_blood_pressure()


# Plot der simulierten Blutdruckwerte
plt.plot(np.linspace(0, duration, len(bp)), bp, label='Blutdruck (mmHg)')
plt.xlabel('Zeit (s)')
plt.ylabel('mmHg')
plt.grid(True)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
plt.show()
