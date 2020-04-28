import c4d
from c4d.modules import mograph as mo
import csv
from c4d import utils


#set gh pos and rot

def main():
        
    #~~~~OPEN CSV FILE FOR GH POSITION DATA~~~~~~~~~~~ CHECKED 
    filepath = 'C:/Users/anam/Desktop/bch rotations/positions3.csv'
    
    GHPOS = [] #store position date from GH IN empty list
    
    data = open(filepath)
    csv_data = csv.reader(data)
    for row in csv_data:
       b = map(float,row)
       GHPOS.append(b)

    data.close()
  

    #~~~~~STORE X,Y,Z POS VECTORS FROM GH~~~~~~~~~~~~~~~~
    marrNew = [] # list of vectors for position    
    for pos in GHPOS:
        x = pos[0] #x items
        y = pos[1] #y items
        z = pos[2] #z items

        off = c4d.Vector(x,y,z) #GH POSITION DATA  
        newMatrix = c4d.Matrix(off)
        
        marrNew.append(newMatrix)
    
     
    #~~~~~~~SET GH MATRIX IN C4D~~~~~~~~~~~~~~~~~~~~~CHECKED
    setNewGHArr = md.SetArray(c4d.MODATA_MATRIX,marrNew,False) #set GH PIXEL 
    print marrNew