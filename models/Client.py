from models.User import User
from models.Commande import Commande
class Client(User):
    def __init__(self,user_id:str, nom:str,login:str,password:str,numero:str)->None:
        super().__init__(user_id,nom,login,password)
        self.__numero=numero
        self.commandes=[]


    def __repr__(self)->str:
        return f'{super().__repr__(),self.__numero}'
    
    def getNumero(self)->str:
        return self.__numero
    
    def setNumero(self,nvNumero:str)-> None:
        self.__numero = nvNumero
    
    def addCommand(self, command: Commande)->None: #None mean the method will not return anything she does it's job and doesn't return anything
        self.commandes.append(command)