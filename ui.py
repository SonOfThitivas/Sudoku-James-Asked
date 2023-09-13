from tkinter import *

root = Tk()
root.title("Sudoku James Asked")
varrowcol = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for j in range(9):
        varrowcol[i].append(0)
Label( text="Sudoku James Asked", font=24).pack()
frm1 = Frame(root)

# Label
for i in range(9):  
    Label(frm1, text=str(i+1)).grid(row=0,column=i+1)
    Label(frm1, text=str(i+1)).grid(row=i+1,column=0)
# Row 1
r1c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=1)
r1c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=2)
r1c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=3)
r1c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=4)
r1c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=5)
r1c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=6)
r1c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=7)
r1c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=8)
r1c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=1,column=9)
# Row 2
r2c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=1)
r2c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=2)
r2c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=3)
r2c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=4)
r2c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=5)
r2c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=6)
r2c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=7)
r2c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=8)
r2c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=2,column=9)
# Row 3
r3c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=1)
r3c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=2)
r3c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=3)
r3c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=4)
r3c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=5)
r3c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=6)
r3c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=7)
r3c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=8)
r3c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=3,column=9)
# Row 4
r4c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=1)
r4c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=2)
r4c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=3)
r4c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=4)
r4c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=5)
r4c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=6)
r4c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=7)
r4c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=8)
r4c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=4,column=9)
# Row 5
r5c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=1)
r5c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=2)
r5c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=3)
r5c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=4)
r5c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=5)
r5c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=6)
r5c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=7)
r5c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=8)
r5c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=5,column=9)
# Row 6
r6c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=1)
r6c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=2)
r6c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=3)
r6c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=4)
r6c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=5)
r6c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=6)
r6c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=7)
r6c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=8)
r6c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=6,column=9)
# Row 7
r7c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=1)
r7c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=2)
r7c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=3)
r7c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=4)
r7c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=5)
r7c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=6)
r7c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=7)
r7c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=8)
r7c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=7,column=9)
# Row 8
r8c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=1)
r8c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=2)
r8c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=3)
r8c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=4)
r8c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=5)
r8c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=6)
r8c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=7)
r8c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=8)
r8c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=8,column=9)
# Row 9
r9c1 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=1)
r9c2 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=2)
r9c3 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=3)
r9c4 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=4)
r9c5 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=5)
r9c6 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=6)
r9c7 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=7)
r9c8 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=8)
r9c9 =  Entry(frm1, font=24, width=2, justify=CENTER).grid(row=9,column=9)

frm1.pack()
Button(root, text="Submit", font=32).pack(pady=10)
    
def checker():
    return 0
# def disableEntry( rc):
#     rc.configure(state="disabled")
    

root.mainloop()