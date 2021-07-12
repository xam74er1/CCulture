class Reponse:
    def __init__(self,compteur,user,reponse):
        self.compteur=compteur
        self.user=user
        self.reponse=reponse
    def getReponse(self,compteur):
        if self.compteur==compteur:
            return self
    
