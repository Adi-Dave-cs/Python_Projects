# tutorial is available at : https://pypi.org/project/prettytable/

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Admfm",["Bdd","Cdddd","Dddddd","Ekrokoe"])
table.add_column("Fdjdjdjdn",["Ginin","Hhbhb","Ibfbbf","Jd"])
# table align left
table.align = 'l'
print(table)
# table align center
table.align = 'c'
print(table)
# table align contents in right
table.align = 'r'
print(table)