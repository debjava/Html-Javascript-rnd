# ******************************************************************************************
# Author  : Debadatta Mishra
# Application servers > server1 > Process definition > Java Virtual Machine
# Purpose : Addition of Generic JVM Argument in IBM WAS 7
# *******************************************************************************************

server = AdminControl.queryNames('node='+AdminControl.getNode( )+',type=Server,*')
serverName = AdminControl.getAttribute(server, "name")
nodeName = AdminControl.getNode( )

AdminTask.setJVMProperties('[-serverName '+serverName+' -nodeName '+nodeName+' -verboseModeClass false -verboseModeGarbageCollection false -verboseModeJNI false -initialHeapSize 256 -maximumHeapSize 1024 -runHProf false -hprofArguments -debugMode false -debugArgs "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7779" -genericJvmArguments "-Ddefault.client.encoding=UTF-8 -Dlog4j.configuration=log4j.debug.properties -Dcorniche.server.debug=true -Dwicket.configuration=deployment" -executableJarFileName -disableJIT false]')
AdminConfig.save()

print '\n*****************************************************\n'
print 'Generic JVM Argument Configured Successfully';
print '\n*****************************************************\n'