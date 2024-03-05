#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 01:32:38 2022

@author: ako
"""

import images
import time

def immagine(x_min, y_min, x_max, y_max, pixel_width, max_deep):
    px_step = (x_max - x_min)/pixel_width
    pixel_height = int((y_max - y_min)/px_step)
    img = []
    for row in range(pixel_height):
        print(str(row)+"/"+str(pixel_height))
        y= y_max - px_step*row
        riga=[]
        
        for col in range(pixel_width):
            x= x_min + px_step*col
            c=Complex(x,y)
            
            color = (0,0,0)
            left = diverge(Complex(0.0, 0.0), c, max_deep)
            if left > 0:
                cc = min(255, int(((max_deep-left)/max_deep)*255))
                color = (cc,cc,cc)
                
            riga.append(color)
            
        img.append(riga)  
    return img

def diverge(z,c,left):
    if z.modulo_quadrato() > 4.0:
        return left #bianco
    if left == 0:
        return left #nero
    zout = z.quadrato().somma(c)
    return diverge(zout, c, left-1)

class Complex:
    
    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im
        pass

    def somma(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def quadrato(self):
        return Complex(self.re*self.re - self.im*self.im, 2*self.re * self.im)
    
    def modulo_quadrato(self):
        return self.re*self.re + self.im*self.im
    
    def __str__(self):
        return f"{self.re}, {self.im}"



ts = time.time()
filename="mandelbrot"+str(ts)+".png"
img=immagine(-1, -1, 1, 1.0, 400, 500)
print("Seconds: "+str(time.time()-ts))
images.save(img, filename)
