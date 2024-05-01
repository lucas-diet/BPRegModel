
import numpy as np
import matplotlib.pyplot as plt

class VascularSystem():

    def __init__(self, aor_rad, art1_rad, art2_rad,cap_rad, ven1_rad, ven2_rad, vc_rad):
        self.aor_rad = aor_rad
        self.art1_rad = art1_rad
        self.art2_rad = art2_rad
        self.cap_rad = cap_rad
        self.ven1_rad = ven1_rad
        self.ven2_rad = ven2_rad
        self.vc_rad = vc_rad

    def vessel(self, radius, wallThickness):
        """_summary_
        
        Args:
            radius (_type_): _description_
            wallThickness (_type_): _description_

        Returns:
            _type_: _description_
        """
        theta = np.linspace(0, 2*np.pi, 150)

        # wallThickness und radius ist in µm
        # wallThickness und rqadius in mm umrechnen
        wallThickness *= 0.001
        radius *= 0.001
        
        # Querschneitt (Lumen)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta) 

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

    def aorta(self, wallThickness=2000, number=1):
        """_summary_
            
        Args:
            wallThickness (int, optional):
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """

        x, y, x1, y1, radius, wallThickness = self.vessel(self.aor_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness
    
    def arteries(self, wallThickness=1000):
        """_summary_

        Args:
            wallThickness (int, optional):
        Returns:

        """

        #number = self.aorta()^2
        x, y, x1, y1, radius, wallThickness = self.vessel(self.art1_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness

    def arterioles(self, wallThickness=30):
        """_summary_
            
        Args:
            wallThickness (int, optional):
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        x, y, x1, y1, radius, wallThickness = self.vessel(self.art2_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness

    def capillaries(self, wallThickness=1):
        """_summary_
            
        Args:
            wallThickness (int, optional):
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        x, y, x1, y1, radius, wallThickness = self.vessel(self.cap_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness

    def venules(self, wallThickness=2):
        """_summary_
            
        Args:
            wallThickness (int, optional):
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven1_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness

    def veins(self, wallThickness=500):
        """_summary_
            
        Args:
            wallThickness (int, optional):
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        x, y, x1, y1, radius, wallThickness = self.vessel(self.ven2_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness

    def venaCava(self, wallThickness=1500, number=1):
        """_summary_
            
        Args:
            wallThickness (int, optional): _description_. Defaults to 2000.
            number (int, optional): _description_. Defaults to 1.
        Returns:
            x
            y
            x1
            y1
            radius
            wallThickness 
        """
        x, y, x1, y1, radius, wallThickness = self.vessel(self.vc_rad, wallThickness)
        return x, y, x1, y1, radius, wallThickness
    
    def vesselResistance(self):
        pass

    
    def vesselPlotter(self, lims=[]):
        fig = plt.figure(figsize=(12,6))
        plt.subplots_adjust(hspace=0.4)
        col = 4
        row = 2
        
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

"""
Parameter (Radien): 
    1. aorta
    2. arteries
    3. arterioles
    4. capillaries
    5. venules
    6. veins
    7. venaCava 
""" 
vs = VascularSystem(20000, 4000, 20, 8, 20, 5000, 30000)
aorta = vs.aorta()
arteries = vs.arteries()
arterioles = vs.arterioles()
capillaries = vs.capillaries()
venules = vs.venules()
veins = vs.veins()
venaCava = vs.venaCava()

lims = [-20, 20]
vs.vesselPlotter(lims)

plt.show()