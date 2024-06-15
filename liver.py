
#TODO: Noch in das System einbinden!!

from sensor import *

class Liver():
    
    def __init__(self, viscosity, maxTime, dt=0.01):
        self.viscosity = viscosity
        self.time = np.arange(0, maxTime, dt)
        self.viscosity_history = []  # Liste zum Speichern der Viskositätswerte

    def getViscosity(self):
        """_summary_
            Gibt den aktuellen Wert der Viskosität zurück.
        
        Args:
            None
        
        Returns:
            float: Der in self.viscosity gespeicherte Wert der Viskosität.
        """

        return self.viscosity

    def setViscosity(self, vis):
        """_summary_
            Legt den Wert für die Viskosität fest.
    
        Args:
            vis (float): Der neue Wert für die Viskosität.
        
        Returns:
            None
        """

        self.viscosity = vis
    
    def increaseViscosity(self, inc):
        """_summary_
            Erhöht die Viskosität um den angegebenen Wert.
    
        Args:
            inc (float): Wert, um den die Viskosität erhöht werden soll.
        
        Returns:
            None
        """
        if self.viscosity + inc > 100:
            self.viscosity = 100
        
        else:
            self.viscosity += inc
            self.viscosity = round(self.viscosity, 2)

    def decreaseViscosity(self, dec):
        """_summary_
            Reduziert die Viskosität um den angegebenen Wert.
    
        Args:
            dec (float): Wert, um den die Viskosität reduziert werden soll.
        
        Returns:
            None
        """

        #if self.viscosity > 100:
        #    pass

        self.viscosity -= dec
        self.viscosity = round(self.viscosity, 2)
    
    def viscositySimulate(self, prop, interval, change):
        """_summary_
            Simuliert die Veränderung der Viskosität über die Zeit.
        
            Überprüft den Wert von 'prop' und verändert entsprechend nach 'interval' und 'change' die Viskosität.
        
        Args:
            prop (String): 'inc' zum Erhöhen und 'dec' zum Reduzieren der Viskosität.
            interval (int): Zeitintervall, in dem die Viskosität geändert wird.
            change (float): Wert, um den die Viskosität verändert werden soll.

        Returns:
            self.viscosity (float): Aktueller Wert der Viskosität nach den Änderungen.
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