# -*- coding: utf-8 -*-
from ClaseFechaHora import FechaHora

class Hora:
    __hora = 0
    __minuto = 0
    __segundo = 0
    
    def __init__(self,h,minu,seg):
        self.__hora = h
        self.__minuto = minu
        self.__segundo = seg
    
    def Mostrar(self):
        print('%.2d:%.2d:%.2d' % (self.__hora, self.__minuto, self.__segundo))
        self.Validar(self.__hora, self.__minuto, self.__segundo)
        
    def Validar(self,h,minu,seg):
        b = False
        if (type(h)==int) and (h in range (0,24)):
            if (type(minu)==int) and (minu in range (0,60)):
                if (type(seg)==int) and (seg in range (0,60)):
                    b = True
        
        if b == True:
            print('La hora son validas')
        else:
            print('La hora no son validas')
            
    def __add__(self, f):
        h=self.getHora() + f.getHora()
        m=self.getMinu() + f.getMinu()
        s=self.getSeg() + f.getSeg()
        return FechaHora(f.getDia(),f.getMes(),f.getAño(),h,m,s)
    
    def __radd__(self, f):
        h=self.getHora() + f.getHora()
        m=self.getMinu() + f.getMinu()
        s=self.getSeg() + f.getSeg()
        return FechaHora(f.getDia(),f.getMes(),f.getAño(),h,m,s)
    
    def getHora(self):
        return self.__hora
    
    def getMinu(self):
        return self.__minuto
    
    def getSeg(self):
        return self.__segundo