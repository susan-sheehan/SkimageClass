def compute (string):
    values =string.split(' ')
	num0= int(values[0])
	num1=int(values[2])
	operator=values[1]
	if operator =='+':
	     return num0 +num1
	elseif operator =='-':
	    return num0-num1
        else: 
	   msg=f'Unknonw operator:"{operatpr}"' 
	   raise ValueError ('msg')
