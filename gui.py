
from tkinter import *

class GuiApp():
    def __init__(self, master):
        self.master = master
        master.title('Blood Pressure Simulator')
        master.geometry('350x600')

        self.duration_holder = 'duration'
        self.heartRate_holder = 'heart rate'

        #self.placeholders = {
        #    'duration': 'duration',
        #    'heartRate': 'heart rate',
        #    'systolic': 'systolic'}
        
        self.duration_label = Label(master, text='duration:', width=12)
        self.duration_label.place(x=5,y=10)

        self.duration_input = Entry(master, width=10, bg='white', fg='black')
        self.duration_input.place(x=150,y=10)

        self.heartRate_lable = Label(master, text='heart rate:', width=12)
        self.heartRate_lable.place(x=5,y=50)

        self.heartRate_input = Entry(master, width=10, bg='white', fg='black')
        self.heartRate_input.place(x=150, y=50)

        self.systolic_label = Label(master, text='systolic pressure:', width=12)
        self.systolic_label.place(x=5, y=90)

        self.systolic_input = Entry(master, width=10, bg='white', fg='black')
        self.systolic_input.place(x=150,y=90)

        self.diastolic_label = Label(master, text='diastolic pressure:', width=12)
        self.diastolic_label.place(x=5, y=130)

        self.diastolic_input = Entry(master, width=10, bg='white', fg='black')
        self.diastolic_input.place(x=150,y=130)

if __name__ == '__main__':
    root = Tk()
    app = GuiApp(root)
    root.mainloop()