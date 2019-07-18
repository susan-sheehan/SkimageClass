def compute (string):
   """Perform simple math based on string input. 
      Example '5+7' -> 12"""
    values =string.split(' ')
	num0 = float(values[0])
	num1 = float(values[2])
	operator=values[1]
	if operator =='+':
	     return num0 +num1
	elseif operator =='-':
	    return num0-num1
        elseif operator =="*":
	    return num0*num1
        elseif operator =='/':
	    return num0/num1
        else: 
	   msg=f'Unknonw operator:"{operatpr}"' 
	   msg +="choose from "+" and "-".'
	   raise ValueError ('msg')
