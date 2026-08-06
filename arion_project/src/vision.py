from dataclasses import dataclass
import cv2, numpy as np
@dataclass
class Detection:
    found: bool; bbox: tuple|None; center: tuple|None; area_ratio: float; confidence: float
class ColorDetector:
    def __init__(self,cfg):
        self.lo=np.array(cfg['hsv_lower'],np.uint8); self.hi=np.array(cfg['hsv_upper'],np.uint8); self.min=float(cfg['min_area_px'])
    def detect(self,rgb):
        hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV); m1=cv2.inRange(hsv,self.lo,self.hi); m2=cv2.inRange(hsv,np.array([170,self.lo[1],self.lo[2]],np.uint8),np.array([179,self.hi[1],self.hi[2]],np.uint8)); mask=cv2.morphologyEx(m1|m2,cv2.MORPH_OPEN,np.ones((5,5),np.uint8)); cs,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if not cs:return Detection(False,None,None,0,0)
        c=max(cs,key=cv2.contourArea); area=float(cv2.contourArea(c))
        if area<self.min:return Detection(False,None,None,0,0)
        x,y,w,h=cv2.boundingRect(c); return Detection(True,(x,y,w,h),(x+w/2,y+h/2),area/(rgb.shape[0]*rgb.shape[1]),min(1,area/(self.min*8)))
class AlphaBetaTracker:
    def __init__(self,a=.75,b=.08): self.a=a; self.b=b; self.p=None; self.v=np.zeros(2)
    def update(self,z,dt):
        if self.p is None:self.p=np.array(z,float); return self.p.copy()
        pred=self.p+self.v*dt; r=np.array(z)-pred; self.p=pred+self.a*r; self.v=self.v+(self.b/max(dt,1e-6))*r; return self.p.copy()
    def predict(self,dt):
        if self.p is None:return None
        self.p=self.p+self.v*dt; return self.p.copy()
