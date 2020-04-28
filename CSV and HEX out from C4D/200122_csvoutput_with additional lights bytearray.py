import c4d, math, random
from c4d.modules import mograph as mo
from c4d import Vector as v, utils as u, Matrix as m
import csv
import time

def print_byte_array(b):
    print ':'.join(x.encode('hex') for x in str(b))

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
def main():

    coldata1 = "F:/contentIPC21.hex"
    doc = c4d.documents.GetActiveDocument ()
    ctime = doc.GetTime() # Save current time

    # Get FPS and minimum + maximum frames
    fps = doc.GetFps()
    start = doc.GetMinTime().GetFrame(fps)
    end  = doc.GetMaxTime().GetFrame(fps)

    op = doc.SearchObject('sunmatrix') #search for object in c4d to store data
    op2 = doc.SearchObject('skymatrix') #search for object in c4d to store data
    op3 = doc.SearchObject('creepyman')
    op4 = doc.SearchObject('ledsSoloMorning')
    op5 = doc.SearchObject('ledsSoloEvening')

    with open(coldata1, 'wb') as f:


        #for frame in xrange(start,end+1):
        frame = 0
        #print c4d.BaseTime(frame,fps)
        while c4d.BaseTime(frame,fps) < doc.GetMaxTime():


            bt = c4d.BaseTime (frame, fps) #current frame,frame rate
            c4d.documents.SetDocumentTime (doc, bt)

            #print "Document time : ", doc.GetTime().GetFrame(fps)

            c4d.GeSyncMessage(c4d.EVMSG_TIMECHANGED)# make the timeline, timeslider etc. do an instant redraw.)
            c4d.EventAdd(c4d.EVENT_ANIMATE)
            md = mo.GeGetMoData(op)
            md2 = mo.GeGetMoData(op2)
            md3 = mo.GeGetMoData(op3)
            md4 = mo.GeGetMoData(op4)
            md5 = mo.GeGetMoData(op5)
            if md==None and md2 == None and md3 == None and md4 == None and md5 == None: return False

            cnt = md.GetCount()
            marr = md.GetArray(c4d.MODATA_CLONE)
            carr = md.GetArray(c4d.MODATA_COLOR)

            cnt2 = md2.GetCount()
            marr2 = md2.GetArray(c4d.MODATA_CLONE)
            carr2 = md2.GetArray(c4d.MODATA_COLOR)

            cnt3 = md3.GetCount()
            marr3 = md3.GetArray(c4d.MODATA_CLONE)
            carr3 = md3.GetArray(c4d.MODATA_COLOR)

            cnt4 = md4.GetCount()
            marr4 = md4.GetArray(c4d.MODATA_CLONE)
            carr4 = md4.GetArray(c4d.MODATA_COLOR)

            cnt5 = md5.GetCount()
            marr5 = md5.GetArray(c4d.MODATA_CLONE)
            carr5 = md5.GetArray(c4d.MODATA_COLOR)

            c4d.DrawViews()

            node_count = 0 #count node
            allcol = []
            for c, d, e,j,k in zip(carr,carr2,carr3,carr4,carr5):
                cx = c * 255 #multiply colour vals by 255 to get RGB
                r = int(cx[0])
                g = int(cx[1])
                b = int(cx[2])
                w = int((r+g+b)/10)

                if(r >= 254):
                    r = 254
                if(g >= 254):
                    g = 254
                if(b >= 254):
                    b = 254
                if(w >= 254):
                   w = 254



                dx = d * 255 #multiply colour vals by 255 to get RGB
                r2 = int(dx[0])
                g2 = int(dx[1])
                b2 = int(dx[2])
                w2 = int((r2+g2+b2)/10)

                if(r2 >= 254):
                    r2 = 254
                if(g2 >= 254):
                    g2 = 254
                if(b2 >= 254):
                    b2 = 254
                if(w2 >= 254):
                   w2 = 254

                ex = e * 255 #multiply colour vals by 255 to get RGB
                r3 = int(ex[0])
                g3 = int(ex[1])
                b3 = int(ex[2])
                w3 = int((r3+g3+b3)/10)

                if(r3 >= 254):
                    r3 = 254
                if(g3 >= 254):
                    g3 = 25
                if(b3 >= 254):
                    b3 = 254
                if(w3 >= 254):
                   w3 = 254


                jx = j * 255 #multiply colour vals by 255 to get RGB
                r4 = int(jx[0])
                g4 = int(jx[1])
                b4 = int(jx[2])
                w4 = int((r4+g4+b4)/10)

                if(r4 >= 254):
                    r4 = 254
                if(g4 >= 254):
                    g4 = 254
                if(b4 >= 254):
                    b4 = 254
                if(w4 >= 254):
                   w4 = 254

                kx = k * 255 #multiply colour vals by 255 to get RGB
                r5 = int(kx[0])
                g5 = int(kx[1])
                b5 = int(kx[2])
                w5 = int((r5+g5+b5)/10)

                if(r5 >= 254):
                    r5 = 254
                if(g5 >= 254):
                    g5 = 254
                if(b5 >= 254):
                    b5 = 254
                if(w5 >= 254):
                   w5 = 254

                allcol.append(r)
                allcol.append(r2)
                allcol.append(r3)
                allcol.append(r4)
                allcol.append(r5)

                allcol.append(g)
                allcol.append(g2)
                allcol.append(g3)
                allcol.append(g4)
                allcol.append(g5)

                allcol.append(b)
                allcol.append(b2)
                allcol.append(b3)
                allcol.append(b4)
                allcol.append(b5)

                allcol.append(w)
                allcol.append(w2)
                allcol.append(w3)
                allcol.append(w4)
                allcol.append(w5)


            ipcByteArray = bytearray()
            ipcByteArray.append(0xFF)


            ipcByteArray.extend(bytearray(allcol))

            node_count += 1


            c4d.EventAdd(c4d.EVENT_ANIMATE) #Adds a global event to Cinema 4Dâ€™s event queue. Results in a CoreMessage() message.

            frame += 1
            f.write(ipcByteArray) # write after every frame
    f.close()


if __name__=='__main__':
    main()