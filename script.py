import pyautogui as pag
import time

delay = 0.5 #time between next messages

positions = {
	"A" : "top",
	"B" : "jungle",
	"C" : "mid",
	"D" : "adc",
	"E" : "supp"
}

print('Pick a position(pick a letter):')
print('A. top')
print('B. jungle')
print('C. mid')
print('D. adc')
print('E. supp')

pos = input('Choice: ')
pos = pos.upper()
try:
	print('Position picked: ' + positions[pos])
	
	while True:
		time.sleep(delay)
		print('Typing...')
		pag.typewrite(positions[pos])
		pag.press("enter")
	
except:
	print('Wrong letter')
	input('Press enter to exit...')