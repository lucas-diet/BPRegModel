
import numpy as np
import matplotlib.pyplot as plt

from heart import Heart
from bloodPressure import BloodPressure

class BodySystem():

    def __init__(self, radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv,  totalVolume, maxTime, pres0 =70, dt=0.01):
        self.radi = radi

        self.aor_rad = radi[0]      # aorta
        self.art1_rad = radi[1]     # arterie
        self.art2_rad = radi[2]     # arteriole
        self.cap_rad = radi[3]      # kapillare
        self.ven1_rad = radi[4]     # venole
        self.ven2_rad = radi[5]     # vene
        self.vc_rad = radi[6]       # v.cava
        
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

        self.aortaPressure = np.zeros_like(self.time)
        self.arteriePressure = np.zeros_like(self.time)
        self.arteriolPressure = np.zeros_like(self.time)
        self.capillarePressure = np.zeros_like(self.time)
        self.venolePressure = np.zeros_like(self.time)
        self.venePressure = np.zeros_like(self.time)
        self.vCavaPressure = np.zeros_like(self.time)

    def vessel(self, radius, wallThickness, lumFactor=1):
        """_summary_
            Erzeugt die Querschnittsformen eines Gefäßes basierend auf dem Radius, der Wanddicke und einem Faktor
                für den inneren Radius.

        Args:
            radius (float): Radius des Gefäßes in Mikrometern (µm).
            wallThickness (float): Wanddicke des Gefäßes in Mikrometern (µm).
            lumFactor (float): Faktor zur Skalierung des inneren Radius, standardmäßig 1 (größer 0 und kleiner/gleich 1).

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius des Gefäßes in Millimetern, Wanddicke in Millimetern.
        """
        
        theta = np.linspace(0, 2*np.pi, 150)

        # wallThickness und radius ist in µm
        # wallThickness und radius in mm umrechnen
        wallThickness *= 0.001
        radius *= 0.001
        
        if lumFactor > 1:
            lumFactor = 1
        elif lumFactor < 0:
            lumFactor = 0.1

        # Querschnitt (Lumen)
        x = radius * np.cos(theta) * lumFactor
        y = radius * np.sin(theta) * lumFactor

        # Querschnitt (komplett)
        cs = radius + wallThickness

        x1 = cs * np.cos(theta)
        y1 = cs * np.sin(theta)

        # Durchmesser halbieren = Radius
        x /= 2
        y /= 2

        x1 /= 2
        y1 /= 2

        return x, y, x1, y1, radius, wallThickness

    def aorta(self, wallThickness=2000, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Aorta, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 2000 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Aorta in Millimetern, Wanddicke in Millimetern.
        """ 
    
        x, y, x1, y1, radius, wallThickness = self.vessel(self.aor_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness
    
    def arteries(self, wallThickness=1000, lumFactor=1):
        """_summary_
        Erzeugt ein Modell einer Arterie, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 1000 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Arterie in Millimetern, Wanddicke in Millimetern.
        """

        x, y, x1, y1, radius, wallThickness = self.vessel(self.art1_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def arterioles(self, wallThickness=30, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Arteriole, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 30 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Arteriole in Millimetern, Wanddicke in Millimetern.
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.art2_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def capillaries(self, wallThickness=1, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Kapillare, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 1 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Kapillare in Millimetern, Wanddicke in Millimetern.
        
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.cap_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def venules(self, wallThickness=2, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Venole, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 2 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Venole in Millimetern, Wanddicke in Millimetern.
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven1_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def veins(self, wallThickness=500, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Vene, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 500 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Vene in Millimetern, Wanddicke in Millimetern.
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven2_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def venaCava(self, wallThickness=1500, lumFactor=1):
        """_summary_
            Erzeugt ein Modell einer Vena cava, indem die vessel-Funktion mit spezifischen Maßen aufgerufen wird.

        Args:
            wallThickness (float, optional): Wanddicke in Mikrometern (µm), standardmäßig 1500 µm.
            lumFactor (float, optional): Faktor zur Skalierung des inneren Radius, standardmäßig 1.

        Returns:
            tuple: x und y Koordinaten des inneren Radius, x1 und y1 Koordinaten des äußeren Radius,
                Radius der Vena cava in Millimetern, Wanddicke in Millimetern.
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.vc_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness
    
    def vesselPlotter(self, lumFactor, lims=[]):
        """_summary_
        Erstellt Plots für verschiedene Gefäße des Körpers.

        Args:
            lumFactor (list): Liste von Faktoren zur Skalierung der inneren Radien für die verschiedenen Gefäße.
            lims (list, optional): Liste mit zwei Werten, um die Grenzen der Gefäß-Plots zu definieren. 
                                Standardmäßig leer ([]).

        Returns:
            None
        """

        fig = plt.figure(figsize=(12,6))
        plt.subplots_adjust(hspace=0.4)
        col = 4
        row = 2

        aorta = self.aorta(lumFactor=lumFactor[0])
        arteries = self.arteries(lumFactor=lumFactor[1])
        arterioles = self.arterioles(lumFactor=lumFactor[2])
        capillaries = self.capillaries(lumFactor=lumFactor[3])
        venules = self.venules(lumFactor=lumFactor[4])
        veins = self.veins(lumFactor=lumFactor[5])
        venaCava = self.venaCava(lumFactor=lumFactor[6])
        
        for i in range(1,8):
            fig.add_subplot(row, col, i)
            plt.grid(True)
            plt.tick_params(labelleft = False)
            plt.xlabel('mm')

            if i == 1:
                plt.plot(aorta[0],aorta[1], 'red', linewidth=1)
                plt.plot(aorta[2],aorta[3], 'black', linewidth=1)
                plt.title('Aorta')
            elif i == 2:
                plt.plot(arteries[0],arteries[1], 'red', linewidth=1)
                plt.plot(arteries[2],arteries[3], 'black', linewidth=1)
                plt.title('Arterien')
            elif i == 3:
                plt.plot(arterioles[0],arterioles[1], 'red', linewidth=1)
                plt.plot(arterioles[2],arterioles[3], 'black', linewidth=1)
                plt.title('Arteriole')
            elif i == 4:
                plt.plot(capillaries[0],capillaries[1], 'red', linewidth=1)
                plt.plot(capillaries[2],capillaries[3], 'black', linewidth=1)
                plt.title('Kapillare')
            elif i == 5:
                plt.plot(venules[0],venules[1], 'red', linewidth=1)
                plt.plot(venules[2],venules[3], 'black', linewidth=1)
                plt.title('Venole')
            elif i == 6:
                plt.plot(veins[0],veins[1], 'red', linewidth=1)
                plt.plot(veins[2],veins[3], 'black', linewidth=1)
                plt.title('Vene')
            elif i == 7:
                plt.plot(venaCava[0],venaCava[1], 'red', linewidth=1)
                plt.plot(venaCava[2],venaCava[3], 'black', linewidth=1)
                plt.title('V. cava')
            
            if len(lims) == 2:
                if lims[0] > 0:
                    lims[0] *= -1
                    
                plt.xlim(lims[0], lims[1])
                plt.ylim(lims[0], lims[1])
        plt.show()
    
    def resistance(self, lens):
        """_summary_
            Berechnet den Strömungswiderstand für gegebene Längen-Werte nach dem Hagen-Poiseuille-Gesetz und dem Ohm'schen Gesetz.

        Args:
            lens (Array): Array mit Längen-Werten der Gefäße in Millimetern.

        Returns:
            res (list): Liste mit den berechneten Strömungswiderständen in Pascal Sekunden pro Kubikmillimeter (Pa s / mm^3).
        """

        res = []
        radius = np.copy(self.radi) * 0.001

        for i in range(0, len(radius)):
            radius[i] *= self.lumFactor[i]
            res.append((8 * self.viscosity * lens) / (radius[i]**4 * np.pi))

        return res

    def parallelResistance(self, arr):
        """_summary_
            Berechnet den Gesamtwiderstand für parallel geschaltete Gefäße.

        Args:
            arr (array-like of float): Array, das die Widerstände der parallel geschalteten Gefäße enthält.

        Returns:
            pres (float): Gesamtwiderstand der parallel geschalteten Gefäße.
        """

        tmp = np.copy(arr)
        res = 1 / np.sum(1 / tmp)

        return res
    
    def serialResistance(self, arr):
        """_summary_
            Berechnet den Gesamtwiderstand für hintereinander geschaltete Gefäße.

        Args:
            arr (array-like of float): Array, das die Widerstände der hintereinander geschalteten Gefäße enthält.

        Returns:
            float: Gesamtwiderstand der hintereinander geschalteten Gefäße.
        """

        tmp = np.copy(arr)

        return np.sum(tmp)

    def vesselResistances(self, lens, nums):
        """_summary_
            Berechnet die Gesamtwiderstände für verschiedene Arten von Blutgefäßen basierend auf ihren Längen und Anzahlen.

        Args:
            lens (list of float): Liste mit Längen der verschiedenen Arten von Blutgefäßen.
            nums (list of int): Liste mit Anzahlen der verschiedenen Arten von Blutgefäßen.

        Returns:
            res (list of float): Liste mit den Gesamtwiderständen für jede Art von Blutgefäß.
        """

        types = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']
        aortaArr = []
        arteriesArr = []
        arteriolesArr = []
        capillariesArr = []
        venulesArr = []
        veinsArr = []
        venaCavaArr = []

        res = []

        aortaRes = arteriesRes = arteriolesRes = capillariesRes = venulesRes = veinsRes = venaCavaRes = 0
        aortaCom = arteriesCom = arteriolesCom = capillariesCom = venulesCom = veinsCom = venaCavaCom = 0

        for type in types:
            if type == 'aorta':
                for _ in range(0, nums[0]):
                    aortaRes = self.resistance(lens[0])[0]
                    aortaArr.append(aortaRes)

            elif type == 'arteries':
                for _ in range(0, nums[1]):
                    arteriesRes = self.resistance(lens[1])[1]
                    arteriesArr.append(arteriesRes)

            elif type == 'arterioles':
                for _ in range(0, nums[2]):
                    arteriolesRes = self.resistance(lens[2])[2]
                    arteriolesArr.append(arteriolesRes)
            
            elif type == 'capillaries':
                for _ in range(0, nums[3]):
                    capillariesRes = self.resistance(lens[3])[3]
                    capillariesArr.append(capillariesRes)
            
            elif type == 'venules':
                for _ in range(0, nums[4]):
                    venulesRes = self.resistance(lens[4])[4]
                    venulesArr.append(venulesRes)

            elif type == 'veins':
                for _ in range(nums[5]):
                    veinsRes = self.resistance(lens[5])[5]
                    veinsArr.append(veinsRes)
            
            elif type == 'venaCava':
                for _ in range(0, nums[6]):
                    venaCavaRes = self.resistance(lens[6])[6]
                    venaCavaArr.append(venaCavaRes)
        
        aortaCom = self.parallelResistance(aortaArr)
        arteriesCom = self.parallelResistance(arteriesArr) 
        arteriolesCom = self.parallelResistance(arteriolesArr)
        capillariesCom = self.parallelResistance(capillariesArr)
        venulesCom = self.parallelResistance(venulesArr)
        veinsCom = self.parallelResistance(veinsArr)
        venaCavaCom = self.parallelResistance(venaCavaArr)

        res = [aortaCom, arteriesCom, arteriolesCom, capillariesCom, venulesCom, veinsCom, venaCavaCom]
        
        return res
    
    def completeResistance(self, resis):
        """_summary_
            Berechnet den Gesamtwiderstand des Körpersystems basierend auf den Widerständen aller Gefäßarten.

        Args:
            resis (array-like): Array mit den Widerständen aller Gefäßarten.

        Returns:
            float: Gesamtwiderstand des Körpersystems.
        """

        resis = np.copy(resis)
        compRes = 0
        for i in range(0, len(resis)):
            compRes += resis[i]
        
        return compRes

    def normalizeResistance(self, resiArr):
        """_summary_
            Normalisiert die Widerstände, um die Werte auf den Bereich [0, 1] zu skalieren.

        Args:
            resiArr (array-like): Array mit den zu normalisierenden Widerstandswerten.

        Returns:
            list: Liste mit normalisierten Widerstandswerten im Bereich [0, 1].
        """

        min_val = np.min(resiArr)
        max_val = np.max(resiArr)

        range_min = 0
        range_max = 1

        res = []
        for val in resiArr:  
            norm = range_min + (val - min_val) * (range_max - range_min) / (max_val - min_val)
            res.append(norm)

        return res

    def resisPrinter(self, le, nu):
        """_summary_
            Gibt die Widerstände der verschiedenen Gefäßarten und den Gesamtwiderstand des Körpersystems aus.

        Args:
            le (array-like): Array mit den Längen der verschiedenen Gefäßarten.
            nu (array-like): Array mit den Anzahlen der verschiedenen Gefäßarten.
        
            Return:
                None
        """
        
        ty = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']
        print('######   Einzelwiderstände der verschiedenen Gefäßarten', '\n')
        resis = self.vesselResistances(le, nu)
        for i in range(0, len(resis)):
            print(ty[i], ': ', '{:e}'.format(resis[i]), 'Pa s / mm^3')

        print()
        print('######   Gesamtwiderstand', '\n')   
        print('{:e}'.format(self.completeResistance(resis)), 'Pa s / mm^3')
        print()
    
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
    
    def aortaPresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in der Aorta über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.
            Es wird überprüft, ob der Druck in der linken Herzkammer größer ist. In diesem Fall wird der Druck in der Aorta gleich dem Druck der linken Herzkammer gesetzt.
            
            Der berechnete Druck wird in self.aortaPressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """

        bp = BloodPressure()

        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.totalVolume, self.maxTime)
        h.leftVentricle()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[0] + 15

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[0]
        currentVolume = self.totalVolume
        
        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)
            
            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            radiusEffect = self.radi[0] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume
            
            self.aortaPressure[i] = self.pres0
            if h.bloodPressure_LV[i] > self.aortaPressure[i]:
                self.aortaPressure[i] = h.bloodPressure_LV[i] + volumeEffect + viskosityEffect - radiusEffect * 0.8
            
            self.aortaPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect #- 15 #- 5

    def arteriePresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in den Arterien über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.
            
            Der berechnete Druck wird in self.arteriePressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """

        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[1]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[1]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[1] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)
              
            self.arteriePressure[i] = self.aortaPressure[i] * 0.7#* 0.8
            self.arteriePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect #* 0.3

    def arteriolePresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in den Arteriolen über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.
            
            Der berechnete Druck wird in self.arteriolPressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """

        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[2]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[2]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[2] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)

            self.arteriolPressure[i] = self.arteriePressure[i] * 0.6 #* 0.5
            self.arteriolPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect - 5 #+ 10

    def capillarePresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
        Simuliert den Druckverlauf in den Kapillaren über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

        Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
        Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
        Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.
        
        Der berechnete Druck wird in self.capillarePressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """

        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[3]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[3]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[3] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)
            
            self.capillarePressure[i] = self.arteriolPressure[i] * 0.5
            self.capillarePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect - 6

    def venolePresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in den Venulen über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.

            Der berechnete Druck wird in self.venolePressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """
        
        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[4]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[4]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[4] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)
                       
            self.venolePressure[i] = self.capillarePressure[i] * 0.4
            self.venolePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect - 7
            
    def venePresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in den Venen über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.

            Der berechnete Druck wird in self.venePressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """
        
        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[5]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[5]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[5] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)

            self.venePressure[i] = self.venolePressure[i] * 0.3
            self.venePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect - 2
            
    def vCavaPresSim(self, le, nu, ctHR=[], newHR=[], ctVis=[], newVis=[], ctRadius=[], newRadius=[], ctVol=[], newVol=[]):
        """_summary_
            Simuliert den Druckverlauf in der Vena Cava über die Zeit unter Berücksichtigung verschiedener Parameteränderungen.

            Zuerst werden wichtige Einflussfaktoren auf den Blutdruck festgelegt. 
            Dann wird über die gesamte Zeit iteriert und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird die Grundstruktur der Blutdruckkurve aus der Klasse BloodPressure verwendet.

            Der berechnete Druck wird in self.vCavaPressure[i] gespeichert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list, optional): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list, optional): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list, optional): Zeitpunkte der Viskositätsänderungen.
            newVis (list, optional): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list, optional): Zeitpunkte der Radiusänderungen.
            newRadius (list, optional): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list, optional): Zeitpunkte der Volumenänderungen.
            newVol (list, optional): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """

        bp = BloodPressure()

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[6]

        currentHeartRate = self.heartRate
        currentViscosity = self.viscosity
        currentRadiusFactor = self.lumFactor[6]
        currentVolume = self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            currentHeartRate = self.updateParameter(t, ctHR, newHR, currentHeartRate)
            currentViscosity = self.updateParameter(t, ctVis, newVis, currentViscosity)
            currentRadiusFactor = self.updateParameter(t, ctRadius, newRadius, currentRadiusFactor)
            currentVolume = self.updateParameter(t, ctVol, newVol, currentVolume)

            viskosityEffect = currentViscosity / 100
            p1, p2 = bp.bpFunction(t, currentHeartRate)

            volumePressureConstant = 0.001
            volumeEffect = volumePressureConstant * currentVolume

            radiusEffect = self.radi[6] * 0.001 * currentRadiusFactor
            radiusEffect = np.log(radiusEffect)
            
            self.vCavaPressure[i] = self.venePressure[i] * 0.2
            self.vCavaPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect - 1

    def vesselSimulator(self, le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol):
        """_summary_
            Simuliert das gesamte Gefäßsystem durch Aufruf der entsprechenden Simulationsfunktionen für Aorta, Arterie, Arteriole, Kapillare,
                Venole, Vene und Vena Cava.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list): Zeitpunkte der Viskositätsänderungen.
            newVis (list): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list): Zeitpunkte der Radiusänderungen.
            newRadius (list): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list): Zeitpunkte der Volumenänderungen.
            newVol (list): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
        
        Returns:
            None
        """
        
        self.aortaPresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.arteriePresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.arteriolePresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.capillarePresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.venolePresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.venePresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)
        self.vCavaPresSim(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)

    def vpPlotter(self, le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol, ctEDV, newEDV, ctESV, newESV):
        """_summary_
            Simuliert das Herz und das Blutsystem über die Zeit und erstellt einen Plot der Druckwerte in verschiedenen Gefäßen.

        Args:
            le (array): Längen der verschiedenen Gefäßarten.
            nu (array): Anzahl der verschiedenen Gefäßarten.
            ctHR (list): Zeitpunkte der Herzfrequenzänderungen.
            newHR (list): Neue Werte der Herzfrequenz zu den Zeitpunkten ctHR.
            ctVis (list): Zeitpunkte der Viskositätsänderungen.
            newVis (list): Neue Werte der Viskosität zu den Zeitpunkten ctVis.
            ctRadius (list): Zeitpunkte der Radiusänderungen.
            newRadius (list): Neue Werte des Lumfaktors zu den Zeitpunkten ctRadius.
            ctVol (list): Zeitpunkte der Volumenänderungen.
            newVol (list): Neue Werte des Gesamtvolumens zu den Zeitpunkten ctVol.
            ctEDV (list): Zeitpunkte der EDV-Änderung.
            newEDV (list): Neue Werte des EDV zu den Zeitpunkten ctEDV.
            ctESV (list): Zeitpunkte der ESV-Änderung.
            newESV (list): Neue Werte des ESV zu den Zeitpunkten ctESV.
        
        Returns:
            None
        """
        
        plt.figure(figsize=(11, 7))
        
        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.totalVolume, self.maxTime)
        h.heartSimulation(ctEDV, newEDV, ctESV, newESV)

        self.vesselSimulator(le, nu, ctHR, newHR, ctVis, newVis, ctRadius, newRadius, ctVol, newVol)

        plt.plot(self.time, self.aortaPressure, label='Aorta Druck')
        plt.plot(self.time, self.arteriePressure, label='Arterie Druck')
        plt.plot(self.time, self.arteriolPressure, label='Arteriole Druck')
        plt.plot(self.time, self.capillarePressure, label='Kapillare Druck')
        plt.plot(self.time, self.venolePressure, label='Venole Druck')
        plt.plot(self.time, self.venePressure, label='Vene Druck')
        plt.plot(self.time, self.vCavaPressure, label='V. Cava Druck')

        plt.xlabel('Zeit (s)')
        plt.ylabel('mmHg')
        plt.title('Simulation des Gefäßsystem')
        plt.grid(True)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 9.5})
        plt.show()
    
    def getPressurs(self):
        """_summary_
            Gibt die Druckwerte aller Gefäßarten zurück.
        
        Args:
            None

        Returns:
            tuple: Tupel mit den Arrays der Druckwerte für Aorta, Arterie, Arteriole, Kapillare,
                Venole, Vene und Vena Cava.
        """
        
        return self.aortaPressure, self.arteriePressure, self.arteriolPressure, self.capillarePressure, self.venolePressure, self.venePressure, self.vCavaPressure