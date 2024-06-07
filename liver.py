
#TODO: Noch in das System einbinden!!

from sensor import *

class Liver():
    
    def __init__(self, viscosity, maxTime, dt=0.01):
        self.viscosity = viscosity
        self.time = np.arange(0, maxTime, dt)
        self.viscosity_history = []  # Liste zum Speichern der Viskositätswerte

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
        if self.viscosity + inc > 100:
            self.viscosity = 100
        
        else:
            self.viscosity += inc
            self.viscosity = round(self.viscosity, 2)

    def decreaseViscosity(self, dec):
        """_summary_
            Nimmt einen Wert und reduziert die Viskostät um diesen.
        Args:
            dec (float): Wert um den reduziert werden soll
        """

        #if self.viscosity > 100:
        #    pass

        self.viscosity -= dec
        self.viscosity = round(self.viscosity, 2)
    
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
        if interval > 0:
            num_changes = 0
            for i in range(interval, len(self.time), interval):
                if prop == 'inc':
                    self.increaseViscosity(change)
                    num_changes += 1
                    #print(i, f"Time: {self.time[i]}, Viskosität reduziert zu: {self.viscosity}")
            
                elif prop == 'dec':
                    self.decreaseViscosity(change)
                    num_changes += 1
                    #print(i, f"Time: {self.time[i]}, Viskosität reduziert zu: {self.viscosity}")

                self.viscosity_history.append([self.viscosity, self.time[i]])
            #print(f"Total number of changes: {num_changes}")

            return self.viscosity