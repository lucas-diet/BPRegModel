
#TODO: Radius über die Zeit manipulieren können
#TODO: Leber integrieren -> in die Kapillaren integiert. Soll ich diese auch in andere Gefäße intigieren?

import numpy as np
import matplotlib.pyplot as plt

from heart import Heart
from bloodPressure import BloodPressure
from liver import Liver

class BodySystem():

    def __init__(self, radi, lumFactor, viscosity, heartRate, strokeVolume, edv, esv, pres0, totalVolume, maxTime, dt=0.01):
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
            Nimmt den Radius, wanddicke und Radius des Lumens, um Gefäße mit den entsprechenden Maßen
            zu erzeugen.
            lumRadi ist für die individuelle Anpassung des inneren Radius
            Maßeinheit µm wir aber in mm umgerechnet
        Args:
            radius (float): Radius eines Gefäß in µm
            wallThickness (float): Wanddicke in µm
            lumRadi (float): Faktor, um inneren Radius zu skalieren -> > 0 und <= 1

        Returns:
            
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
            Nimmt die vessel-Funktion mit den Maßen für eine Aorta und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """

        x, y, x1, y1, radius, wallThickness = self.vessel(self.aor_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness
    
    def arteries(self, wallThickness=1000, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine Arterie und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """

        x, y, x1, y1, radius, wallThickness = self.vessel(self.art1_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def arterioles(self, wallThickness=30, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine Arteriole und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.art2_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def capillaries(self, wallThickness=1, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine Kapillare und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.cap_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def venules(self, wallThickness=2, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine Venole und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven1_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def veins(self, wallThickness=500, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine Vene und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven2_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness

    def venaCava(self, wallThickness=1500, lumFactor=1):
        """_summary_
            Nimmt die vessel-Funktion mit den Maßen für eine V.cava und erzeugt das entsprechende Gefäß.
        Args:
            wallThickness (float, optional): Wanddicke in µm
            lumRadi (float, optional): Innerer Radius in µm
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.vc_rad, wallThickness, lumFactor)
        return x, y, x1, y1, radius, wallThickness
    
    def vesselPlotter(self, lumFactor, lims=[]):
        """_summary_
            Funktion, um die Erzeugen Maße für die Gefäße zu plotten
        Args:
            lims (list, optional): Ist ein Array, was zwei Werte beinhalten soll, um die 
             Grenzen für die Gefäß-Plots zu definieren. Defaults = [].
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
            Helfer-Funktion
            Berechnet den Strömungswiderstand für gegebene Werte nach Hagen-Poiseuille-Gesetz und 
            umformung durch das Ohm'sche Gesetz
        Args:
            lens (Array): Längen-Werte in mm
            radius (Array): Werte für Radi in µm

        Returns:
            res (float): Strömungswiderstand in Pa s / mm^3 
        """
        res = []
        radius = np.copy(self.radi) * 0.001

        for i in range(0, len(radius)):
            radius[i] *= self.lumFactor[i]
            res.append((8 * self.viscosity * lens) / (radius[i]**4 * np.pi))

        return res

    def parallelResistance(self, arr):
        """_summary_
            Kopiert den Inhalt des übergebenen Arrays und berechnet dann den parallelen Widerstand.
        Args:
            arr (Array, float): Beinhaltet die Gefäßwiderstände von parallel geschalteten Gefäßen

        Returns:
            pres (float): Gesamtwiderstand von parallel geschalteten Gefäßen
        """
        tmp = np.copy(arr)
        res = 1 / np.sum(1 / tmp)

        return res
    
    def serialResistance(self, arr):
        """_summary_
            Berechnet Widerstände von Gefäßen, die hintereinander geschaltet sind.
        Args:
            arr (_type_): Beinhaltet 

        Returns:
            _type_: _description_
        """
        tmp = np.copy(arr)

        return np.sum(tmp)

    def vesselResistances(self, lens, nums):
        """_summary_

        Args_:
            types: (Array, String): Mit String für jede Art von Gefäß
            lens: (Array, float): Mit Längen-Werte für jede Art von Gefäß
            radius: (Array, float): Array mit Werte für den Radius fpr jede Art von Gefäß
            nums: (Array, int): Array mit Wertden für die Anzahl von jeder Art von Gefäß

        Returns:
            res (Array, float): Array, wo jeder Wert jeweils den parallelen Widerstand entspricht
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
                for i in range(0, nums[0]):
                    aortaRes = self.resistance(lens[0])[0]
                    aortaArr.append(aortaRes)

            elif type == 'arteries':
                for i in range(0, nums[1]):
                    arteriesRes = self.resistance(lens[1])[1]
                    arteriesArr.append(arteriesRes)

            elif type == 'arterioles':
                for i in range(0, nums[2]):
                    arteriolesRes = self.resistance(lens[2])[2]
                    arteriolesArr.append(arteriolesRes)
            
            elif type == 'capillaries':
                for i in range(0, nums[3]):
                    capillariesRes = self.resistance(lens[3])[3]
                    capillariesArr.append(capillariesRes)
            
            elif type == 'venules':
                for i in range(0, nums[4]):
                    venulesRes = self.resistance(lens[4])[4]
                    venulesArr.append(venulesRes)

            elif type == 'veins':
                for i in range(nums[5]):
                    veinsRes = self.resistance(lens[5])[5]
                    veinsArr.append(veinsRes)
            
            elif type == 'venaCava':
                for i in range(0, nums[6]):
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
            Berechnet den kompletten Widerstand des Körpersystem
        Args:
            resis (array): Beinhaltet Widerstände aller Gefäßarten

        Returns:
            comRes (float): Kompletter Widerstand 
        """
        resis = np.copy(resis)
        compRes = 0
        for i in range(0, len(resis)):
            compRes += resis[i]
        
        return compRes

    def normalizeResistance(self, resiArr):
        """_summary_
            Soll die Widerstände normalisieren, damit die Werte nicht mehr so extrem größ sind.
        Args:
            resi (_type_): _description_

        Returns:
            _type_: _description_
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
            In dieser Funktion werden die jeweiligen Funktionen aufgerufen, um die Widerstände der Gefäße auszugeben. 
        Args:
            le (array): Ein Array, welches die Längen der verschiedenen Gefäßarten besitzt
            nu (arary): Ein Array, welche die Anzahl der veschiedenen Gefäßarten besitzt
        """
        #bs = BodySystem(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.maxTime)
        ty = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']
        print('######   Einzelwiderstände der verschiedenen Gefäßarten', '\n')
        resis = self.vesselResistances(le, nu)
        for i in range(0, len(resis)):
            print(ty[i], ': ', '{:e}'.format(resis[i]), 'Pa s / mm^3')

        print()
        print('######   Gesamtwiderstand', '\n')   
        print('{:e}'.format(self.completeResistance(resis)), 'Pa s / mm^3')
        print()

    def findIndex(self, arr, val):
        idx = None
        for i in range(0, len(arr)):
            if arr[i] == val:
                idx = i
                break
        
        return idx
    
    def aortaPresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Es wird überprüft, ob der Druck in der linken Herzkammer größer ist, in diesem Fall soll der Druck in der 
            Aorta gleich dem Druck der linken Herzkammer sein.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.aortaPressure[i] gespecihert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.totalVolume, self.maxTime)
        h.leftVentricle()

        radiusEffect =  self.radi[0] * 0.001
        radiusEffect *= self.lumFactor[0]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[0] + 15

        viskosityEffect = self.viscosity / 100
        
        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]
                         
            p1, p2 = bp.bpFunction(t, self.heartRate)          
            self.aortaPressure[i] = self.pres0
 
            if h.bloodPressure_LV[i] > self.aortaPressure[i]:
                self.aortaPressure[i] = h.bloodPressure_LV[i] + volumeEffect + viskosityEffect
            
            self.aortaPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect

    def arteriePresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.arteriePressure[i] gespecihert.

        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        radiusEffect = self.radi[1] * 0.001
        radiusEffect *= self.lumFactor[1]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[1]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)
            
              
            self.arteriePressure[i] = self.aortaPressure[i] * 0.8
            self.arteriePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect #* 0.3

    def arteriolePresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.arteriolPressure[i] gespeichert.
        
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        radiusEffect = self.radi[2] * 0.001
        radiusEffect *= self.lumFactor[2]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[2]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)

            self.arteriolPressure[i] = self.arteriePressure[i] * 0.5
            self.arteriolPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect #+ 10

    def capillarePresSim(self, le, nu, prop, interval, change=0):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            
            Hier wird je nach übergebenen Parametern die Viskosität noch beeinflusst. Wenn 'change' == 0, dann wird nicht vereändert
            Wenn change != 0, dann wird verändert.
            
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.capillarePressure[i] gespeichert.
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
            prop (String): 'inc' zum erhöhen; 'dec' zum reduzieren
            interval (int): Zeitpunkte wo immer eine Anpassung geschehene soll
            change (float): Wert um den Viskosität verändert werden soll; Wenn == 0, dann geschieht keine Veränderung
        """
        bp = BloodPressure()

        radiusEffect = self.radi[3] * 0.001
        radiusEffect *= self.lumFactor[3]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[3]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)
            
            self.capillarePressure[i] = self.arteriolPressure[i] * 0.5
            self.capillarePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect

    def venolePresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.venolePressure[i] gespeichert.
        
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        radiusEffect = self.radi[4] * 0.001
        radiusEffect *= self.lumFactor[4]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[4]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)
                       
            self.venolePressure[i] = self.capillarePressure[i] * 0.4
            self.venolePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect + 5
            
    def venePresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.venePressure[i] gespeichert.
        
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        radiusEffect = self.radi[5] * 0.001
        radiusEffect *= self.lumFactor[5]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[5]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)
            

            self.venePressure[i] = self.venolePressure[i] * 0.3
            self.venePressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect  - radiusEffect + 3
            
    def vCavaPresSim(self, le, nu):
        """_summary_
            Zuerst werdne die wichtigen Faktoren festgelegt die den Blutdruck beeinflussen festgelegt.

            Dann wird über die gemsante Zeit gelaufen und der Blutdruck zu jedem Zeitpunkt berechnet.
            Dafür wird sich die Grundstruktur (x * sin(...) + y * sin(..)) der Kurve aus dem Programm bloodPressure.py geholt.
            Und zu letzt wird dann der Druck zu jedem Punkt i in self.vCavaPressure[i] gespeichert.
        
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
        """
        bp = BloodPressure()

        radiusEffect = self.radi[6] * 0.001
        radiusEffect *= self.lumFactor[6]
        radiusEffect = np.log(radiusEffect) * 0.3

        resis = self.vesselResistances(le, nu)
        resisEffect = self.normalizeResistance(resis)[6]

        viskosityEffect = self.viscosity / 100

        volumePressureConstant = 0.01
        volumeEffect = volumePressureConstant * self.totalVolume

        for i in range(0, len(self.time)):
            t = self.time[i]

            p1, p2 = bp.bpFunction(t, self.heartRate)
            
            self.vCavaPressure[i] = self.venePressure[i] * 0.2
            self.vCavaPressure[i] += resisEffect * (p1 + p2) + volumeEffect + viskosityEffect - radiusEffect

    def vesselSimulator(self, le, nu, prop, interval, change):
        """_summary_
            Ruft einfach alle Funktionen auf, um so dann das Gefäßsystem zu simulieren.
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
            prop (String): 'inc' zum erhöhen und 'dec' zum reduzieren der Viskosität
            interval (int): Zeitpunkte wo Viskosität verändert wird.
            change (float):Wert um den Viskosität verändert werden soll
        """
        self.aortaPresSim(le, nu)
        self.arteriePresSim(le, nu)
        self.arteriolePresSim(le, nu)
        self.capillarePresSim(le, nu, prop, interval, change)
        self.venolePresSim(le, nu)
        self.venePresSim(le, nu)
        self.vCavaPresSim(le, nu)

    def vpPlotter(self, le, nu, prop, interval, change):
        """_summary_
            Simuliert das Herz, um dann das Blutsystem zu simulieren. Simulation wird dann geplottet, also
            der Druck in jedem Gefäß über die Zeit.
        Args:
            le (array): Längen der verschiedenen Gefäßarten
            nu (array): Anzahl der verschiedenen Gefäßarten
            prop (String): 'inc' zum erhöhen und 'dec' zum reduzieren der Viskosität
            interval (int): Zeitpunkte wo Viskosität verändert wird.
            change (float):Wert um den Viskosität verändert werden soll
        """
        plt.figure(figsize=(11, 7))
        
        h = Heart(self.radi, self.viscosity, self.heartRate, self.strokeVolume, self.edv, self.esv, self.pres0, self.totalVolume, self.maxTime)
        h.heartSimulation()

        self.vesselSimulator(le, nu, prop, interval, change)

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
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=7, prop={'size': 8.5})
        plt.show()
    
    def getPressurs(self):
        """_summary_
            Es werden alle Gefäßarten zurückgeliefert, mit ihren Werten.
        Returns:
            _type_: Alle Gefäßarten
        """
        return self.aortaPressure, self.arteriePressure, self.arteriolPressure, self.capillarePressure, self.venolePressure, self.venePressure, self.vCavaPressure