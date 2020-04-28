import c4d

from c4d.modules import mograph as mo
import socket




UDP_IP = "192.168.1.12"
UDP_PORT = 7864

def main():
    md = mo.GeGetMoData(op)
    if md is None: return False

    cnt = md.GetCount()
    marr = md.GetArray(c4d.MODATA_MATRIX)

    fall = md.GetFalloffs()


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data
    sock.close()

    fingerdictC4D = eval(data) # convert to dictionary again from string
    fingers = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky'] # list to sort the dictionary
   #get position y of each unicorn
    marrNew = [] # new vectors matrix
    for im,m in enumerate(marr):

        positions = m.off #obtain position data
        xpos = positions[0]
        ypos = positions[1]
        ypos = fingerdictC4D[fingers[im]]
        zpos = positions[2]


        off = c4d.Vector(xpos,ypos,zpos)
        newMatrix = c4d.Matrix(off)
        marrNew.append(newMatrix)

             #set new position vector with new leap yposiiton
             #create new matrix
             #append matrix to empty list
    #set new y position for each clone

    setNewArr = md.SetArray(c4d.MODATA_MATRIX,marrNew,False) # set new cloner matrix

#each finger is linked to each row

