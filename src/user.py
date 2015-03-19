#/usr/bin/env python3

import time

class User(object):
    def __init__(self,user_id=None):
        if user_id == None:
            self.new_user = True
            user_id = self.time.time()
        else:
            self.new_user = False
            #self._populateUser() 

    def commit(self):
        if self.new_user:
            pass
        else:
            #Do UPDATES 
            pass
        
    def delete(self):
        if self.new_user == False:
            return False
        	
#class Table(object):
 #   def __init__(self, table_id=None):
  #      if table_id == None:
   #         self.new_table = True
    #        table_id =  




