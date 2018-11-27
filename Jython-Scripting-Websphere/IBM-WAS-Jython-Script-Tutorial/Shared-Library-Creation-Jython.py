Jython Script Tutorial for IBM Websphere 7
------------------------------------------
# ***************************************************************************
# Author  : Debadatta Mishra
# Purpose : Shared Library Creation 
# ***************************************************************************
#Provide below Database specific helper name
name = 'DB2DataSourceHelper'
#Provide below the classpath
classpath = '/home'

#Ensure WAS_LIBS_DIR variable at Server level
varName = 'WAS_LIBS_DIR'
varValue = '${WAS_INSTALL_ROOT}/lib'
varDesc = ''

#Creation of class loader
dbHelperClsName = name

# ************** END OF VARIABLES DECLARATION ******************
import time

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )
n1 = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+'/')
print n1
library = AdminConfig.create('Library', n1, [['name', name], ['classPath', classpath]])
print library
AdminConfig.save()

print '\n**************************************************************\n'
print 'New Shared Library with the name '+name+' created successfully';
print '\n**************************************************************\n'









