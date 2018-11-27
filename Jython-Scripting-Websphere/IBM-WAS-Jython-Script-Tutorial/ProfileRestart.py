# ***********************************************
# Author  : Debadatta Mishra
# Purpose : Restarting the Profile in IBM WAS 7
# ***********************************************

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*');
print server;
serverName = AdminControl.getAttribute(server, "name");
print serverName;
nodeName = AdminControl.getNode( );
print nodeName;
cellName = AdminControl.getCell( );
print cellName;
serverObjectName = AdminControl.completeObjectName('type=Server,node=%s,process=%s,*' % ( nodeName, serverName ,))
# Restart the server.
AdminControl.invoke(serverObjectName, 'restart')
AdminConfig.save( )
print '\n*****************************************************\n'
print 'Restarting the profile, please wait a while ... '
print '\n*****************************************************\n'
time.sleep(30)