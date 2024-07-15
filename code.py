import itertools    # For creating cartesian product for naming boxes
from time import time
from time import strptime

all_boxes={}

ab=['A','B','C','D','E','F','G','H','I']
number=['1','2','3','4','5','6','7','8','9']

a=list(itertools.product(ab,number))
b=[]
for i in a:
    c=''.join(i)
    b.append(c)

for i in b:
    all_boxes[i]=['1','2','3','4','5','6','7','8','9']

del a
#del b
del c

def input_num():     # Function to take input from the user to fill the given boxes
    print("Enter the values")
    for i in b:
        a=input(i)
        if a=='':
            pass
        else:
            all_boxes[i]=list(a)

def column(x):    # To return the column of which 'x' is a part
    for i in ab:
        if x[0]==i:
            return list(i+str(j) for j in number)

def row(x):     # To return the row of which 'x' is a part
    for i in number:
        if x[1]==i:
            return list(str(j)+i for j in ab)

def box(x):     # To return the box of which 'x' is a part
    for i in e:
        for j in i:
            if j==x:
                return i

# For creating list of boxes

abc=['A','B','C']
defg=['D','E','F']
ghi=['G','H','I']

a123=['1','2','3']
a456=['4','5','6']
a789=['7','8','9']

abcd=[abc,defg,ghi]

a1234=[a123,a456,a789]

def gen_box():    # Generate box
    global boxes
    boxes=[]
    for i in abcd:
        for j in a1234:
            box=[]
            for k in i:
                for l in j:
                 box.append(list(itertools.product(k,l)))
            boxes.append(box)
    #return boxes

gen_box()
d=[]
for i in boxes:
    e=[]
    for j in i:
        f=[]
        for k in j:
            g=[]
            for l in k:
                c=''.join(l)
                g.append(c)
            f.append(g)
        e.append(f)
    d.append(e)

e=[]     # Final list with the list of boxes
for i in d:
    f=[]
    for j in i:
        for k in j:
            l=k[0]+k[1]
        f.append(l)
    e.append(f)

def solve_column(box,num):    # To remove the 'num' from the column of which 'box' is a part
    for i in column(box):
        if num in all_boxes[i]:
            if len(all_boxes[i])>1:
                all_boxes[i].remove(num)

def solve_row(box,num):     # To remove the 'num' from the row of which 'box' is a part
    for i in row(box):
        if num in all_boxes[i]:
            if len(all_boxes[i])>1:
                all_boxes[i].remove(num)

def solve_box(box1,num):   # To remove the 'num' from the boxe of which 'box' is a part
    for i in box(box1):
        if num in all_boxes[i]:
            if len(all_boxes[i])>1:
                all_boxes[i].remove(num)

def check_state():      # To check is the Sudoku is solved or not
    for i in all_boxes:
        if len(all_boxes[i])>1:
            return "Not_solved"
    else:
        return "Solved"

def solver():     # The main loop the solves the Sudoku
    while check_state()=="Not_solved":
        for i in all_boxes:
            if len(all_boxes[i])==1:
                solve_column(i,all_boxes[i][0])
                solve_row(i,all_boxes[i][0])
                solve_box(i,all_boxes[i][0])

def num_of_unsolved_boxes():    # To know the number of unsolved boxes
    n=0
    for i in all_boxes:
        if len(all_boxes[i])>1:
            n+=1
    return n

def print_grid():
    a = all_boxes
    print(a['A1'][0],a['A2'][0],a['A3'][0],'  ',a['A4'][0],a['A5'][0],a['A6'][0],'  ',a['A7'][0],a['A8'][0],a['A9'][0])
    print(a['B1'][0],a['B2'][0],a['B3'][0],'  ',a['B4'][0],a['B5'][0],a['B6'][0],'  ',a['B7'][0],a['B8'][0],a['B9'][0])
    print(a['C1'][0],a['C2'][0],a['C3'][0],'  ',a['C4'][0],a['C5'][0],a['C6'][0],'  ',a['C7'][0],a['C8'][0],a['C9'][0])
    
    print('')
    print('')
    
    print(a['D1'][0],a['D2'][0],a['D3'][0],'  ',a['D4'][0],a['D5'][0],a['D6'][0],'  ',a['D7'][0],a['D8'][0],a['D9'][0])
    print(a['E1'][0],a['E2'][0],a['E3'][0],'  ',a['E4'][0],a['E5'][0],a['E6'][0],'  ',a['E7'][0],a['E8'][0],a['E9'][0])
    print(a['F1'][0],a['F2'][0],a['F3'][0],'  ',a['F4'][0],a['F5'][0],a['F6'][0],'  ',a['F7'][0],a['F8'][0],a['F9'][0])
         
    print('')
    print('')
     
    print(a['G1'][0],a['G2'][0],a['G3'][0],'  ',a['G4'][0],a['G5'][0],a['G6'][0],'  ',a['G7'][0],a['G8'][0],a['G9'][0])
    print(a['H1'][0],a['H2'][0],a['H3'][0],'  ',a['H4'][0],a['H5'][0],a['H6'][0],'  ',a['H7'][0],a['H8'][0],a['H9'][0])
    print(a['I1'][0],a['I2'][0],a['I3'][0],'  ',a['I4'][0],a['I5'][0],a['I6'][0],'  ',a['I7'][0],a['I8'][0],a['I9'][0])

all_boxes = {'A1': ['5'], 'A2': ['4'], 'A3': ['1'], 'A4': ['8'], 'A5': ['3'], 'A6': ['2'], 'A7': ['9'], 'A8': ['7'], 'A9': ['6'], 'B1': ['9'], 'B2': ['2'], 'B3': ['3'], 'B4': ['5'], 'B5': ['6'], 'B6': ['7'], 'B7': ['1'], 'B8': ['8'], 'B9': ['4'], 'C1': ['8'], 'C2': ['7'], 'C3': ['6'], 'C4': ['4'], 'C5': ['1'], 'C6': ['9'], 'C7': ['3'], 'C8': ['2'], 'C9': ['5'], 'D1': ['2'], 'D2': ['9'], 'D3': ['5'], 'D4': ['6'], 'D5': ['4'], 'D6': ['1'], 'D7': ['7'], 'D8': ['3'], 'D9': ['8'], 'E1': ['1'], 'E2': ['3'], 'E3': ['7'], 'E4': ['9'], 'E5': ['5'], 'E6': ['8'], 'E7': ['6'], 'E8': ['4'], 'E9': ['2'], 'F1': ['6'], 'F2': ['8'], 'F3': ['4'], 'F4': ['2'], 'F5': ['7'], 'F6': ['3'], 'F7': ['5'], 'F8': ['9'], 'F9': ['1'], 'G1': ['4'], 'G2': ['6'], 'G3': ['8'], 'G4': ['3'], 'G5': ['9'], 'G6': ['5'], 'G7': ['2'], 'G8': ['1'], 'G9': ['7'], 'H1': ['7'], 'H2': ['5'], 'H3': ['9'], 'H4': ['1'], 'H5': ['2'], 'H6': ['4'], 'H7': ['8'], 'H8': ['6'], 'H9': ['3'], 'I1': ['3'], 'I2': ['1'], 'I3': ['2'], 'I4': ['7'], 'I5': ['8'], 'I6': ['6'], 'I7': ['4'], 'I8': ['5'], 'I9': ['9']}

start = time()
solver()
stop = time()
print(check_state())
duration = str(stop-start)
print('Solved in '+duration+' seconds')
print('')
print_grid()
