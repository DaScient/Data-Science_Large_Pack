import collections
#legit = 0 
#cft = 1

prefix = ''
suffix = ''
#*************************************************************
#insert file name here... make sure it belongs in the same directory
file = input('Paste name of file here: ') 
#*************************************************************
#-------------------------------------------------------------
with open(file +'.csv', 'r') as src:
    with open(file + '_appended_cont' +prefix+ '.csv', 'w') as dest:
        for line in src:
            c = collections.Counter(line)
            print(c[line], line.index(0,end = ''))
            dest.write(' %s%s%s\n' % (prefix, line.rstrip('\n'), suffix))  
#-------------------------------------------------------------
print ("""\n     D  O  N  E  !  \n""" + file + """  
 is appended. """)
#-------------------------------------------------------------        
