'''
Created on 

@author: prita
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","B1smillah!","dev" )
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old order by proId desc")
            else: 
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where proId = %s order by proId desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_usd(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where currency = 'USD' order by proId desc")
            else: 
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where proId = %s order by proId desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_cad(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where currency = 'CAD' order by proId desc")
            else: 
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where proId = %s order by proId desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_brl(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where currency = 'BRL' order by proId desc")
            else: 
                cursor.execute("SELECT proId, proTitle,leadOrg,leadCon, cost, currency FROM project_old where proId = %s order by proId desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_strategy(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM strategy order by id desc")
            else: 
                cursor.execute("SELECT * FROM strategy where id = %s order by id desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def read_species(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT * FROM species order by id desc")
            else: 
                cursor.execute("SELECT * FROM species where id = %s order by id desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def dashboard(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT *  FROM global_var order by id desc")
            elif id == 1:
                cursor.execute("SELECT *  FROM bar order by id desc")
            elif id == 2:
                cursor.execute("SELECT *  FROM line order by id desc")
            elif id == 3: 
                cursor.execute("SELECT * FROM pie order by id desc")
            else: 
                cursor.execute("SELECT * FROM global_var where id = %s order by proId desc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

            
    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        print("INSERT INTO project_old(proTitle,leadOrg,leadCon) VALUES(%s, %s, %s)", (data['proTitle'],data['leadOrg'],data['leadCon'],))
        try:
            cursor.execute("INSERT INTO project_old(proTitle,leadOrg,leadCon) VALUES(%s, %s, %s)", (data['proTitle'],data['leadOrg'],data['leadCon'],))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
            
    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE project_old set proTitle = %s, leadOrg = %s, leadCon = %s where proId = %s", (data['proTitle'],data['leadOrg'],data['leadCon'],id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
        
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM project_old where proId = %s", (id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()

    #select count(*) from strategy;
    #select count(*) from species;
    #select sum(cost) from project_old where currency='USD'
    #select sum(cost) from project_old where currency='CAD'
    #select sum(cost) from project_old where currency='Brazilian Real'

