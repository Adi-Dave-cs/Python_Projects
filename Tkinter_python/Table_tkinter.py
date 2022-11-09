# Python program to create a table

from tkinter import *


class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='blue',
							font=('Arial',16,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'A','E',1),
	(2,'B','F',1),
	(3,'B','G',2),
	(4,'C','G',2),
	(5,'D','G',3)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
root.title("Table in tkinter")
t = Table(root)
root.mainloop()
