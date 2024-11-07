from models.Produit import Produit
class Commande:
    def __init__(self, id_commande:int, reference:int, date: str, produits:list[Produit])->None:
        self.__id_commande=id_commande
        self.__reference=reference
        self.date=date
        self.produits=produits
       
       

    def __repr__(self)-> str:
        products, = [p.produit_id for p in self.produits]
        return f'{self.__id_commande},{self.__reference},{self.date},{products}'
    
    def getIDCommand(self)->int:
        return self.__id_commande
    
    def getReference(self)->int:
        return self.__reference
    
    def setReference(self, nvReference:int)->None:
        self.__reference=nvReference