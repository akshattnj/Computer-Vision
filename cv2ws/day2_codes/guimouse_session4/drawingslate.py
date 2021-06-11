# disclaimer: please note that the commented functions selectRegion() and dynamicCreateSlate()
#             have been commented out due to their dependency on the module pyautogui.
#             If you'd like to use them as well install pyautogui, its a fairly straightforward
#             process and pyautogui is a verrrry useful library.  

# ===============================================================================================
'''
Instructions pour utiliser (thats french for "instructions to use") (I'm funny like that..)

1. create an object:
    One object per drawing slate. So if you want multiple drawing slates you can do that.
'''
    # eg> slate1 = slate('name of the slate')
'''
2. You have two options here:
    use static or dynamic create.
  
    a. If you decide to use staticCreateSlate(), you wont need the additional library 'pyautogui'
'''      
      # eg> slate1.staticCreateSlate( (x,y), image )    x,y being the position of the slate.
'''
    b. If you wanna use dynamicCreateSlate(), you will need the additional library 'pyautogui'
'''
      # eg> slate1.dynamicCreateSlate() 
'''
3. Simply Show it:
''' 
   # eg> slate1.showSlate(value)          value --> when you press this key the slate closes
   #                                      value has to be an ascii value. 
   #                                      tip : use ord() to find ascii values 
# ===============================================================================================

import cv2
import numpy as np
# import pyautogui as pg


# def selectRegion():
        
#     input('move mouse to position of left upper corner and press enter ')
#     LUC =  pg.position()
#     input('move mouse to position of right lower corner and press enter ')
#     RLC = pg.position()
#     size = (RLC[0] - LUC[0], RLC[1] - LUC[1])
#     pos = tuple(LUC)
#     return pos,size

class slate:
    def __init__(self,name):
        self.touch = False
        self.name = name
        self.sheet = None
        self.thickness = 2
        self.colour = [0,0,0]
        
    def staticCreateSlate(self,position,image):  # hardcoded slate create

        self.sheet = image               
        cv2.namedWindow(self.name,cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.name,position[0],position[1])       

    # def DynamicCreateSlate(self):

    #     pos,size = selectRegion()
    #     size = (size[1], size[0], 3)            
    #     self.sheet = np.zeros(size, np.uint8)
    #     cv2.namedWindow(self.name,cv2.WINDOW_AUTOSIZE)
    #     cv2.moveWindow(self.name,pos[0],pos[1])
    
    def createAllTrackBars(self):

        cv2.createTrackbar('B',self.name,0,255,self.BtrackbarCall)
        cv2.createTrackbar('G',self.name,0,255,self.GtrackbarCall)
        cv2.createTrackbar('R',self.name,0,255,self.RtrackbarCall)
        cv2.createTrackbar('W',self.name,1,20,self.WtrackbarCall)

    def BtrackbarCall(self,value):
        self.colour[0] = value
       
    def GtrackbarCall(self,value):
        self.colour[1] = value
      
    def RtrackbarCall(self,value):
        self.colour[2] = value
      
    def WtrackbarCall(self,value):
        self.thickness = value
      
    def showSlate(self,key = 27):                # key parameter has to be int 
        self.createAllTrackBars()
        cv2.setMouseCallback(self.name, self.chalk)
        while True:
            cv2.imshow(self.name,self.sheet)
            if cv2.waitKey(1) == key:       
                break
        cv2.destroyWindow(self.name)
        
    def chalk(self,event,x,y,flags,param):
        global prevX,prevY

        if event == cv2.EVENT_LBUTTONDOWN:
            self.touch = True
            prevX,prevY = x,y
            
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.touch == True:
                cv2.line(self.sheet, (prevX,prevY) , (x,y) , tuple(self.colour) , self.thickness )
                prevX,prevY = x,y

        elif event == cv2.EVENT_LBUTTONUP:
            self.touch = False
            cv2.line(self.sheet, (prevX,prevY) , (x,y) , tuple(self.colour) , self.thickness )
            prevX,prevY = x,y

        return x,y
    



