from tkinter import *

root = Tk() # declear module
root.title("Sudoku James Asked") # title of the window
Label( text="Sudoku James Asked", font=24).pack() # text on head
frm1 = Frame(root) # frame for contain the table

# define variables to contain data
vr1c1, vr1c2, vr1c3, vr1c4, vr1c5, vr1c6, vr1c7, vr1c8, vr1c9 = [StringVar() for i in range(9)]
vr2c1, vr2c2, vr2c3, vr2c4, vr2c5, vr2c6, vr2c7, vr2c8, vr2c9 = [StringVar() for i in range(9)]
vr3c1, vr3c2, vr3c3, vr3c4, vr3c5, vr3c6, vr3c7, vr3c8, vr3c9 = [StringVar() for i in range(9)]
vr4c1, vr4c2, vr4c3, vr4c4, vr4c5, vr4c6, vr4c7, vr4c8, vr4c9 = [StringVar() for i in range(9)]  
vr5c1, vr5c2, vr5c3, vr5c4, vr5c5, vr5c6, vr5c7, vr5c8, vr5c9 = [StringVar() for i in range(9)]
vr6c1, vr6c2, vr6c3, vr6c4, vr6c5, vr6c6, vr6c7, vr6c8, vr6c9 = [StringVar() for i in range(9)]
vr7c1, vr7c2, vr7c3, vr7c4, vr7c5, vr7c6, vr7c7, vr7c8, vr7c9 = [StringVar() for i in range(9)]
vr8c1, vr8c2, vr8c3, vr8c4, vr8c5, vr8c6, vr8c7, vr8c8, vr8c9 = [StringVar() for i in range(9)]
vr9c1, vr9c2, vr9c3, vr9c4, vr9c5, vr9c6, vr9c7, vr9c8, vr9c9 = [StringVar() for i in range(9)]

# take all data in variables to a list
vrowcol = [[vr1c1, vr1c2, vr1c3, vr1c4, vr1c5, vr1c6, vr1c7, vr1c8, vr1c9],
           [vr2c1, vr2c2, vr2c3, vr2c4, vr2c5, vr2c6, vr2c7, vr2c8, vr2c9],
           [vr3c1, vr3c2, vr3c3, vr3c4, vr3c5, vr3c6, vr3c7, vr3c8, vr3c9],
           [vr4c1, vr4c2, vr4c3, vr4c4, vr4c5, vr4c6, vr4c7, vr4c8, vr4c9],
           [vr5c1, vr5c2, vr5c3, vr5c4, vr5c5, vr5c6, vr5c7, vr5c8, vr5c9],
           [vr6c1, vr6c2, vr6c3, vr6c4, vr6c5, vr6c6, vr6c7, vr6c8, vr6c9],
           [vr7c1, vr7c2, vr7c3, vr7c4, vr7c5, vr7c6, vr7c7, vr7c8, vr7c9],
           [vr8c1, vr8c2, vr8c3, vr8c4, vr8c5, vr8c6, vr8c7, vr8c8, vr8c9],
           [vr9c1, vr9c2, vr9c3, vr9c4, vr9c5, vr9c6, vr9c7, vr9c8, vr9c9]]


# declear text that displays what is happening
resultText1 = StringVar(value="!!! GAME START !!!") # text line 1
resultText2 = StringVar()                           # text line 2

# Label display row column at
for i in range(9):  
    Label(frm1, text=str(i+1)).grid(row=0,column=i+1)
    Label(frm1, text=str(i+1)).grid(row=i+1,column=0)

# section for the table
# Row 1
r1c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c1)
r1c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c2)
r1c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c3)
r1c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c4)
r1c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c5)
r1c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c6)
r1c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c7)
r1c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c8)
r1c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr1c9)
# Row 2
r2c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c1)
r2c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c2)
r2c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c3)
r2c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c4)
r2c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c5)
r2c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c6)
r2c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c7)  
r2c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c8)
r2c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr2c9)
# Row 3
r3c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c1)
r3c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c2)
r3c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c3)
r3c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c4)
r3c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c5)
r3c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c6)
r3c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c7)
r3c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c8)
r3c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr3c9)
# Row 4
r4c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c2)
r4c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c3)
r4c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c1)
r4c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c4)
r4c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c5)
r4c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c6)
r4c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c7)
r4c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c8)
r4c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr4c9)
# Row 5
r5c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c1)
r5c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c2)
r5c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c3)
r5c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c4)
r5c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c5)
r5c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c6)
r5c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c7)
r5c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c8)
r5c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr5c9)
# Row 6
r6c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c1)
r6c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c2)
r6c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c3)
r6c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c4)
r6c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c5)
r6c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c6)
r6c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c7)
r6c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c8)
r6c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr6c9)
# Row 7
r7c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c1)
r7c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c2)
r7c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c3)
r7c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c4)
r7c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c5)
r7c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c6)
r7c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c7)
r7c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c8)
r7c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr7c9)
# Row 8
r8c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c1)
r8c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c2)
r8c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c3)
r8c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c4)
r8c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c5)
r8c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c6)
r8c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c7)
r8c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c8)
r8c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr8c9)
# Row 9
r9c1 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c1)
r9c2 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c2)
r9c3 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c3)
r9c4 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c4)
r9c5 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c5)
r9c6 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c6)
r9c7 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c7)
r9c8 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c8)
r9c9 =  Entry(frm1, font=24, width=2, justify=CENTER, textvariable=vr9c9)

# take all widgits to a list
rowcol = [[r1c1, r1c2, r1c3, r1c4, r1c5, r1c6, r1c7, r1c8, r1c9],
           [r2c1, r2c2, r2c3, r2c4, r2c5, r2c6, r2c7, r2c8, r2c9],
           [r3c1, r3c2, r3c3, r3c4, r3c5, r3c6, r3c7, r3c8, r3c9],
           [r4c1, r4c2, r4c3, r4c4, r4c5, r4c6, r4c7, r4c8, r4c9],
           [r5c1, r5c2, r5c3, r5c4, r5c5, r5c6, r5c7, r5c8, r5c9],
           [r6c1, r6c2, r6c3, r6c4, r6c5, r6c6, r6c7, r6c8, r6c9],
           [r7c1, r7c2, r7c3, r7c4, r7c5, r7c6, r7c7, r7c8, r7c9],
           [r8c1, r8c2, r8c3, r8c4, r8c5, r8c6, r8c7, r8c8, r8c9],
           [r9c1, r9c2, r9c3, r9c4, r9c5, r9c6, r9c7, r9c8, r9c9]]

# section for grid to frame
# grid row 1
r1c1.grid(row=1,column=1)
r1c2.grid(row=1,column=2)
r1c3.grid(row=1,column=3)
r1c4.grid(row=1,column=4)
r1c5.grid(row=1,column=5)
r1c6.grid(row=1,column=6)
r1c7.grid(row=1,column=7)
r1c8.grid(row=1,column=8)
r1c9.grid(row=1,column=9)
# grid row 2
r2c1.grid(row=2,column=1)
r2c2.grid(row=2,column=2)
r2c3.grid(row=2,column=3)
r2c4.grid(row=2,column=4)
r2c5.grid(row=2,column=5)
r2c6.grid(row=2,column=6)
r2c7.grid(row=2,column=7)
r2c8.grid(row=2,column=8)
r2c9.grid(row=2,column=9)
# grid row 3
r3c1.grid(row=3,column=1)
r3c2.grid(row=3,column=2)
r3c3.grid(row=3,column=3)
r3c4.grid(row=3,column=4)
r3c5.grid(row=3,column=5)
r3c6.grid(row=3,column=6)
r3c7.grid(row=3,column=7)
r3c8.grid(row=3,column=8)
r3c9.grid(row=3,column=9)
# grid row 4
r4c1.grid(row=4,column=1)
r4c2.grid(row=4,column=2)
r4c3.grid(row=4,column=3)
r4c4.grid(row=4,column=4)
r4c5.grid(row=4,column=5)
r4c6.grid(row=4,column=6)
r4c7.grid(row=4,column=7)
r4c8.grid(row=4,column=8)
r4c9.grid(row=4,column=9)
# grid row 5
r5c1.grid(row=5,column=1)
r5c2.grid(row=5,column=2)
r5c3.grid(row=5,column=3)
r5c4.grid(row=5,column=4)
r5c5.grid(row=5,column=5)
r5c6.grid(row=5,column=6)
r5c7.grid(row=5,column=7)
r5c8.grid(row=5,column=8)
r5c9.grid(row=5,column=9)
# grid row 6
r6c1.grid(row=6,column=1)
r6c2.grid(row=6,column=2)
r6c3.grid(row=6,column=3)
r6c4.grid(row=6,column=4)
r6c5.grid(row=6,column=5)
r6c6.grid(row=6,column=6)
r6c7.grid(row=6,column=7)
r6c8.grid(row=6,column=8)
r6c9.grid(row=6,column=9)
# grid row 7
r7c1.grid(row=7,column=1)
r7c2.grid(row=7,column=2)
r7c3.grid(row=7,column=3)
r7c4.grid(row=7,column=4)
r7c5.grid(row=7,column=5)
r7c6.grid(row=7,column=6)
r7c7.grid(row=7,column=7)
r7c8.grid(row=7,column=8)
r7c9.grid(row=7,column=9)
# grid row 8
r8c1.grid(row=8,column=1)
r8c2.grid(row=8,column=2)
r8c3.grid(row=8,column=3)
r8c4.grid(row=8,column=4)
r8c5.grid(row=8,column=5)
r8c6.grid(row=8,column=6)
r8c7.grid(row=8,column=7)
r8c8.grid(row=8,column=8)
r8c9.grid(row=8,column=9)
# grid row 9
r9c1.grid(row=9,column=1)
r9c2.grid(row=9,column=2)
r9c3.grid(row=9,column=3)
r9c4.grid(row=9,column=4)
r9c5.grid(row=9,column=5)
r9c6.grid(row=9,column=6)
r9c7.grid(row=9,column=7)
r9c8.grid(row=9,column=8)
r9c9.grid(row=9,column=9)

frm1.pack() # pack a frame

# function for check the input row and column
def checker():
    global vrowcol, rowcol # take variables outside the function
    flag = False # to break loops
    # loop to take data in variables in a table
    # in row
    for i in range(9):
        # in column
        for j in range(9):
            if  not(vrowcol[i][j].get()).isdigit(): # If it is float, alphabet, decimal, negative integer
                resultText1.set("There are not a number(1-9) in a table.")
            else: # if it is a positive integer
                # if there is 1 character, range 1-9
                if len(vrowcol[i][j].get()) == 1 and int(vrowcol[i][j].get()) > 0 and int(vrowcol[i][j].get()) < 10:
                    # loop to check other rows and columns
                    for row in range(9):
                        for col in range(9):
                            # take variable loop and check loop are not the same
                            if i == row and j == col:
                                continue
                            # if there is a same number in row or column
                            elif vrowcol[i][j].get() == vrowcol[row][col].get():
                                resultText2.set("There is same number in row:{} column:{}.".format(row+1, col+1))
                                flag = True # stop check loop
                                break # stop column loop
                        if flag: # stop row loop
                            break
                    if not(flag): # if everything is okay
                        rowcol[i][j].configure(state="disabled") # disables that shell
                        resultText2.set("")                      
                else: # if there is not 1 character, range 1-9
                    resultText2.set("Enter only 1-9.")
    
Button(root, text="Submit", font=32, command=checker).pack(pady=10) # a button to cehck
Label(root, textvariable=resultText1, font=24).pack() # result line 1
Label(root, textvariable=resultText2, font=24).pack() # result line 2
    
root.mainloop() # start window