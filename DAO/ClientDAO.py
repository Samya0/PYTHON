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
    def getOne(self,client_id:int)->Client:
        connection=get_connection()
        if connection:
            try:
                cursor=connection.cursor()
                cursor.execute("SELECT * FROM client WHERE client_id = %s", client_id)
                clientDetails=cursor.fetchall()
                return clientDetails
            except mysql.connector.Error as err:
                print(f"Error fetching client {err} ")
            finally:
                cursor.close() #to clean the cursor bu default in mysql no really need to close cursor just close connection but either way best practice to close it 
                connection.close()
    def getAll(self)-> list():
        connection=get_connection
        if connection:
            try:
                cursor=connection.cursor()
                cursor.execute("SELECT * FROM client")
                clientsDetails=cursor.fetchall()
                return clientsDetails
            except mysql.connector.Error as err:
                    print(f"Error fetching client {err} ")
            finally:
                cursor.close() 
                connection.close()




                

        
