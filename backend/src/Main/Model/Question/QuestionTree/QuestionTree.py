# Le but de cette class est de represente un arbre de probilite affin de pouvoir choisire les poids
# Ex si je veux avoir plus de question de type geographie que d'histoire je pourais mettre un poids de larbre diffeent
import random

import backend
from backend.src.Main.Model.Question.question import Question

class QuestionTree:
    def __init__(self, name: str = "root", poids=1):
        self.name = name
        self.childs: [QuestionTree] = []
        self.poids = poids


    def add(self, child):
        self.childs.append(child)

    '''
    Alogoriment qui permet de tire au sort une feuille de l'arbre 
    
    Le principe est que tantque lon a pas une feuille on continue a decendre
    '''

    def getRandomQuestion(self):

        child = self.__getRandomChild__()
        while type(child) != backend.src.Main.Model.Question.QuestionTree.QuestionLeaves.QuestionLeaves:
            child = child.__getRandomChild__()

        feuille = child
        # On retoune une question quelquon de la liste
        return feuille.get_question()

    def get_question(self):
        return self.getRandomQuestion()
    '''
    Algo pour tire au sort des ellement dans une liste pondere
    
    Ex [ A = 30 % , B = 20 % , C = 50% ] 
    On peux reprsente cela par [A A A B B C C C C C]
    Si on tire le nombre 0.4 
    A la premiere iteration on sera a 0.3 donc on contiue
    A la seonde on sera a 0.5 on a donc trouve 
    
    Cette algoriment sapuis sur l'equiprobalite de tomber dans un ensemble (aka autent de chance de fait 0.1 que de faire 0.9 )
    '''

    def __getRandomChild__(self):
        sum = 0;
        # On conte le poids total
        for child in self.childs:
            sum += child.poids

        cnt = 0;
        # On tire un seuille
        rmd_number = random.random()
        for tree in self.childs:
            tree: QuestionTree = tree
            cnt += tree.poids
            # Si on depasse le num random cest que lon a trouve lellment
            if cnt > rmd_number:
                return tree
        return None

    '''
    Algo recusive pour trouve un fils ou petit fils qui porte le nom voulus
    '''

    def getTreeByName(self, name):
        # Cas trivialle : si jai le meme nom je marete et je retourne
        if self.name == name:
            return self

        # Si on ne trouve pas on parcoure tout les fils
        for child in self.childs:
            # SI le fils possede lui meme des enfant qui porte ce nom il nous les retourne
            res = child.getTreeByName(name)
            # Si lenfant nest pas None on le renvois si non on continus
            if res != None:
                return res
        # Si je ne trouve rien de renvois None
        return None



