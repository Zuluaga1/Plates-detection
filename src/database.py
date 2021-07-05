# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:02:34 2021

@author: esteb
"""
import pymysql
import datetime

class DataBase():
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost', #ip si la base es remota
            user = 'root',
            password = '',
            db = 'placas',
            port = 8111,
            )
        self.cursor = self.connection.cursor() #para seleccionar de la base
        print("conexión con la base de datos establecida")
    
    def select(self,id): #select a un usuario
        sql = 'SELECT * FROM entrada WHERE idEntrada = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone() #one es para obtener un solo registro
            print('placa',user[1])
            print('time',user[2])
            return user
        except Exception:
            print("HAY un error en la consulta con la db")
            raise
            
    def select_all(self): #select a varios
        sql = 'select * from entrada'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print("id", user[0])
                print('placa:' ,user[1])
                print('fecha' ,user[2])
                print("____\n")
                return users
        except Exception:
             print("HAY un error en la consulta con la db")
             raise 
             
    def select_all_sal(self): #select a varios
        sql = 'select * from salida'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print("id", user[0])
                print('placa:' ,user[1])
                print('fecha' ,user[2])
                print("____\n")
                return users
        except Exception:
             print("HAY un error en la consulta con la db")
             raise 
             
    def insert(self, placa, fecha):
        sql = "INSERT INTO entrada(PLACA, FECHA) values('{}', '{}')".format(placa, fecha)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit() #guardar cambios en db
        except Exception:
            raise
            
    def insert_sal(self, placa, fecha):
        sql = "INSERT INTO salida(PLACA, FECHA) values('{}', '{}')".format(placa, fecha)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit() #guardar cambios en db
        except Exception:
            raise
        
    def close(self):
        self.connection.close()
        
#db = DataBase()
#ejeje= db.select_all()
#time1 = datetime.datetime.now()
#time1 = time1.strftime('%Y-%m-%d %H:%M:%S')
#placa = 'MXL931'
#h =db.select_all()
#db.insert(placa,time1)

#db.close()


















