
import numpy as np
import matplotlib.pyplot as plt

class VascularSystem():

    def __init__(self, radi, viscocity):
        self.aor_rad = radi[0]      # aorta
        self.art1_rad = radi[1]     # arterie
        self.art2_rad = radi[2]     # arteriole
        self.cap_rad = radi[3]      # kapillare
        self.ven1_rad = radi[4]     # venole
        self.ven2_rad = radi[5]     # vene
        self.vc_rad = radi[6]       # v.cava
        self.viscocity = viscocity

    def vessel(self, radius, wallThickness, lumRadi=1):
        """_summary_
            Nimmt den Radius, wanddicke und Radius des Lumens, um Gefäße mit den entsprechenden Maßen
            zu erzeugen.
            lumRadi ist für die individuelle Anpassung des inneren Radius
            Maßeinheit µm wir aber in mm umgerechnet
        Args:
            radius (float): Radius eines Gefäß in µm
            wallThickness (float): Wanddicke in µm
            lumRadi (float): Radius des Lumen in µm

        Returns:
            
        """
        
        theta = np.linspace(0, 2*np.pi, 150)

        # wallThickness und radius ist in µm
        # wallThickness und radius in mm umrechnen
        wallThickness *= 0.001
        radius *= 0.001
        
        # Querschneitt (Lumen)
        x = radius * np.cos(theta) * lumRadi
        y = radius * np.sin(theta) * lumRadi

        # Querschnitt (komplett)
        cs = radius + wallThickness

        x1 = cs * np.cos(theta)
        y1 = cs * np.sin(theta)

        # Durchmesser halbieren
        x /= 2
        y /= 2

        x1 /= 2
        y1 /= 2

        return x, y, x1, y1, radius, wallThickness

    def aorta(self, wallThickness=2000, lumRadi=1):
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

        x, y, x1, y1, radius, wallThickness = self.vessel(self.aor_rad, wallThickness,lumRadi)
        return x, y, x1, y1, radius, wallThickness
    
    def arteries(self, wallThickness=1000, lumRadi=1):
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

        x, y, x1, y1, radius, wallThickness = self.vessel(self.art1_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness

    def arterioles(self, wallThickness=30, lumRadi=1):
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
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.art2_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness

    def capillaries(self, wallThickness=1, lumRadi=1):
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
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.cap_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness

    def venules(self, wallThickness=2, lumRadi=1):
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
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven1_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness

    def veins(self, wallThickness=500, lumRadi=1):
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
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven2_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness

    def venaCava(self, wallThickness=1500, lumRadi=1):
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
        
        x, y, x1, y1, radius, wallThickness = self.vessel(self.vc_rad, wallThickness, lumRadi)
        return x, y, x1, y1, radius, wallThickness
    
    def vesselPlotter(self, lims=[]):
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

        aorta = self.aorta()
        arteries = self.arteries()
        arterioles = self.arterioles()
        capillaries = self.capillaries()
        venules = self.venules()
        veins = self.veins()
        venaCava = self.venaCava()
        
        for i in range(1,8):
            fig.add_subplot(row, col, i)
            plt.grid(True)
            plt.tick_params(labelleft = False)

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
                plt.title('Kappilare')
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

    def setViscocity(self, val):
        """_summary_
            Legt die Viskositöt fest
        Args:
            val (float): Viskosität in Pa s (Pascal-Sekunde)
        """
        self.viscocity = val
    
    def resistance(self, lens, radius):
        """_summary_
            Helfer-Funktion
            Berechnet en Strömungswiderstand für gegebene Werte nach Hagen-Poiseuille-Gesetz und 
            umformung durch das Ohm'sche Gesetz
        Args:
            lens (Array): Längen-Werte in mm
            radius (Array): Werte für Radi in µm

        Returns:
            res (float): Strömungswiderstand in Pa s / mm^3 
        """

        res = (8 * self.viscocity * lens) / ((radius)**4 * np.pi)
        return res

    def parallelResistance(self, arr):
        """_summary_

        Args:
            arr (Array, float): Beinhaltet die Gefäßwiderstände von parallel geschalteten Gefäßen

        Returns:
            pres (float): Gesamtwiderstand von parallel geschalteten Gefäßen
        """
        tmp = np.copy(arr)
        for i in range(0,len(tmp)):
            tmp[i] = 1 / tmp[i]

        res = np.sum(tmp)
        pRes = 1/res
        return pRes
    
    def serialResistance(self, arr):
        return np.sum(arr)

    def vesselResistances(self, types, lens, radius, nums):
        """_summary_

        Args_:
            types: (Array, String): Mit String für jede Art von Gefäß
            lens: (Array, float): Mit Längen-Werte für jede Art von Gefäß
            radius: (Array, float): Array mit Werte für den Radius fpr jede Art von Gefäß
            nums: (Array, int): Array mit Wertden für die Anzahl von jeder Art von Gefäß

        Returns:
            res (Array, float): Array, wo jeder Wert jeweils den parallelen Widerstand entspricht
        """

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
        for i in range(0,len(radius)):
            radius[i] *= 0.001

        for type in types:
            if type == 'aorta':
                for i in range(0,nums[0]):
                    aortaRes = self.resistance(lens[0], radius[0])
                    aortaArr.append(aortaRes)

            elif type == 'arteries':
                for i in range(0,nums[1]):
                    arteriesRes = self.resistance(lens[1], radius[1])
                    arteriesArr.append(arteriesRes)

            elif type == 'arterioles':
                for i in range(nums[2]):
                    arteriolesRes = self.resistance(lens[2], radius[2])
                    arteriolesArr.append(arteriolesRes)
            
            elif type == 'capillaries':
                for i in range(nums[3]):
                    capillariesRes = self.resistance(lens[3], radius[3])
                    capillariesArr.append(capillariesRes)
            
            elif type == 'venules':
                for i in range(nums[4]):
                    venulesRes = self.resistance(lens[4], radius[4])
                    venulesArr.append(venulesRes)

            elif type == 'veins':
                for i in range(nums[5]):
                    veinsRes = self.resistance(lens[5], radius[5])
                    veinsArr.append(veinsRes)
            
            elif type == 'venaCava':
                for i in range(nums[6]):
                    venaCavaRes = self.resistance(lens[6], radius[6])
                    venaCavaArr.append(venaCavaRes)
        
        aortaCom = self.parallelResistance(aortaArr)
        arteriesCom = self.parallelResistance(arteriesArr) 
        arteriolesCom = self.parallelResistance(arteriolesArr)
        capillariesCom = self.parallelResistance(capillariesArr)
        venulesCom = self.parallelResistance(venulesArr)
        veinsCom = self.parallelResistance(veinsArr)
        venaCavaCom = self.parallelResistance(venaCavaArr)

        #print('1', aortaCom, 'mm^3 / Pa s')
        res = [aortaCom, arteriesCom, arteriolesCom, capillariesCom, venulesCom, veinsCom, venaCavaCom]
        return res
    
    def completeResistance(self, resis):
        compRes = 0
        for i in range(0,len(resis)):
            compRes += resis[i]
        return compRes

"""
Parameter (Radien, in µm): 
    1. aorta
    2. arteries
    3. arterioles
    4. capillaries
    5. venules
    6. veins
    7. venaCava 
"""

radi = [20000, 4000, 20, 8, 20, 5000, 30000]
viscocity = 1
vs = VascularSystem(radi, viscocity)

lims = [-20, 20]
vs.vesselPlotter(lims)

nums = [1, 2, 4, 16, 4, 2, 1]
lens = [200, 150, 100, 50, 100, 150, 300] # in mm
type = ['aorta', 'arteries', 'arterioles', 'capillaries', 'venules', 'veins', 'venaCava']

resis = vs.vesselResistances(type, lens, radi, nums)
print(vs.completeResistance(resis), 'mm^3 / Pa s')

#plt.show()