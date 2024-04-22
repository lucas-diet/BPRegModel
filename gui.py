
from tkinter import *

class GuiApp():
    def __init__(self, master):
        self.master = master
        master.title('BloodPressureSim')
        master.geometry('800x900')

   




if __name__ == '__main__':
    root = Tk()
    app = GuiApp(root)
    root.mainloop()
    

