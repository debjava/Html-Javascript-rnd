#----------------------------------------------------
# Author : Debadatta Mishra
# Comments : Datasource creation for DB2 in IBM WAS 7
#-----------------------------------------------------

# ************** START OF VARIABLES DECLARATION ******************

dbname = "ccdemo1"
DB_ServerHost = "192.168.100.223"
PortNumber = "50000"
jdbcName = 'DB2JDBC1';
alias1 = 'ccdemo1';
user = 'ccdemo1';
password = 'ccdemo1'
datasource = "DB2DS"
jndiName = "DB2DS"

# ************** END OF VARIABLES DECLARATION ******************

#------------------------------------------------
# JDBC Provider Creation
#------------------------------------------------
jdbc_driver = '${DB2UNIVERSAL_JDBC_DRIVER_PATH}/db2jcc.jar;${UNIVERSAL_JDBC_DRIVER_PATH}/db2jcc_license_cu.jar;${DB2UNIVERSAL_JDBC_DRIVER_PATH}/db2jcc_license_cisuz.jar;'
server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )
serverId1 = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+'/')
print serverId1

## Creating New JDBC Provider ##
print " Creating New JDBC Provider :"+ jdbcName
n1 = ["name" , jdbcName ]
desc = ["description" , "One-phase commit DB2 JCC provider"]
impln = ["implementationClassName" , "com.ibm.db2.jcc.DB2ConnectionPoolDataSource"]
classpath = ["classpath" , jdbc_driver ]
providerType = ["providerType" , "DB2 Universal JDBC Driver Provider"]
nativePath = ["nativepath" ,'${DB2UNIVERSAL_JDBC_DRIVER_NATIVEPATH}']
attrs1 = [n1 , impln , desc , classpath , nativePath,providerType]
#attrs1 = [n1 , impln , desc , classpath]
cell = AdminControl.getCell()
#Serverid = AdminConfig.getid('/Cell:'+ cell +'/')		
#print Serverid
jdbc = AdminConfig.create('JDBCProvider' , serverId1 , attrs1)
print " New JDBC Provider created :"+ jdbcName 
AdminConfig.save()
print " Saving Configuraion " 
print " ---------------------------- End of JDBC Provider Creation --------------------------- "

#------------------------------------------------
# J2C Authentication Data Creation
#------------------------------------------------
cell = AdminControl.getCell();
sec = AdminConfig.getid('/Cell:'+ cell +'/Security:/');
print sec;
## J2C Authentication Entries ##
print " Creating New JAASAuthData with Alias name :"+ alias1
alias_attr = ["alias" , alias1]
desc_attr = ["description" , alias1]
userid_attr = ["userId" , user ]
password_attr = ["password" , password]
attrs = [alias_attr , desc_attr , userid_attr , password_attr ]
authdata = AdminConfig.create('JAASAuthData' , sec , attrs)
print " Saving Configuraion "
AdminConfig.save()
print " ----------------------- End of J2C Authentication Data Creation ----------------------- "

#------------------------------------------------
# Datasource Creation in Websphere
#------------------------------------------------
server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
print serverName
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )
ds = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+''+'/JDBCProvider:'+ jdbcName) 
#print ds;
name1 = ["name" , datasource]
jndi = ["jndiName" , jndiName]
authentication = ["authDataAlias" , alias1]
ds_hlpclass = ["datasourceHelperClassname" , "com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper"]
map_configalias_attr=["mappingConfigAlias", "DefaultPrincipalMapping"]
map_attrs=[authentication , map_configalias_attr]
mapping_attr=["mapping", map_attrs]
ds_attr = [name1 , jndi , authentication , ds_hlpclass ,mapping_attr]
newds = AdminConfig.create('DataSource' , ds , ds_attr)
print " New DataSource created with name :"+ datasource 
AdminConfig.save()
print " Saving Configuraion "

#------------------------------------------------
# Setting the DB2 Property
#------------------------------------------------

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
print serverName
nodeName = AdminControl.getNode( )
cellName = AdminControl.getCell( )
newds1 = AdminConfig.getid('/Cell:'+cellName+'/Node:'+nodeName+'/Server:'+serverName+''+'/JDBCProvider:'+ jdbcName +'/DataSource:'+ datasource)
print newds1;

psAttr = ["propertySet", []]
attrs = []
attrs.append(psAttr)
AdminConfig.modify(newds1, attrs)

#--------------------------------------------------------------
# Add desired custom properties to the DataSource.
#--------------------------------------------------------------
 
dbnameAttr = [["name", "databaseName"], ["value", dbname], ["type", "java.lang.String"]]
svrnameAttr = [["name", "serverName"], ["value", DB_ServerHost], ["type", "java.lang.String"]] 
portAttr = [["name", "portNumber"], ["value", PortNumber], ["type", "java.lang.String"]]
drivertypeAttr = [["name", "driverType"], ["value", "4"], ["type", "java.lang.Integer"]]
#pretestsqlAttr = [["name", "preTestSQLString"], ["value", sqlString], ["type", "java.lang.String"]]

newsprops = []
newsprops.append(dbnameAttr)
newsprops.append(svrnameAttr)
newsprops.append(portAttr)
newsprops.append(drivertypeAttr)
#newsprops.append(pretestsqlAttr)

psAttr = ["propertySet", [["resourceProperties", newsprops]]]
attrs = [psAttr]
AdminConfig.modify(newds1, attrs)
# print AdminConfig.showall(dataSource)
#--------------------------------------------------------------
# Save All 
#-------------------------------------------------------------- 
print "Success! DataSource Created! Saving the configuration"
AdminConfig.save( )

print '\n*****************************************************\n'
print 'DataSource Creation Successfull.... '
print '\n*****************************************************\n'
AdminConfig.save( )
#--------------------------------------------------------------
# Restarting the Profile 
#-------------------------------------------------------------- 
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
