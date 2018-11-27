# ********************************************************************************
# Author  : Debadatta Mishra
# Purpose : Creation of class loader and assoication DB Helper Class in IBM WAS 7
# ********************************************************************************

# ************** START OF VARIABLES DECLARATION ******************

dbHelperClsName = 'DB2DataSourceHelper'

# ************** END OF VARIABLES DECLARATION ******************

applicationServer = AdminConfig.list("ApplicationServer")
params = [];
params.append(["mode", "PARENT_FIRST"]);
ParentFirstClassLoader = AdminConfig.create("Classloader", applicationServer, params)
print "Created Parent Last Class Loader: " + ParentFirstClassLoader;

print '\n*****************************************************\n'
print 'Class Loader Created Successfully';
print '\n*****************************************************\n'

AdminConfig.save()
# Add the shared library to the class loader.
params = [];
params.append(["libraryName", dbHelperClsName]);
params.append(["sharedClassloader", "true"]);
AdminConfig.create("LibraryRef", ParentFirstClassLoader, params)
AdminConfig.save()

print '\n*****************************************************\n'
print 'Class Loader Created and Associated with Successfully';
print '\n*****************************************************\n'