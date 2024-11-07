class User:
    def __init__(self,user_id:int, nom:str,login:str,password:str)->None:
        self._user_id=user_id #protected
        self._nom=nom  #protected
        self._login=login #protected
        self._password=password #protected

    def __str__(self)-> str:
        return f'{self._user_id},{self._nom},{self._login},{self._password}'
    
    #user_id getter
    def getUserId(self)->int:
        return self._user_id
    
    #name getter
    def getName(self)-> str:
        return self._nom
    
    #login getter
    def getLogin(self)->str:
        return self._login
    
    #password getter
    def getPassword(self)-> str:
        return self._password
    
    #pas de setter id

    #nom setter
    def setName(self,nouveauNom:str)-> None:
        self._nom = nouveauNom  #we need to check if it is an instance of 
    
    #login setter
    def setLogin(self,nvlogin:str)-> None:
        self._login = nvlogin 

    def setPassword(self,nvpassword:str)-> None:
        self._password = nvpassword