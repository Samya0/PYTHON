import mysql.connector
from config.database import get_connection
from DAO.dao import BaseDAO
from models.User import User



class UserDAO:
        
    def create(self, user: User):
        connection = get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO user (nom, email, password) VALUES (%s, %s,%s)" #placeholder prevent from sql injection
                cursor.execute(sql, (user.getName(), user.getLogin(), user.getPassword))
                connection.commit()
            except mysql.connector.Error as err:
                connection.rollback()
                print(f"Error during insert: {err}")  #need a roolback to improve next time
            finally:
                cursor.close()
                connection.close()
    
    def getOne(self, userId : int) -> User:
        connection=get_connection()
        if connection:
            try:
                cursor=connection.cursor()
                sql= "SELECT * FROM user WHERE id=%s"
                cursor.execute(sql, (userId))
                user_details=cursor.fetchall()
                return user_details
            except mysql.connector.Error as err:
                print(f"Error during get user:{err}")
            finally:
                cursor.close()
                connection.close()

    def getAll(self)->list():
        connection=get_connection()
        if connection:
            try:
                cursor=connection.cursor()
                sql="SELECT * FROM user"
                cursor.execute(sql)
                user_details=cursor.fetchall()
                return user_details
            except mysql.connector.Error as err:
                print(f"Error during get user:{err}")
            finally:
                cursor.close()
                connection.close()
        
    def update_user(self, user:User):
        connection =get_connection()
        if connection:
            try:
                cursor=connection.cursor()
                if user.getName():
                    sql="Update user set nom=%s WHERE id=%s"
                    cursor.execute(sql,(user.getName(),user.getUserId()))
                    connection.commit()
                if user.getPassword():
                    sql="Update user set password=%s where id=%s"
                    cursor.execute(sql,(user.getPassword(),user.getUserId()))
                    connection.commit()    #bad practice to commit multiple times to improve after
                if user.getLogin():
                    sql="Update user set email=%s where id=%s"
                    cursor.execute(sql,(user.getLogin(),user.getUserId()))
                    connection.commit() #bad practice to commit multiple times to improve after
            except mysql.connector.Error as err:
                connection.rollback()
                print(f"Error during updating {err} ")
            finally:
                cursor.close()
                connection.close()

    #we can not delete a user we can add a column to table is_active and we delete(not really)we set it to false->bool to improve after


        
