import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calcultor")
        root.resizable(False, False)
        root.config(padx=10, pady=10, bg="#85857d")

        self.equation = tk.StringVar()
        self.entry_value = ''

        #Display
        entry = tk.Entry(root, textvariable=self.equation, font=("Arial", 18), bd=5, relief="flat", justify="left")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))

        # Buttons
        buttons = [
            ('C', 1, 0, self.clear),
            ('back', 1, 1, self.backspace),
            ('%', 1, 2, lambda: self.show('%')),
            ('/', 1, 3, lambda: self.show('/')),

            ('7', 2, 0, lambda: self.show('7')),
            ('8', 2, 1, lambda: self.show('8')),
            ('9', 2, 2, lambda: self.show('9')),
            ('*', 2, 3, lambda: self.show('*')),

            ('4', 3, 0, lambda: self.show('4')),
            ('5', 3, 1, lambda: self.show('5')),
            ('6', 3, 2, lambda: self.show('6')),
            ('-', 3, 3, lambda: self.show('-')),

            ('1', 4, 0, lambda: self.show('1')),
            ('2', 4, 1, lambda: self.show('2')),
            ('3', 4, 2, lambda: self.show('3')),
            ('+', 4, 3, lambda: self.show('+')),

            ('0', 5, 0, lambda: self.show('0')),
            ('.', 5, 1, lambda: self.show('.')),
            ('(', 5, 2, lambda: self.show('(')),
            (')', 5, 3, lambda: self.show(')')),

            ('=', 6, 0, self.solve)
        ]

        for (text, row, col, command) in buttons:
            btn = tk.Button(root, text=text, font=("Arial", 16), width=5, height=2, command=command)
            btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        # making equla button
        root.grid_rowconfigure(6, weight=1)
        equal_btn = tk.Button(root, text='=', font=("Arial", 18), bg='#4125b3', command=self.solve)
        equal_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # responsive columns
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
