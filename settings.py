####MONGODB SERVER DATABASE SETTINGS

host     = 'localhost'  #localhost or machine name(IGNORE FOR REPLICASET)
port     = None         #port number or leave empty and default to port 27017
name     = 'test'       #database name for regular DB instance or replicaset instance
user     = ''           #user name to database(IGNORE FOR REPLICASET)
password = ''           #user password to database(IGNORE FOR REPLICASET)

#####THE FOLLOWING OPTIONS APPLY ONLY TO REPLICA SET CONFIGURATION
#####PLEASE IGNORE THESE CONFIGURATION ON A REGULAR MONGODB SERVER CONFIGURATION
replicaName = None      #replica set name e.g. replicaName='set1'
hosts       = [] #replica host(s) e.g. hosts=['wsa.com:27017','wsa.com:27018']
