#Mandelbrot Set Program
#Graphs the Mandelbrot set iteratively (function is NOT recursive)
#Written by Dr. Mo, Fall 2019
import pygame
import math
import cmath

pygame.init()  
pygame.display.set_caption("mandelbrot")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))

#mandelbrot function definition------------------------ 
def mandelbrot(c):
    z = complex(0,0);
    count = 0;
    while abs(z) < 2 and count < 80: 
        z = z * z + c;
        count+=1;
    return count;
#end mandelbrot function--------------------------------

#-------------------------------------------------------
#in C++, this would be the start of main----------------

t = -2 #lower bound for real axis
while t<2: #upper bound for real (horizontal) axis
    t+=.01 #make this number SMALLER to increase picture resolution
    
    m = -2 #lower bound for imaginary axis
    while m<2: #upper bound for imaginary (vertical) axis
        m+=.01 #make this number SMALLER to increase picture resolution
        
        c = complex(t, m) #create a complex number from iterators
        num = mandelbrot(c); #call the function

        #these if statements are just to differentiate the colors more, not needed if you want black & white image
        if num < 20:
            screen.set_at((int(t * 200 + 400), int(m * 200 + 400)), (num*8, num*6, num*12))
        elif num<40:
            screen.set_at((int(t * 200 + 400), int(m * 200 + 400)), (num*2, num/2, num*6))
        elif num is 80:
            screen.set_at((int(t * 200 + 400), int(m * 200 + 400)), (255,255,255))
        else:
            screen.set_at((int(t * 200 + 400), int(m * 200 + 400)), (num*3, num/2, num*2))

        pygame.display.flip()#this actually puts the pixel on the screen
        
        
pygame.time.wait(10000)#pause to see the picture
pygame.quit()#quit pygame
