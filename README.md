English version below

# BPRegModel

Es wurde ein Modell zur Blutdruckregulation im Menschen als Regelkreis implementiert. Dabei wurden die wichtigsten Komponenten des Blutsystems jeweils in eigenen Dateien realisiert.

### bloodPressure.py
Diese Datei enthält eine Funktion, die aufgrund der speziellen Blutdruckkurvenform eine Annäherung der Blutdruckkurve vornimmt.

Diese Funktion wird über `import` in anderen Dateien verwendet, um dort weitere Komponenten zu implementieren.

### heart.py
Hier wurde das Herz modelliert, wobei das linke und rechte Herz sowie die beiden Hauptkammern in separaten Funktionen umgesetzt wurden. Zusätzlich gibt es eine Funktion zur Visualisierung des Druckverlaufs in den Herzkammern.

### bodySystem.py
Das Gefäßsystem wurde hier umgesetzt. Dazu wurden alle Gefäßarten (Aorta, Arterie, Arteriole, Kapillare, Venole, Vene, V. Cava) jeweils in einer eigenen Funktion modelliert und miteinander verbunden, um den Druckverlauf durch das Gefäßsystem zu simulieren.

Für jede Gefäßart wurde eine Funktion implementiert, um den Druckverlauf zu modellieren und schließlich Druckwerte für jede Gefäßart zu generieren.

Zusätzlich wurde der Gefäßwiderstand (Reihen- und Parallelwiderstand) berechnet, um die Druckwerte zu ermitteln.

Weitere Funktionen zur Ausgabe von Widerständen in der Konsole sowie zur Visualisierung der Druckwerte sind ebenfalls implementiert.

### sensor.py
Hier wurden die Sensoren für die Blutgefäße implementiert, um den Blutdruck zu messen. Dabei werden systolischer und diastolischer Druck ermittelt, um anschließend den mittleren Druck zu berechnen.

Zusätzlich gibt es Funktionen zur Ausgabe der verschiedenen Drücke in der Konsole für jede Gefäßart.

### controlSystem.py
In dieser Datei wird der eigentliche Regelkreis realisiert. Dabei werden Objekte aus den anderen Klassen erstellt, um den aktuellen Zustand zu simulieren. Anschließend werden Soll-Werte übergeben, um den aktuellen Zustand auf den Soll-Zustand einzustellen.

### Main.py
Diese Datei dient zur Interaktion mit dem Modell und enthält alle wichtigen Funktionen, die für die Visualisierung oder Ausgabe in der Konsole benötigt werden.

Dafür müssen die entsprechenden Funktionen nur durch Entkommentieren aktiviert werden, wenn der Nutzer diese Informationen benötigt. Dies umfasst die Ausgabe von Widerständen, die Visualisierung der Radien und Druckverläufe sowie die Darstellung der Regelkreise.

Außerdem enthält Main Anwendungsbeispiele, die bei Bedarf einfach aktiviert werden können, indem die erforderlichen Parameter (initiale, dynamische und Soll-Parameter) gesetzt werden.

---------------------------------------------------------------------


A model for blood pressure regulation in humans has been implemented as a control loop. The main components of the circulatory system were implemented in separate files.

### bloodPressure.py
This file contains a function that approximates the blood pressure curve based on its specific waveform.

This function is imported into other files to implement additional components.

### heart.py
Here, the heart was modeled, with the left and right sides and the two main chambers implemented in separate functions. Additionally, there is a function to visualize the pressure changes within the heart chambers.

### bodySystem.py
The vascular system was implemented here. All types of vessels (aorta, artery, arteriole, capillary, venule, vein, vena cava) were modeled in separate functions and interconnected to simulate pressure changes throughout the vascular system.

For each type of vessel, a function was implemented to model the pressure changes and generate pressure values.

Additionally, vascular resistance (series and parallel resistance) was calculated to determine pressure values.

Additional functions for printing resistances in the console and visualizing pressure values were also implemented.

### sensor.py
Sensors for blood vessels were implemented here to measure blood pressure. This includes determining systolic and diastolic pressures to subsequently calculate mean arterial pressure.

Functions are also included to print various pressures in the console for each type of vessel.

### controlSystem.py
This file implements the actual control loop. Objects from other classes are instantiated to simulate the current state. Subsequently, setpoint values are provided to adjust the current state to the desired state.

### Main.py
This file facilitates interaction with the model and contains all essential functions for visualization or console output.

To use specific functions, they only need to be uncommented if the user requires that information. This includes printing resistances, visualizing radii and pressure curves, as well as displaying control loops.

Main also includes application examples that can be easily activated by setting the necessary parameters (initial, dynamic, and setpoint parameters).