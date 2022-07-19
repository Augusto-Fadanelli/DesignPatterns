import tkinter as tk
from tkinter import Text, ttk

from ttkthemes import ThemedTk


class ConfigWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Notepad - Config')
        self.geometry('250x180')

        self.font_label = ttk.Label(self, text='Font:')
        self.size_label = ttk.Label(self, text='Size:')

        self.font_combo = ttk.Combobox(self, values=['Arial', 'Hack', 'Times'])
        self.size_combo = ttk.Combobox(
            self, values=['8', '10', '12', '14', '16', '18', '20']
        )
        self.font_combo.set('Hack')
        self.size_combo.set('12')

        self.apply = ttk.Button(self, text='Apply')

        # Show
        self.font_label.pack(padx=10, pady=10)
        self.font_combo.pack(padx=10)
        self.size_label.pack(padx=10, pady=10)
        self.size_combo.pack(padx=10)
        self.apply.pack(padx=10, pady=10)


class Window(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme('breeze')
        self.title('Notepad')

        self.__frame_general = ttk.Frame()
        self.__frame_toolbar = ttk.Frame(self.__frame_general)

        self.__toolbar()
        self.__textBox()
        self.__show()

    def __open_config(self):
        self.config_window = ConfigWindow(self)
        self.config_window.grab_set()

    def __toolbar(self):
        file = ttk.Menubutton(self.__frame_toolbar, text='File')
        file.menu = tk.Menu(self.__frame_toolbar, tearoff=0)
        file.menu.add_radiobutton(label='Open', value='Open')
        file.menu.add_radiobutton(label='Save', value='Save')
        file.menu.add_radiobutton(label='Save as...', value='Save as...')
        file['menu'] = file.menu

        config = ttk.Button(
            self.__frame_toolbar, text='Config', command=self.__open_config
        )
        about = ttk.Button(self.__frame_toolbar, text='About')

        # Show
        file.grid(row=0, column=0, padx=10, pady=5)
        config.grid(row=0, column=1, padx=10, pady=5)
        about.grid(row=0, column=2, padx=10, pady=5)

    def __textBox(self):
        # font = ConfigWindow(self).font_combo.get()
        # size = int(ConfigWindow(self).size_combo.get())
        self.textbox = Text(
            self.__frame_general,
            height=25,
            width=70,
            font=('Hack', 12),
            bg='#bac3cc',
        )

    def __show(self):
        # Show
        self.__frame_toolbar.pack()
        self.textbox.pack(padx=10, pady=10, fill='both', expand='yes')
        self.__frame_general.pack(fill='both', expand='yes')


if __name__ == '__main__':
    window = Window()
    window.mainloop()
