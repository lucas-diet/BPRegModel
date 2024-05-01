
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

    def aorta(self, wallThickness=2000, number=1):
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
        radius = self.aor_rad
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
    
    def arteries(self, wallThickness=1000):
        """_summary_

        Args:
            wallThickness (int, optional): _description_. Defaults to 1000.
        Returns:

        """
        #number = self.aorta()^2
        radius = self.art1_rad

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

    def arterioles(self, wallThickness=30):
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
        radius = self.art2_rad
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

    def capillaries(self, wallThickness=1):
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
        radius = self.cap_rad
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

    def venules(self, wallThickness=2):
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
        radius = self.ven1_rad
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

    def veins(self, wallThickness=500):
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
        radius = self.ven2_rad
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
        radius = self.vc_rad
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
    
    def plotter(self, lims=[]):
        fig, axs = plt.subplots(2,4)
        fig.set_figheight(6)
        fig.set_figwidth(12)
        
        for i in range(0, 4):
            for j in range(0, 2):
                if i == 0 and j == 0:
                    axs[j,i].plot(aorta[0],aorta[1])
                    axs[j,i].plot(aorta[2],aorta[3])
                    axs[j,i].title.set_text('Aorta')
                
                elif i == 1 and j == 0:
                    axs[j,i].plot(arteries[0],arteries[1])
                    axs[j,i].plot(arteries[2],arteries[3])
                    axs[j,i].title.set_text('Arterien')

                elif i == 2 and j == 0:
                    axs[j,i].plot(arterioles[0],arterioles[1])
                    axs[j,i].plot(arterioles[2],arterioles[3])
                    axs[j,i].title.set_text('Arteriole')
                
                elif i == 3 and j == 0:
                    axs[j,i].plot(capillaries[0],capillaries[1])
                    axs[j,i].plot(capillaries[2],capillaries[3])
                    axs[j,i].title.set_text('Kappilare')
                
                elif i == 0 and j == 1:
                    axs[j,i].plot(venules[0],venules[1])
                    axs[j,i].plot(venules[2],venules[3])
                    axs[j,i].title.set_text('Venole')

                elif i == 1 and j == 1:
                    axs[j,i].plot(veins[0],veins[1])
                    axs[j,i].plot(veins[2],veins[3])
                    axs[j,i].title.set_text('Vene')
                
                elif i == 2 and j == 1:
                    axs[j,i].plot(venaCava[0],venaCava[1])
                    axs[j,i].plot(venaCava[2],venaCava[3])
                    axs[j,i].title.set_text('V. cava')
                
                if len(lims) == 2:
                    if lims[0] > 0:
                        lims[0] *= -1
                    
                    axs[j,i].set_xlim(lims[0], lims[1])
                    axs[j,i].set_ylim(lims[0], lims[1])

                axs[j,i].grid(True)
                axs[j,i].tick_params(labelleft = False)

                    


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
vs.plotter(lims)

plt.show()