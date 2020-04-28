import c4d
from c4d.modules import mograph as mo
import csv
from c4d import utils


#set gh pos and rot

def main():
    pass
#---------CSV ROTATION DATA RADIANS----------------------

       
filepath = 'C:/Users/anam/Desktop/bch rotations/rotations3.csv'
    
GHROTS = [] #store rotation date from GH IN empty list
    
data = open(filepath)
csv_data = csv.reader(data)
    
for row in csv_data:
    b = map(float,row)
    GHROTS.append(b)

data.close()


anglelist = []
for angle in GHROTS:
#---------STORE ANGLES IN A LIST ----------------------    
    H = angle[0] #x items
    P = angle[1] #y items
    B = angle[2] #z items
    
    hpb = c4d.Vector(P,B,-H) #REMEMBER TO NEGATE THE ANGLES POTENTIALLY FROM GH
  
    anglelist.append(hpb)
    
obj = doc.SearchObject("baked clones 3")
child = obj.GetChildren()


for c,d in zip(child,anglelist):
    m = c.GetMg() #GET MATRIX 
    
    pos = m.off #GET POSITION DATA
      
    m = utils.HPBToMatrix(d) #SET A NEW MATRIX WITH GH ANGLES
  
    m.off = pos
 
    c.SetMg(m) #SET THE ANGLE MATRIX TO THE CURRENT MARTIX