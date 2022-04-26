# pip install ttkthemes

import tkinter as tk
from tkinter import ttk, Text
from ttkthemes import ThemedTk

class ConfigWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Notepad - Config')
        self.geometry('250x150')

        self.font_label = ttk.Label(self, text='Font:')
        self.size_label = ttk.Label(self, text='Size:')

        self.font_combo = ttk.Combobox(self, values=['Arial', 'Times', 'Hack'])
        self.size_combo = ttk.Combobox(self, values=['8', '10', '12', '14', '16', '18', '20'])
        self.font_combo.set('Arial')
        self.size_combo.set('12')

        # Show
        self.font_label.pack(padx=10, pady=5)
        self.font_combo.pack(padx=10, pady=5)
        self.size_label.pack(padx=10, pady=5)
        self.size_combo.pack(padx=10, pady=5)

class Window(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme('breeze')
        self.title('Notepad')

        self.__frame_general = ttk.Frame()
        self.__frame_toolbar = ttk.Frame(self.__frame_general)

        self.__toolbar()
        self.__general()

    def __open_config(self):
        config_window = ConfigWindow(self)
        config_window.grab_set()

    def __toolbar(self):
        file = ttk.Menubutton(self.__frame_toolbar, text='File')
        file.menu = tk.Menu(self.__frame_toolbar, tearoff=0)
        file.menu.add_radiobutton(label='Open', value='Open')
        file.menu.add_radiobutton(label='Save', value='Save')
        file.menu.add_radiobutton(label='Save as...', value='Save as...')
        file["menu"] = file.menu

        config = ttk.Button(self.__frame_toolbar, text='Config', command=self.__open_config)
        about = ttk.Button(self.__frame_toolbar, text='About')

        # Show
        file.grid(row=0, column=0, padx=10, pady=5)
        config.grid(row=0, column=1, padx=10, pady=5)
        about.grid(row=0, column=2, padx=10, pady=5)

    def __general(self):
        textbox = Text(self.__frame_general, height=25, width=70, font=('Arial', 12), bg='#bac3cc')

        # Show
        self.__frame_toolbar.pack()
        textbox.pack(padx=10, pady=10, fill='both', expand='yes')
        self.__frame_general.pack(fill='both', expand='yes')

if __name__ == '__main__':
    window = Window()
    window.mainloop()
