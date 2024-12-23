from config.database import get_connection
from flask import Flask, request, jsonify
from DAO.UserDAO import UserDAO
from models.User import User
import os
from dotenv import load_dotenv


load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Initialize the database connection
db_connection = get_connection()

# Set up a basic route
@app.route("/")
def home():
    return "Hello, Flask!"
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    try:
        user_dao = UserDAO()
        # Fetch the user details using the DAO
        user_details = user_dao.getOne(user_id)
        
        # Check if user was found
        if user_details:
            #the jsonify can read either a list or a dictionnary not a list of tuple
            user_data = {
                "id": user_details[0][0],       
                "nom": user_details[0][1],      
                "login": user_details[0][2],    
                "password": user_details[0][3]  
            }
            return jsonify({"user": user_data}), 200
        else:
            # If no user is found
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
@app.route('/user', methods=['GET'])
def get_All_User():
     try:
        cursor=db_connection.cursor()
        sql="SELECT * FROM user"
        cursor.execute(sql)
        user_details=cursor.fetchall()# return a list of tuples
        print(user_details)
        users_list=[]
        for each_user in user_details:
             user_data={
                  "id": each_user[0],"nom":each_user[1], "email":each_user[2],"password":each_user[3]
             }
             users_list.append(user_data)
        return jsonify({"users":users_list}), 200

     except Exception as e:
          return jsonify({"error": str(e)}), 500
   

if __name__ == "__main__":
    # Set the port from environment or use default 8080
    port = int(os.getenv("PORT", 8080))
    # Run the Flask app
    app.run(host="0.0.0.0", port=port)
