# ******************************************************************************************
# Author  : Debadatta Mishra
# Purpose : Filter Configuration in Websphere 7 and 8
# *******************************************************************************************

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )

scope = 'cells/'+cellName+'/nodes/'+nodeName+'/servers/'+serverName
print "SCOPE - "+scope

serid = AdminConfig.getid('/Server:'+serverName)
webid = AdminConfig.list('WebContainer',serid)
print "WebContainer = " +webid

AdminConfig.create('Property', webid, '[[validationExpression ""] [name "com.ibm.ws.webcontainer.invokefilterscompatibility"] [description ""] [value "true"] [required "false"]]') 
AdminConfig.save()

print '\n*****************************************************\n'
print 'Filter Configured Successfully';
print '\n*****************************************************\n'