#WebContainer Custom Property Filter Configuration


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

-----------------------------------------------------------------------------------------------------------

# Create shared library

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )

n1 = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+'/')
print n1

library = AdminConfig.create('Library', n1, [['name', 'DB2DataSourceHelper'], ['classPath', '/home']])
print library
AdminConfig.save() 
-----------------------------------------------------------------------------------------------------------------------

    # Create a class loaderr
        applicationServer = AdminConfig.list("ApplicationServer")
        params = [];
        params.append(["mode", "PARENT_FIRST"]);
        ParentFirstClassLoader = AdminConfig.create("Classloader", applicationServer, params)
        print "Created Parent Last Class Loader: " + ParentFirstClassLoader;
 
    # Add the shared library to the class loader.
    params = [];
    params.append(["libraryName", "DB2DataSourceHelper"]);
    params.append(["sharedClassloader", "true"]);
    AdminConfig.create("LibraryRef", ParentFirstClassLoader, params)
 
    print "Using Shared Library: " + sharedLibraryId;
AdminConfig.save()


# Installation of Corebank-server-war
AdminApp.install('corebank-server-war-db2-2.1-SNAPSHOT.war', '[ -usedefaultbindings -defaultbinding.virtual.host default_host -defaultbinding.force -defaultbinding.strategy.file /opt/IBM/WebSphere/Profiles/DefaultAppSrv01/wstemp/1566246272/upload/ibm-web-bnd.xmi -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname corebank-server-war-db2-2_1-SNAPSHOT_war -nocreateMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -processEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -allowDispatchRemoteInclude -allowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -contextroot /corebank-server-war -MapModulesToServers [[ corebank-server corebank-server-war-db2-2.1-SNAPSHOT.war,WEB-INF/web.xml WebSphere:cell=CloudBurstCell_2,node=CloudBurstNode_2,server=server1 ]] -CtxRootForWebMod [[ corebank-server corebank-server-war-db2-2.1-SNAPSHOT.war,WEB-INF/web.xml /corebank-server-war ]]]' ) 


#Core bank backoffice installation

AdminApp.install('corebank-backoffice-war-2.1-SNAPSHOT.war', '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname corebank-backoffice-war-2_1-SNAPSHOT_war -nocreateMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -processEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -allowDispatchRemoteInclude -allowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -contextroot /corebank-backoffice-war -MapModulesToServers [[ corebank-backoffice corebank-backoffice-war-2.1-SNAPSHOT.war,WEB-INF/web.xml WebSphere:cell=CloudBurstCell_2,node=CloudBurstNode_2,server=server1 ]] -MapWebModToVH [[ corebank-backoffice corebank-backoffice-war-2.1-SNAPSHOT.war,WEB-INF/web.xml default_host ]] -CtxRootForWebMod [[ corebank-backoffice corebank-backoffice-war-2.1-SNAPSHOT.war,WEB-INF/web.xml /corebank-backoffice-war ]]]' ) 


