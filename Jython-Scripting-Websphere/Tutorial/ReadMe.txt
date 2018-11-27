How to execute the jython script for websphere
Go to F:\dev\websphere8\profiles\AppSrv01\bin location in command prompt.
The is the location of your profile bin directory.

wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Deployment\connectionpoolapp-undeploy.jy
wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Deployment\connectionpoolapp-deploy.jy


wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Deployment\number2textwebapp-undeploy.jy
wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Deployment\number2textwebapp-deploy.jy

wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Final-DS-Creation-Jython\Remove-Ds.jy
wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Final-DS-Creation-Jython\finalDS-JythonScript.jy


A full and final script to create datasource and deployment of application

wsadmin -lang jython -f D:\Jython-Scripting-Websphere\Deployment\datasource-deploy-script-full.jy