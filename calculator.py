"""
GUI Calculator Application
"""

import tkinter as tk


class CalculatorGUI:
    """Calculator GUI"""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 20),
            justify="right"
        )
        display.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(
                root,
                text=button,
                width=8,
                height=3,
                command=lambda value=button: self.click(value)
            ).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(
            root,
            text="C",
            width=34,
            height=2,
            command=self.clear
        ).grid(row=5, column=0, columnspan=4)

    def click(self, value):
        """Handle button click"""

        if value == "=":
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except (SyntaxError, ZeroDivisionError):
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.display_var.set(self.expression)

    def clear(self):
        """Clear display"""
        self.expression = ""
        self.display_var.set("")


def main():
    """Application entry point"""
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()