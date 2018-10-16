s=raw_input("Enter the sentence")
consonants=0
word=0
dig=0
qmark=0
s=" "+s
for i in s:
	x=i.lower()
	if x==" ":
		word=word+1
	elif x=="?":
		qmark=qmark+1
	elif x.isdigit():
		dig=dig+1
	elif ((x!="a")and(x!="e")and(x!="i")and(x!="o")and(x!="u")):
		consonants=consonants+1

print "number of consonants:" ,consonants
print "number of qestion marks:" ,qmark
print "number of digits:" ,dig
print "number of words" ,word



