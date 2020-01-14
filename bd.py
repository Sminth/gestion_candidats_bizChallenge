import pymysql

class lienBaseDeDonnee:
    def __init__(self):
        self.chaineconnexion= pymysql.connect(host="localhost",user="root",password="",db="bizchallenge")
        self.curseur=self.chaineconnexion.cursor()
        
    def select(self,nomtable):
        sql="select * from "+nomtable
        self.curseur.execute(sql)
        self.chaineconnexion.commit()
        return self.curseur.fetchall()

    def insert(self,nomtable,valeurs):
        sql="insert into "+nomtable+" (noms,solde,pseudo,passe) values (%s, %s, %s,%s)"
        self.curseur.execute(sql,valeurs)
        self.chaineconnexion.commit()

    #def update(self,nomtable,valeurs):
#insertBd = lienBaseDeDonnee()
#insertBd.insert("candidats",["denzel","500","denzo525","biz25"])      

#fonction update fonction supp

    
