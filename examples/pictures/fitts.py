from pymt import *

c = Widget()

for i in range (10):
		img_src = 'bilder/testpic'+str(i+1)+'.jpg'
		x , y =  i/5*300+150, i%5*200+100
		b = ZoomableImage(img_src, parent=c,  pos = (x,y))
			
		c.add_widget(b)
		
		
		
w = UIWindow()
w.add_widget(c)
w.set_fullscreen()
runTouchApp()