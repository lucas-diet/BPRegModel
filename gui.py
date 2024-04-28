
from tkinter import *

class GuiApp():
    def __init__(self, master):
        self.master = master
        master.title('Blood Pressure Simulator')
        master.geometry('400x200')

        self.duration_holder = 'duration'
        self.heartRate_holder = 'heart rate'

        self.placeholders = {
            'duration': 'duration',
            'heartRate': 'heart rate',
            'systolic': 'systolic'}

        # Eingabefelder erstellen und platzieren
        self.entries = {}
        row = 0
        column = 0
        for key, placeholder in self.placeholders.items():
            entry = Entry(self.master, width=10)
            entry.insert(0, placeholder)
            entry.grid(row=row, column=column, padx=10, pady=10)
            entry.bind('<FocusIn>', lambda event, widget=entry, key=key: self.onFocusIn(widget, key))
            entry.bind('<FocusOut>', lambda event, widget=entry, key=key, placeholder=placeholder: self.onFocusOut(widget, key, placeholder))
            self.entries[key] = entry
            entry.config(bg='white', fg='gray')
            row += 1
            if row == 3:
                row = 0
                column += 1
            elif column == 2:
                #TODO: Zukunft, je nachdem wie viele Paramter
                pass


    def onFocusIn(self, widget, key):
        #Wird aufgerufen, wenn das Entry-Feld den Fokus erhält.
        if widget.get() == self.placeholders[key]:
            widget.delete(0, END)

    def onFocusOut(self, widget, key, placeholder):
        #Wird aufgerufen, wenn das Entry-Feld den Fokus verliert.
        if not widget.get():
            widget.insert(0, placeholder)

if __name__ == '__main__':
    root = Tk()
    app = GuiApp(root)
    root.mainloop()