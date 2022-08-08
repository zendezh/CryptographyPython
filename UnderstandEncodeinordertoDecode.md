To know how to decode - we need to know how it was encoded. 

 Profesor used ord() to encode then used chr() to decode
 
### ord(character)
#### Convert an integer represening the Unicode of the specified character

### chr()
#### Returns a character from the specified Unicode code. This is the inverse of chr().

Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 

ord('€') (Euro sign) returns 8364. 

----------------------------------------------------


For example, I want to send you message > abc 
After encoding based on professor code you receive > 602115

-How did we got that number?

Look at the formula: 

### encode(s) 	= sum(ord(s[i])*2048^i for i in range (len(s))) 



Lets encode 'abc'



s[0] = 'a'  = index of a = 0
s[1] = 'b'	
s[2] = 'c'


2048^i 

2048^i 
2048^i 
2048^i 


encode(s) 	= sum(ord(s[i])*2048^i for i in range (len(s))) 		= 602115


encode ('abc')  	= 

		
			=  ord('a')*2048^0    +    ord('b')*2048^1    +   ord('c')*2048^2 
						
			
			=  97 x 2048   + 9

			
		= sum((97)*2048^0)+(98)*2048^1)+(99)*2048^2)) 		= 602115
	

		= 2145 + 




