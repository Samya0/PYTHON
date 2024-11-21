from flask import Flask, request, jsonify
from models.User import User
from DAO.UserDAO import UserDAO

app=Flask(__name__) #flask constructor

user_dao = UserDAO()


@app.route('/user', methods=['POST'])

def create_user():
    try:
        data = request.get_json()
 
        user = User(nom=data['nom'],login=data['email'],password=data['password'])

        user.setName(data['name'])
        user.setLogin(data['email'])
        user.setPassword(data['password']) #need to be hashed 

        user_dao.create(user)
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/user/<int:user_id ', methods=['PUT']) 
def update_user():
    try:
        data=request.get_json()
        user=User(id=data['id'],nom=data['nom'],login=data['email'],password=data['password'])
        if 'name' in data:
                user.setName(data['nom'])
        if 'email' in data:
                user.setLogin(data['email'])
        if 'password' in data:
                user.setPassword(data['password'])
                
        user_dao.update_user(user)       
        return jsonify({"message":"User updated successfully"}),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
       
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    try:
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
def get_All():
     try:
        users=UserDAO.getAll() # return a list of tuples
        users_list=[]
        for each_user in users:
             user_data={
                  "id": each_user[0],"nom":each_user[1], "email":each_user[2],"password":each_user[3]
             }
             users_list.append(user_data)
        return jsonify({"users":users_list}), 200

     except Exception as e:
          return jsonify({"error": str(e)}), 500
        
     
     