# ******************************************************************************************
# Author  : Debadatta Mishra
# Application servers > server1 > Web container
# Purpose : Enable servlet caching and Disable servlet request and response pooling IBM WAS 7
# *******************************************************************************************

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
print server
serverName = AdminControl.getAttribute(server, "name")
serid = AdminConfig.getid('/Server:'+serverName)
webid = AdminConfig.list('WebContainer',serid)
print "WebContainer = " +webid
AdminConfig.modify(webid, '[[sessionAffinityTimeout "0"] [enableServletCaching "true"] [disablePooling "true"] [defaultVirtualHostName "default_host"]]')
AdminConfig.save()
print '\n****************************************************************\n'
print 'Servlet caching enabled and servlet request disbaled Successfully';
print '\n****************************************************************\n'