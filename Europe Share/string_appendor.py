#legit = 0 
#cft = 1
pre = ''

prefix = pre + ','
suffix = ''

print("You are appending " +pre+ "'s to the beginning of each line.")

#-------------------------------------------------------------
#*************************************************************
#insert file name here... make sure it belongs in the same directory


file = input('Paste name of file here: ') 


#*************************************************************
#-------------------------------------------------------------


#-------------------------------------------------------------


with open(file +'.csv', 'r') as src:
    with open(file + '_appended_' +pre+ '.csv', 'w') as dest:
       for line in src:
           dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))
           
           
           
#-------------------------------------------------------------
           
#-------------------------------------------------------------   


print ("""\n     D  O  N  E  ! ! !  \n""" + file + """  
 is appended. """)


#-------------------------------------------------------------        
