# ***************************************************************************
# Author  : Debadatta Mishra
# Purpose : Deployment of application in Websphere 7 and 8 
# ***************************************************************************

# ************** START OF VARIABLES DECLARATION ******************

# Provide below the .war directory path
file_path = '/home/dist/';
# Provide below the .war file name only
war_file_name = 'corebank-server-war-db2-2.1-SNAPSHOT.war';
# Provide below the root context application name
application_name = 'corebank-server-war';
# Provide below the module name
moduleName = 'corebank-server'
# Provide below the Websphere application server version number
serverVersionNo = '7.0.0.17';
# Full War file path 
war_file_path = file_path+war_file_name;
# ibm-web-bnd.xmi file for enterprise application
ibm_bnd_xmi_file_path = file_path+'ibm-web-bnd.xmi'

# ************** END OF VARIABLES DECLARATION ******************

import time
server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*');
print server;
serverName = AdminControl.getAttribute(server, "name");
print serverName;
nodeName = AdminControl.getNode( );
print nodeName;
cellName = AdminControl.getCell( );
print cellName;

# **************** Uninstallation of existing application *********************
#AdminApp.uninstall(application_name);
#AdminConfig.save();

wasServerVarName = 'WebSphere:cell='+cellName+',node='+nodeName+',server='+serverName;
print wasServerVarName;

AdminApp.install(war_file_path, '[ -usedefaultbindings -defaultbinding.virtual.host default_host -defaultbinding.force -defaultbinding.strategy.file '+ibm_bnd_xmi_file_path+' -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname '+application_name+' -nocreateMBeansForResources -noreloadEnabled -deployws -validateinstall warn -processEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -allowDispatchRemoteInclude -allowServiceRemoteInclude -asyncRequestDispatchType SERVER_SIDE -nouseAutoLink -contextroot /'+application_name+' -MapModulesToServers [[ '+moduleName+' '+war_file_name+',WEB-INF/web.xml WebSphere:cell='+cellName+',node='+nodeName+',server='+serverName+' ]] -CtxRootForWebMod [[ '+moduleName+' '+war_file_name+',WEB-INF/web.xml /'+application_name+' ]]]' )
print "Saving the information"
AdminConfig.save();

print '\n*****************************************************\n'
print 'Application '+application_name+' Deployed Successfully';
print '\n*****************************************************\n'

# ************************* Change of ClassLoader Setting **************************
time.sleep(60)
application_name = "corebank-server-war"
AdminApplication.configureWebModulesOfAnApplication(application_name, application_name,"10000", "PARENT_LAST")
AdminConfig.save()

print '\n*****************************************************\n'
print 'Application Classloding Setting Modified Successfully';
print '\n*****************************************************\n'

time.sleep(60)

# *****************************Start the deployed application **********************
AdminControl.invoke('WebSphere:name=ApplicationManager,process=server1,platform=proxy,node='+nodeName+',version='+serverVersionNo+',type=ApplicationManager,mbeanIdentifier=ApplicationManager,cell='+cellName+',spec=1.0', 'startApplication', '['+application_name+']', '[java.lang.String]');
#print "Saving the information"
AdminConfig.save();
time.sleep(90)
print '\n*****************************************************\n'
print 'Application '+application_name+' Started Successfully';
print '\n*****************************************************\n'