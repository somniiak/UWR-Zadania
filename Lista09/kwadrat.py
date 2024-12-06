import turtle as t

BOK = 25
SX = -100
SY = 0

def kwadrat(x, y, kolor):
    t.fillcolor(kolor)
    t.pu()
    t.goto(SX + x * BOK, SY + y * BOK)
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.fd(BOK)
        t.rt(90)
    t.end_fill() 

t.tracer(0,1)
print ('Zmienna __name__ =', __name__)    

if __name__ == '__main__':
    t.speed('fastest')    
    kolory = ['red', 'green', 'blue']
        
    for i in range(10):
        kwadrat(i,i, kolory[i % 3])    

    
    input()    
