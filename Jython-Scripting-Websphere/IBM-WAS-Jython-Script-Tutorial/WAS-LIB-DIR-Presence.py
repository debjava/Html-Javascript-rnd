# ***************************************************************************
# Author  : Debadatta Mishra
# Purpose : To Ensure WAS_LIB_DIR availability in IBM WAS 7
# ***************************************************************************

# ************** START OF VARIABLES DECLARATION ******************
#Declare below all your relevent variables
varName = 'WAS_LIBS_DIR'

# ************** END OF VARIABLES DECLARATION ******************
server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )

varMap = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+'/VariableMap:/')
print varMap

varEntries_str = AdminConfig.showAttribute(varMap,"entries")
if (len(varEntries_str) > 2):
	   varEntries_str =  varEntries_str[1:len(varEntries_str)-1] 
	   varEntries = varEntries_str.split(" ")
	   for var in varEntries:
	      name = AdminConfig.showAttribute(var,"symbolicName")
	      if(name == varName):
		    print "Variable "+varName+" already exists, no need to create once again"
