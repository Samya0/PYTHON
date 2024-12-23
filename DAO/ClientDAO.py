import mysql.connector
from config.database import get_connection
from DAO.dao import BaseDAO
from models.Client import Client

class ClientDAO:

    def create(self,client:Client):
        connection=get_connection()
        if connection:
            try:
                cursor= connection.cursor()
                sqlUser="INSERT INTO user (nom, email, password) VALUES (%s,%s,%s)"
                cursor.execute(sqlUser,(Client.getName(), Client.getLogin(), Client.getPassword()))
                 # Retrieve the last inserted user_id
                user_id=cursor.lastrowid() #last row id
                sqlClient="INSERT INTO client (user_id, numerp) VALUES (%s,%s)"
                cursor.execute(sqlClient, (user_id,Client.getNumero())) 
                connection.commit()
            except mysql.connector.Error as err:
                connection.rollback()
                print(f"Error during insert: {err}") 
            finally:
                cursor.close()
                connection.close()   
    # def getOne():
        
