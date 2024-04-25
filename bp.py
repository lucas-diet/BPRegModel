
import numpy as np
import matplotlib.pyplot as plt

def simulate_blood_pressure(duration, heart_rate, systolic_factor=1.2, diastolic_factor=0.8, noise_level=0.0):
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
    # Zeitachse
    t = np.linspace(0, duration, int(duration * 100))  # Abtastung mit 100 Hz
    
    # Simuliere Herzfrequenz mit Sinusfunktion
    heart_rate_signal = np.sin(2 * np.pi * heart_rate/ 60 * t) + 1
    
    # Skaliere den Blutdruck basierend auf der Herzfrequenz
    systolic_pressure = systolic_factor * heart_rate_signal + np.random.normal(scale=noise_level, size=len(t))
    diastolic_pressure = diastolic_factor * heart_rate_signal + np.random.normal(scale=noise_level, size=len(t))

    blood_pressure = systolic_factor * heart_rate_signal + diastolic_factor * heart_rate_signal + np.random.normal(scale=noise_level, size=len(t))

    mad_1 = diastolic_pressure + (1/2) * (systolic_pressure - diastolic_pressure)
    mad_2 = diastolic_pressure + (1/3) * (systolic_pressure - diastolic_pressure)
    
    return systolic_pressure, diastolic_pressure, mad_1, mad_2

# Simuliere Blutdruck mit einer Herzfrequenz von 75 Schlägen pro Minute für 60 Sekunden
duration = 60  # Sekunden
heart_rate = 10  # Schläge pro Minute
systolic_pressure, diastolic_pressure , mad_1, mad_2 = simulate_blood_pressure(duration, heart_rate)

# Plot der simulierten Blutdruckwerte
#fig, axs = plt.subplots(2)
#fig.suptitle('Simulierter Blutdruck über Zeit (Herzfrequenz = {} bpm)'.format(heart_rate))
plt.plot(np.linspace(0, duration, len(systolic_pressure)), systolic_pressure, label='systolische Blutdruck')
plt.plot(np.linspace(0, duration, len(diastolic_pressure)), diastolic_pressure, label='diastolische Blutdruck')

plt.plot(np.linspace(0, duration, len(mad_1)), mad_1, label='herznahe Arterien mittleren arteriellen Blutdruck', color='red')
plt.plot(np.linspace(0, duration, len(mad_2)), mad_2, label='herzferne Arterien mittleren arteriellen Blutdruc', color='green')

plt.xlabel('Zeit (s)')
plt.ylabel('mmHg')
plt.grid(True)
plt.legend()
plt.show()
