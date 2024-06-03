
#TODO: Noch in das System einbinden!!

from sensor import *

class Liver():
    
    def __init__(self, viscosity, maxTime, dt=0.01):
        self.viscosity = viscosity
        self.time = np.arange(0, maxTime, dt)

    def getViscosity(self):
        """_summary_
            Gibt den Wert der Viskosität zurück
        Returns:
            self.viscosity (float): 
        """
        return self.viscosity

    def setViscosity(self, vis):
        """_summary_
            Legt den Wert für die Viskosität fest
        Args:
            vis (float): Wert für die Viskosität
        """
        self.viscosity = vis
    
    def increaseViscosity(self, inc):
        """_summary_
            Nimmt einen Wert und erhöt die Viskostät um diesen.
        Args:
            inc (float): Wert, um den die Viskosität erhöht werden soll
        """
        self.viscosity += inc
        self.viscosity = round(self.viscosity, 2)
        #if self.viscosity <= 0:
        #    self.viscosity = 1
        #elif self.viscosity >= 100:
        #    self.viscosity = 100

    def decreaseViscosity(self, dec):
        """_summary_
            Nimmt einen Wert und reduziert die Viskostät um diesen.
        Args:
            dec (float): Wert um den reduziert werden soll
        """
        self.viscosity -= dec
        self.viscosity = round(self.viscosity, 2)
        #if self.viscosity <= 0:
        #    self.viscosity = 1
        #elif self.viscosity >= 100:
        #    self.viscosity = 100
    
    def viscositySimulate(self, prop, interval, change):
        """_summary_
            Überprüft den Wert von 'prop' und verändert dann entsprechend nach 'interval' und 'change' die 
            Viskosität.
        Args:
            prop (String): 'inc' zum erhöhen und 'dec' zum reduzieren der Viskosität
            interval (int): Zeitpunkte wo Viskosität verändert wird.
            change (float):Wert um den Viskosität verändert werden soll

        Returns:
           self.viscosity (float): Wert für die Viskostät
        """
        if interval != 0:
            if prop == 'inc':
                for i in range(interval, len(self.time), interval):
                    self.increaseViscosity(change)
                    #print(f"Time: {self.time[i]}, Viskosität erhöht zu: {self.viscosity}")
                    return self.viscosity

            elif prop == 'dec':
                for i in range(interval, len(self.time), interval):
                    self.decreaseViscosity(change)
                    #print(f"Time: {self.time[i]}, Viskosität reduziert zu: {self.viscosity}")
                    return self.viscosity
        
        else:
            pass