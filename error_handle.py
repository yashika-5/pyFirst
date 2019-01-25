#!/usr/bin/python2

from googlesearch import search
import webbrowser

try :
	x = raw_input("Enter one num :")
	
	y = raw_input("Enter sec num :")

	print int(x)+int(y)

except :
       	print "plz dekhkr type kr bhai"
	#webdata = search('calculator')
      # 	webbrowser.open_new_tab('https://www.calculator.com')

       	webbrowser.open_new_tab('https://www.google.com/search?q=calculator')

	
	
	
