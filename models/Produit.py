
class Produit:
    def __init__(self,id_produit:int,libelle:str,prix:float)->None:
        self.__id_produit=id_produit
        self.libelle=libelle
        self.prix=prix
    

    def __repr__(self) -> str:
        return f'{self.__id_produit},{self.libelle},{self.prix}'
    
    def getIDProduit(self)->int:
        return self.__id_produit