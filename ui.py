import tkinter as tk

class Sudoku_James_Asked(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku James Asked")
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Sudoku James Asked", font=24).pack()
        self.frm1 = tk.Frame(self)  

        # Label
        for i in range(9):  
            tk.Label(self.frm1, text=str(i+1)).grid(row=0,column=i+1)
            tk.Label(self.frm1, text=str(i+1)).grid(row=i+1,column=0)
        # Row 1
        self.r1c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=1)
        self.r1c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=2)
        self.r1c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=3)
        self.r1c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=4)
        self.r1c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=5)
        self.r1c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=6)
        self.r1c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=7)
        self.r1c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=8)
        self.r1c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=1,column=9)
        # Row 2
        self.r2c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=1)
        self.r2c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=2)
        self.r2c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=3)
        self.r2c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=4)
        self.r2c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=5)
        self.r2c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=6)
        self.r2c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=7)
        self.r2c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=8)
        self.r2c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=2,column=9)
        # Row 3
        self.r3c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=1)
        self.r3c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=2)
        self.r3c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=3)
        self.r3c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=4)
        self.r3c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=5)
        self.r3c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=6)
        self.r3c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=7)
        self.r3c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=8)
        self.r3c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=3,column=9)
        # Row 4
        self.r4c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=1)
        self.r4c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=2)
        self.r4c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=3)
        self.r4c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=4)
        self.r4c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=5)
        self.r4c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=6)
        self.r4c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=7)
        self.r4c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=8)
        self.r4c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=4,column=9)
        # Row 5
        self.r5c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=1)
        self.r5c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=2)
        self.r5c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=3)
        self.r5c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=4)
        self.r5c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=5)
        self.r5c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=6)
        self.r5c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=7)
        self.r5c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=8)
        self.r5c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=5,column=9)
        # Row 6
        self.r6c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=1)
        self.r6c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=2)
        self.r6c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=3)
        self.r6c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=4)
        self.r6c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=5)
        self.r6c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=6)
        self.r6c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=7)
        self.r6c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=8)
        self.r6c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=6,column=9)
        # Row 7
        self.r7c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=1)
        self.r7c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=2)
        self.r7c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=3)
        self.r7c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=4)
        self.r7c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=5)
        self.r7c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=6)
        self.r7c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=7)
        self.r7c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=8)
        self.r7c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=7,column=9)
        # Row 8
        self.r8c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=1)
        self.r8c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=2)
        self.r8c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=3)
        self.r8c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=4)
        self.r8c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=5)
        self.r8c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=6)
        self.r8c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=7)
        self.r8c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=8)
        self.r8c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=8,column=9)
        # Row 9
        self.r9c1 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=1)
        self.r9c2 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=2)
        self.r9c3 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=3)
        self.r9c4 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=4)
        self.r9c5 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=5)
        self.r9c6 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=6)
        self.r9c7 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=7)
        self.r9c8 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=8)
        self.r9c9 = tk.Entry(self.frm1, font=24, width=2, justify="center").grid(row=9,column=9)

        self.frm1.pack()

        tk.Button(self, text="Submit", font=32).pack(pady=10)
        
    def checker(self):
    
    # def disableEntry(self, rc):
    #     rc.configure(state="disabled")
    
if __name__ == "__main__":
    root = Sudoku_James_Asked()
    root.mainloop()