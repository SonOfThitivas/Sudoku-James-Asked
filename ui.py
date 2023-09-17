from tkinter import *
from random import randint

root = Tk() # declear module
root.title("Sudoku James Asked") # title of the window
Label( text="Sudoku James Asked", font=24).pack() # text on head

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
# list in 9x9
vrowcol9x9 = [[vr1c1, vr1c2, vr1c3, vr1c4, vr1c5, vr1c6, vr1c7, vr1c8, vr1c9],
           [vr2c1, vr2c2, vr2c3, vr2c4, vr2c5, vr2c6, vr2c7, vr2c8, vr2c9],
           [vr3c1, vr3c2, vr3c3, vr3c4, vr3c5, vr3c6, vr3c7, vr3c8, vr3c9],
           [vr4c1, vr4c2, vr4c3, vr4c4, vr4c5, vr4c6, vr4c7, vr4c8, vr4c9],
           [vr5c1, vr5c2, vr5c3, vr5c4, vr5c5, vr5c6, vr5c7, vr5c8, vr5c9],
           [vr6c1, vr6c2, vr6c3, vr6c4, vr6c5, vr6c6, vr6c7, vr6c8, vr6c9],
           [vr7c1, vr7c2, vr7c3, vr7c4, vr7c5, vr7c6, vr7c7, vr7c8, vr7c9],
           [vr8c1, vr8c2, vr8c3, vr8c4, vr8c5, vr8c6, vr8c7, vr8c8, vr8c9],
           [vr9c1, vr9c2, vr9c3, vr9c4, vr9c5, vr9c6, vr9c7, vr9c8, vr9c9]]

# list in 3x3 that starts left to right, up to down
vrowcol3x3 = [[vr1c1, vr1c2, vr1c3,vr2c1, vr2c2, vr2c3, vr3c1, vr3c2, vr3c3], # 1x1
              [vr1c4, vr1c5, vr1c6,vr2c4, vr2c5, vr2c6, vr3c4, vr3c5, vr3c6], # 1x2
              [vr1c7, vr1c8, vr1c9,vr2c7, vr2c8, vr2c9, vr3c7, vr3c8, vr3c9], # 1x3
              [vr4c1, vr4c2, vr4c3,vr5c1, vr5c2, vr5c3, vr6c1, vr6c2, vr6c3], # 2x1
              [vr4c4, vr4c5, vr4c6,vr5c4, vr5c5, vr5c6, vr6c4, vr6c5, vr6c6], # 2x2
              [vr4c7, vr4c8, vr4c9,vr5c7, vr5c8, vr5c9, vr6c7, vr6c8, vr6c9], # 2x3
              [vr7c1, vr7c2, vr7c3,vr8c1, vr8c2, vr8c3, vr9c1, vr9c2, vr9c3], # 3x1
              [vr7c4, vr7c5, vr7c6,vr8c4, vr8c5, vr8c6, vr9c4, vr9c5, vr9c6], # 3x2
              [vr7c7, vr7c8, vr7c9,vr8c7, vr8c8, vr8c9, vr9c7, vr9c8, vr9c9]] # 3x3

# declear text that displays what is happening
resultText1 = StringVar(value="!!! GAME START !!!") # text line 1
resultText2 = StringVar()                           # text line 2

# section for the table
tableFrame = Frame(root) # frame for contain the table
# text show numbers of row and column
row0col0Frame = Frame(tableFrame) # empty frame to fit gird
row0col1Frame = Frame(tableFrame) # 123 column
row0col2Frame = Frame(tableFrame) # 456 column
row0col3Frame = Frame(tableFrame) # 789 column
row1col0Frame = Frame(tableFrame) # 123 row
row2col0Frame = Frame(tableFrame) # 456 row
row3col0Frame = Frame(tableFrame) # 789 row
# table 3x3
row1col1Frame = Frame(tableFrame)
row1col2Frame = Frame(tableFrame)
row1col3Frame = Frame(tableFrame)
row2col1Frame = Frame(tableFrame)
row2col2Frame = Frame(tableFrame)
row2col3Frame = Frame(tableFrame)
row3col1Frame = Frame(tableFrame)
row3col2Frame = Frame(tableFrame)
row3col3Frame = Frame(tableFrame)

# entry table
# row 1 column 1 
r1c1 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr1c1)
r1c2 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr1c2)
r1c3 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr1c3)
r2c1 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr2c1)
r2c2 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr2c2)
r2c3 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr2c3)
r3c1 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr3c1)
r3c2 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr3c2)
r3c3 =  Entry(row1col1Frame, font=24, width=2, justify=CENTER, textvariable=vr3c3)
# row 1 column 2 
r1c4 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr1c4)
r1c5 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr1c5)
r1c6 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr1c6)
r2c4 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr2c4)
r2c5 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr2c5)
r2c6 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr2c6)
r3c4 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr3c4)  
r3c5 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr3c5)
r3c6 =  Entry(row1col2Frame, font=24, width=2, justify=CENTER, textvariable=vr3c6)
# row 1 column 3 
r1c7 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr1c7)
r1c8 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr1c8)
r1c9 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr1c9)
r2c7 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr2c7)
r2c8 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr2c8)
r2c9 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr2c9)
r3c7 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr3c7)
r3c8 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr3c8)
r3c9 =  Entry(row1col3Frame, font=24, width=2, justify=CENTER, textvariable=vr3c9)
# row 2 column 1 
r4c1 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr4c1)
r4c2 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr4c2)
r4c3 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr4c3)
r5c1 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr5c1)
r5c2 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr5c2)
r5c3 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr5c3)
r6c1 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr6c1)
r6c2 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr6c2)
r6c3 =  Entry(row2col1Frame, font=24, width=2, justify=CENTER, textvariable=vr6c3)
# row 2 column 2 
r4c4 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr4c4)
r4c5 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr4c5)
r4c6 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr4c6)
r5c4 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr5c4)
r5c5 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr5c5)
r5c6 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr5c6)
r6c4 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr6c4)
r6c5 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr6c5)
r6c6 =  Entry(row2col2Frame, font=24, width=2, justify=CENTER, textvariable=vr6c6)
# row 2 column 3 
r4c7 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr4c7)
r4c8 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr4c8)
r4c9 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr4c9)
r5c7 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr5c7)
r5c8 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr5c8)
r5c9 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr5c9)
r6c7 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr6c7)
r6c8 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr6c8)
r6c9 =  Entry(row2col3Frame, font=24, width=2, justify=CENTER, textvariable=vr6c9)
# row 3 column 1 
r7c1 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr7c1)
r7c2 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr7c2)
r7c3 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr7c3)
r8c1 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr8c1)
r8c2 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr8c2)
r8c3 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr8c3)
r9c1 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr9c1)
r9c2 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr9c2)
r9c3 =  Entry(row3col1Frame, font=24, width=2, justify=CENTER, textvariable=vr9c3)
# row 3 column 2 
r7c4 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr7c4)
r7c5 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr7c5)
r7c6 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr7c6)
r8c4 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr8c4)
r8c5 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr8c5)
r8c6 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr8c6)
r9c4 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr9c4)
r9c5 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr9c5)
r9c6 =  Entry(row3col2Frame, font=24, width=2, justify=CENTER, textvariable=vr9c6)
# row 3 column 3
r7c7 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr7c7)
r7c8 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr7c8)
r7c9 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr7c9)
r8c7 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr8c7)
r8c8 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr8c8)
r8c9 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr8c9)
r9c7 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr9c7)
r9c8 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr9c8)
r9c9 =  Entry(row3col3Frame, font=24, width=2, justify=CENTER, textvariable=vr9c9)


# take all widgits to a list
# list in row and column
rowcol9x9 = [[r1c1, r1c2, r1c3, r1c4, r1c5, r1c6, r1c7, r1c8, r1c9],
           [r2c1, r2c2, r2c3, r2c4, r2c5, r2c6, r2c7, r2c8, r2c9],
           [r3c1, r3c2, r3c3, r3c4, r3c5, r3c6, r3c7, r3c8, r3c9],
           [r4c1, r4c2, r4c3, r4c4, r4c5, r4c6, r4c7, r4c8, r4c9],
           [r5c1, r5c2, r5c3, r5c4, r5c5, r5c6, r5c7, r5c8, r5c9],
           [r6c1, r6c2, r6c3, r6c4, r6c5, r6c6, r6c7, r6c8, r6c9],
           [r7c1, r7c2, r7c3, r7c4, r7c5, r7c6, r7c7, r7c8, r7c9],
           [r8c1, r8c2, r8c3, r8c4, r8c5, r8c6, r8c7, r8c8, r8c9],
           [r9c1, r9c2, r9c3, r9c4, r9c5, r9c6, r9c7, r9c8, r9c9]]

# list in 3x3 that starts left to right, up to down
rowcol3x3 = [[r1c1, r1c2, r1c3,r2c1, r2c2, r2c3, r3c1, r3c2, r3c3], # 1x1
              [r1c4, r1c5, r1c6,r2c4, r2c5, r2c6, r3c4, r3c5, r3c6], # 1x2
              [r1c7, r1c8, r1c9,r2c7, r2c8, r2c9, r3c7, r3c8, r3c9], # 1x3
              [r4c1, r4c2, r4c3,r5c1, r5c2, r5c3, r6c1, r6c2, r6c3], # 2x1
              [r4c4, r4c5, r4c6,r5c4, r5c5, r5c6, r6c4, r6c5, r6c6], # 2x2
              [r4c7, r4c8, r4c9,r5c7, r5c8, r5c9, r6c7, r6c8, r6c9], # 2x3
              [r7c1, r7c2, r7c3,r8c1, r8c2, r8c3, r9c1, r9c2, r9c3], # 3x1
              [r7c4, r7c5, r7c6,r8c4, r8c5, r8c6, r9c4, r9c5, r9c6], # 3x2
              [r7c7, r7c8, r7c9,r8c7, r8c8, r8c9, r9c7, r9c8, r9c9]] # 3x3

# Label display row column at
Label(row0col0Frame, text=" ").grid(row=0,column=0) # empty grid
# show columns
Label(row0col1Frame, text="1", font=24).grid(row=0,column=0,padx=2)
Label(row0col1Frame, text="2", font=24).grid(row=0,column=1,padx=2)
Label(row0col1Frame, text="3", font=24).grid(row=0,column=2,padx=2)
Label(row0col2Frame, text="4", font=24).grid(row=0,column=0,padx=2)
Label(row0col2Frame, text="5", font=24).grid(row=0,column=1,padx=2)
Label(row0col2Frame, text="6", font=24).grid(row=0,column=2,padx=2)
Label(row0col3Frame, text="7", font=24).grid(row=0,column=0,padx=2)
Label(row0col3Frame, text="8", font=24).grid(row=0,column=1,padx=2)
Label(row0col3Frame, text="9", font=24).grid(row=0,column=2,padx=2)
# show rows
Label(row1col0Frame, text="1", font=24).grid(row=0,column=0,padx=2)
Label(row1col0Frame, text="2", font=24).grid(row=1,column=0,padx=2)
Label(row1col0Frame, text="3", font=24).grid(row=0,column=0,padx=2)
Label(row2col0Frame, text="4", font=24).grid(row=0,column=0,padx=2)
Label(row2col0Frame, text="5", font=24).grid(row=1,column=0,padx=2)
Label(row2col0Frame, text="6", font=24).grid(row=2,column=0,padx=2)
Label(row3col0Frame, text="7", font=24).grid(row=0,column=0,padx=2)
Label(row3col0Frame, text="8", font=24).grid(row=1,column=0,padx=2)
Label(row3col0Frame, text="9", font=24).grid(row=2,column=0,padx=2)

r1c1.grid(row=0,column=0)
r1c2.grid(row=0,column=1)
r1c3.grid(row=0,column=2)
r2c1.grid(row=1,column=0)
r2c2.grid(row=1,column=1)
r2c3.grid(row=1,column=2)
r3c1.grid(row=2,column=0)
r3c2.grid(row=2,column=1)
r3c3.grid(row=2,column=2)
r1c4.grid(row=0,column=0)
r1c5.grid(row=0,column=1)
r1c6.grid(row=0,column=2)
r2c4.grid(row=1,column=0)
r2c5.grid(row=1,column=1)
r2c6.grid(row=1,column=2)
r3c4.grid(row=2,column=0)
r3c5.grid(row=2,column=1)
r3c6.grid(row=2,column=2)
r1c7.grid(row=0,column=0)
r1c8.grid(row=0,column=1)
r1c9.grid(row=0,column=2)
r2c7.grid(row=1,column=0)
r2c8.grid(row=1,column=1)
r2c9.grid(row=1,column=2)
r3c7.grid(row=2,column=0)
r3c8.grid(row=2,column=1)
r3c9.grid(row=2,column=2)
r4c1.grid(row=0,column=0)
r4c2.grid(row=0,column=1)
r4c3.grid(row=0,column=2)
r5c1.grid(row=1,column=0)
r5c2.grid(row=1,column=1)
r5c3.grid(row=1,column=2)
r6c1.grid(row=2,column=0)
r6c2.grid(row=2,column=1)
r6c3.grid(row=2,column=2)
r4c4.grid(row=0,column=0)
r4c5.grid(row=0,column=1)
r4c6.grid(row=0,column=2)
r5c4.grid(row=1,column=0)
r5c5.grid(row=1,column=1)
r5c6.grid(row=1,column=2)
r6c4.grid(row=2,column=0)
r6c5.grid(row=2,column=1)
r6c6.grid(row=2,column=2)
r4c7.grid(row=0,column=0)
r4c8.grid(row=0,column=1)
r4c9.grid(row=0,column=2)
r5c7.grid(row=1,column=0)
r5c8.grid(row=1,column=1)
r5c9.grid(row=1,column=2)
r6c7.grid(row=2,column=0)
r6c8.grid(row=2,column=1)
r6c9.grid(row=2,column=2)
r7c1.grid(row=0,column=0)
r7c2.grid(row=0,column=1)
r7c3.grid(row=0,column=2)
r8c1.grid(row=1,column=0)
r8c2.grid(row=1,column=1)
r8c3.grid(row=1,column=2)
r9c1.grid(row=2,column=0)
r9c2.grid(row=2,column=1)
r9c3.grid(row=2,column=2)
r7c4.grid(row=0,column=0)
r7c5.grid(row=0,column=1)
r7c6.grid(row=0,column=2)
r8c4.grid(row=1,column=0)
r8c5.grid(row=1,column=1)
r8c6.grid(row=1,column=2)
r9c4.grid(row=2,column=0)
r9c5.grid(row=2,column=1)
r9c6.grid(row=2,column=2)
r7c7.grid(row=0,column=0)
r7c8.grid(row=0,column=1)
r7c9.grid(row=0,column=2)
r8c7.grid(row=1,column=0)
r8c8.grid(row=1,column=1)
r8c9.grid(row=1,column=2)
r9c7.grid(row=2,column=0)
r9c8.grid(row=2,column=1)
r9c9.grid(row=2,column=2)

row0col0Frame.grid(row=0,column=0, padx=2)
row0col1Frame.grid(row=0,column=1, padx=2)
row0col2Frame.grid(row=0,column=2, padx=2)
row0col3Frame.grid(row=0,column=3, padx=2)
row1col0Frame.grid(row=1,column=0, padx=2)
row2col0Frame.grid(row=2,column=0, padx=2)
row3col0Frame.grid(row=3,column=0, padx=2)
row1col1Frame.grid(row=1,column=1, padx=2)
row1col2Frame.grid(row=1,column=2, padx=2)
row1col3Frame.grid(row=1,column=3, padx=2)
row2col1Frame.grid(row=2,column=1, padx=2)
row2col2Frame.grid(row=2,column=2, padx=2)
row2col3Frame.grid(row=2,column=3, padx=2)
row3col1Frame.grid(row=3,column=1, padx=2)
row3col2Frame.grid(row=3,column=2, padx=2)
row3col3Frame.grid(row=3,column=3, padx=2)

tableFrame.pack() # pack a frame



# contain widgets that are disabled
rowcolLatest = []


# initial random 30 numbers at first
for time in range(30):
    row = randint(0,8)
    col = randint(0,8)
    num = randint(1,9)
    if vrowcol[row][col].get() == "":
        vrowcol[row][col].set(str(num))
        rowcolLatest.append(rowcol[row][col])
        
def checker3x3():
    global vrowcol3x3, vrowcol9x9, rowcol, rowcolLatest # take variables outside the function
    flag = False
    # check table 3x3
    for checkRow in range(9):
        for checkCol in range(9):
            if not(vrowcol3x3[checkRow][checkCol].get()).isdigit(): # If it is float, alphabet, decimal, negative integer
                continue
            else:
                # if there is 1 character, range 1-9
                if len(vrowcol3x3[checkRow][checkCol].get()) == 1 and int(vrowcol3x3[checkRow][checkCol].get()) > 0 and int(vrowcol3x3[checkRow][checkCol].get()) < 10:
                    # loop to check other rows and columns
                    for otherRow3x3 in range(9):
                        for otherCol3x3 in range(9):
                            if checkRow == otherRow3x3 and checkCol == otherCol3x3: # do not check in the same table
                                continue
                            elif vrowcol3x3[otherRow3x3][otherCol3x3].get() == vrowcol3x3[checkRow][checkCol].get():
                                return False # case same in the table 3x3
                            
def checker9x9():
    for checkRow in range(9):
        for checkCol in range(9):
            if not(vrowcol9x9[checkRow][checkCol].get()).isdigit(): # If it is float, alphabet, decimal, negative integer
                return 0 # case not a positive integer
            else:
                # if there is 1 character, range 1-9
                if len(vrowcol3x3[checkRow][checkCol].get()) == 1 and int(vrowcol3x3[checkRow][checkCol].get()) > 0 and int(vrowcol3x3[checkRow][checkCol].get()) < 10:
                    # loop to check other rows and columns
                    for otherRow3x3 in range(9):
                        for otherCol3x3 in range(9):
                            if checkRow == otherRow3x3 and checkCol == otherCol3x3: # do not check in the same table
                                continue
                            elif vrowcol3x3[otherRow3x3][otherCol3x3].get() == vrowcol3x3[checkRow][checkCol].get():
                                return False # case same in the table 3x3

# function for check the input row and column
def submit():
    global vrowcol, rowcol, rowcolLatest # take variables outside the function
    flag = False # to break loops
    # loop to take data in variables in a table
    # input from rows
    for rowinput in range(9):
        # input from columns
        for colinput in range(9):
            if  not (vrowcol[rowinput][colinput].get()).isdigit(): # If it is float, alphabet, decimal, negative integer
                resultText1.set("There are not a number(1-9) in a table.")
            else: # if it is a positive integer
                # if there is 1 character, range 1-9
                if len(vrowcol[rowinput][colinput].get()) == 1 and int(vrowcol[rowinput][colinput].get()) > 0 and int(vrowcol[rowinput][colinput].get()) < 10:
                    # loop to check other rows and columns
                    for allrow in range(9):
                        for allcol in range(9):
                            # take variable loop and check loop are not the same
                            if rowinput == allrow and colinput == allcol:
                                continue
                            # if there is a same number in row or column
                            elif (vrowcol[rowinput][colinput].get() == vrowcol[allrow][allcol].get()) and (allrow == rowinput or allcol == colinput):
                                resultText2.set("There is same number in row:{} column:{}.".format(allrow+1, allcol+1))
                                flag = True # stop check loop
                                break # stop column loop
                        if flag: # stop row loop
                            break
                    if not(flag): # if everything is okay
                        rowcol[rowinput][colinput].configure(state="disabled") # disables that shell
                        rowcolLatest.append([rowinput, colinput]) # add a latest widgets that are disables
                        resultText2.set("")                      
                else: # if there is not 1 character, range 1-9
                    resultText2.set("Enter only 1-9.")
                    
    # GAME OVER if all tables disable
    flag = False # to break nested loop
    for row in rowcol:
        for column in row: # widgets
            state = str(column["state"]) 
            if  state == "disabled": # check state
                continue
            else:
                flag = True
                break
                
        if flag:
            break
    if not(flag): # if all widgets are disabled
        resultText1.set("!!! GAME OVER !!!")
        resultText2.set("!!! Thank you for playing !!!")

# function previous event
def previous():
    global vrowcol, rowcol, rowcolLatest # take variables outside the function
    rowcolIndex = rowcolLatest.pop() # take a last widget
    row = rowcolIndex[0] # row of latest widget
    col = rowcolIndex[1] # col of latest widget
    rowcol[row][col].configure(state="normal") # be normal
    vrowcol[row][col].set("") # clear a input

buttonFrame = Frame(root) # button frame
Button(buttonFrame, text="Submit", font=32, command=submit).grid(row=0,column=0, padx=5) # a button to check
Button(buttonFrame, text="Previous", font=32, command=previous).grid(row=0,column=1, padx=5) # a button to pervious
buttonFrame.pack(pady=10, anchor="center")

Label(root, textvariable=resultText1, font=24).pack() # result line 1
Label(root, textvariable=resultText2, font=24).pack() # result line 2
    
root.mainloop() # start window