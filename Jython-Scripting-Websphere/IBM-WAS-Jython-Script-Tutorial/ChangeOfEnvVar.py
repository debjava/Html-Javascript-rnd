# ********************************************************************************
# Author  : Debadatta Mishra
# Purpose : Change of Host Name and Port in IBM WAS 7
# ********************************************************************************

# ************** START OF VARIABLES DECLARATION ******************

war_file_name = 'bootstrap.war';
application_name = 'bootstrap';

# ************** END OF VARIABLES DECLARATION ******************
HostName = 'HostName'
PortNo = 'PortNo'
hostValue = AdminControl.getHost()
print hostValue
NamedEndPointIDs = AdminConfig.getid('/NamedEndPoint:/').split(lineSeparator)
for y in NamedEndPointIDs:
	s1 = AdminConfig.showAttribute(y,'endPointName')
	#print s1;
	if s1 == 'WC_defaulthost':
		ss = AdminConfig.showAttribute(y,'endPoint')
		PortValue = AdminConfig.showAttribute(ss,'port')
		print PortValue
		AdminApp.edit(application_name, '[ -MapEnvEntryForWebMod [[ '+war_file_name+' '+war_file_name+',WEB-INF/web.xml '+HostName+' String "" '+hostValue+' ][ '+war_file_name+' '+war_file_name+',WEB-INF/web.xml '+PortNo+' String "" '+PortValue+' ]]]' )
		AdminConfig.save()
		AdminConfig.save()
print '\n*****************************************************\n'
print 'Application '+application_name+' Modified Successfully';
print '\n*****************************************************\n'		
time.sleep(30)