for i in range(1, 10):  #pyramid will run until 9th line
   temporary_list = [] #create list variable
   for b in range(i, i ** 2 + 1, i): #loop equation for pyramid pattern
      temporary_list.append(str(b)) #attach loop to list

   print(" ".join(temporary_list)) #get rid of list brackets and add space between numbers to make it look like a pyramid
   
