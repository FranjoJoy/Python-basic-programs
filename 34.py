def quadrant(x,y):
	if (x>0 and y>0):
		print "1st Quadrant"
	elif (x<0 and y>0):
		print "2nd Quadrant"
	elif (x<0 and y<0):
		print "3rd Quadrant"
	elif (x>0 and y<0):
		print "4th quadrant"
	elif (x==0 and y>0):
		print "positive y axis"
	elif (x==0 and y<0):
		print "negative y axis"
	elif (y==0 and x>0):
		print "positive x axis"
	elif (y==0 and x<0):
		print "negative y axis"
	else:
		print "point is at origin"

a,b=input("Enter the coordinates")
quadrant(a,b)




