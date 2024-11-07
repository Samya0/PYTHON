from models.Produit import Produit
from models.Commande import Commande

class Ligne_cmd:
    def __init__(self,produit:Produit, commande:Commande, quantite:float):
        self.produit=produit
        self.commande=commande
        self.quantite=quantite