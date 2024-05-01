
import numpy as np
import matplotlib.pyplot as plt

class VascularSystem():

    def __init__(self):
        pass

    def aorta(self, radius, wallThickness=2000, number=1):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness
    
    def arteries(self, radius, wallThickness=1000):
        """_summary_

        Args:
            radius (_type_): _description_
            wallThickness (int, optional): _description_. Defaults to 1000.
        Returns:

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

        return x, y, x1, y1, radius, wallThickness

    def arterioles(self, radius, wallThickness=30):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness

    def capillaries(self, radius, wallThickness=1):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness

    def venules(self, radius, wallThickness=2):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness

    def veins(self, radius, wallThickness=500):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness

    def venaCava(self, radius, wallThickness=1500, number=1):
        """_summary_
            
        Args:
            radius (_type_): _description_
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

        return x, y, x1, y1, radius, wallThickness
    
    def normVessels(self):
        pass



vs = VascularSystem()
aorta = vs.aorta(20000)
arteries = vs.arteries(4000)
arterioles = vs.arterioles(20)
capillaries = vs.capillaries(8)
venules = vs.venules(20)
veins = vs.veins(5000)
venaCava = vs.venaCava(30000)

fig, axs = plt.subplots(2,4)
fig.set_figheight(6)
fig.set_figwidth(12)

axs[0,0].plot(aorta[0],aorta[1])
axs[0,0].plot(aorta[2],aorta[3])
axs[0,0].grid(True)
axs[0,0].tick_params(labelleft = False)
axs[0,0].set_xlim(-32,32)
axs[0,0].set_ylim(-32,32)
axs[0,0].title.set_text('Aorta')

axs[0,1].plot(arteries[0], arteries[1])
axs[0,1].plot(arteries[2], arteries[3])
axs[0,1].grid(True)
axs[0,1].tick_params(labelleft = False)
axs[0,1].set_xlim(-32,32)
axs[0,1].set_ylim(-32,32)
axs[0,1].title.set_text('Arterie')

axs[0,2].plot(arterioles[0], arterioles[1])
axs[0,2].plot(arterioles[2], arterioles[3])
axs[0,2].grid(True)
axs[0,2].tick_params(labelleft = False)
axs[0,2].set_xlim(-32,32)
axs[0,2].set_ylim(-32,32)
axs[0,2].title.set_text('Arteriole')

axs[0,3].plot(capillaries[0], capillaries[1])
axs[0,3].plot(capillaries[2], capillaries[3])
axs[0,3].grid(True)
axs[0,3].tick_params(labelleft = False)
axs[0,3].set_xlim(-32,32)
axs[0,3].set_ylim(-32,32)
axs[0,3].title.set_text('Kapillare')

axs[1,0].plot(venules[0], venules[1])
axs[1,0].plot(venules[2], venules[3])
axs[1,0].grid(True)
axs[1,0].tick_params(labelleft = False)
axs[1,0].set_xlim(-32,32)
axs[1,0].set_ylim(-32,32)
axs[1,0].title.set_text('Venole')

axs[1,1].plot(veins[0], veins[1])
axs[1,1].plot(veins[2], veins[3])
axs[1,1].grid(True)
axs[1,1].tick_params(labelleft = False)
axs[1,1].set_xlim(-32,32)
axs[1,1].set_ylim(-32,32)
axs[1,1].title.set_text('Vene')

axs[1,2].plot(venaCava[0], venaCava[1])
axs[1,2].plot(venaCava[2], venaCava[3])
axs[1,2].grid(True)
axs[1,2].tick_params(labelleft = False)
axs[1,2].set_xlim(-32,32)
axs[1,2].set_ylim(-32,32)
axs[1,2].title.set_text('V. cava')


plt.show()