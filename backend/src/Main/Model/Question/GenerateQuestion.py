import csv
import pathlib
#backend/ressouces/question.csv
from random import random

from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaveCalculus import QuestionLeaveCalculus
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaveCountryFlag import QuestionLeaveCountryFlag
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves
from backend.src.Main.Model.Question.QuestionTree.QuestionLeavesCapital import QuestionLeaveCapital
from backend.src.Main.Model.Question.QuestionTree.QuestionTree import QuestionTree
from backend.src.Main.Model.Question.question import Question

#Statistique pour le nombre de question :
# Question sur les drapeau : 197
# Question sur les captitalle : 197 (A faire)

root : QuestionTree = None

list_csv_file=["question.csv"]
#Source : https://www.openquizzdb.org/
list_open_quiz_file_generale =["general_1.csv","harry_potter.csv","start_wars.csv","princesse_disney.csv","fromage.csv","vin.csv"]
list_open_quiz_categorie = [["histoire","date_20_em_siecle.csv"],["histoire","bataille.csv"],["histoire","histoire_france.csv"]]
def generateQuestion(root_path="backend/ressouces/"):

    root = generatreTreeRoot()

    default_q : QuestionLeaves = root.getTreeByName("default")

    for path in list_open_quiz_file_generale:
        question_list = parseCSVQuestionFromOpenQuiz(root_path+path)
        default_q.question_list += question_list
    for item in list_open_quiz_categorie:
        categorie = item[0]+"_question"
        print(categorie)
        path = item[1]
        leaves : QuestionLeaves= root.getTreeByName(categorie)
        question_list = parseCSVQuestionFromOpenQuiz(root_path + path,categorie=categorie)
        leaves.question_list+=question_list



    return root;
    list_question = []
    for f in list_csv_file:
       questions= parseCSVQuestion(root_path+f)
       list_question.append(questions)
    return list_question

def generatreTreeRoot():
    root : QuestionTree = QuestionTree()

    #Fils direct
    science : QuestionTree = QuestionTree(name="science",poids=3)
    geo :QuestionTree = QuestionTree(name="geo",poids=6)
    histoire:QuestionTree = QuestionTree(name="histoire",poids=4)
    autre :QuestionTree = QuestionTree(name="autre",poids=10)

    #Ajout
    root.add(geo)
    root.add(science)
    root.add(histoire)
    root.add(autre)

    #Science
    science_question = QuestionLeaves([],name="science_question",poids=4)
    calcule = QuestionLeaveCalculus(name="calcule",poids=1)

    science.add(science_question)
    science.add(calcule)

    #Geo
    geo_question = QuestionLeaves([],name="geo_question",poids=1)
    drapeau = QuestionLeaveCountryFlag(name="drapeau",poids=4)
    capital = QuestionLeaveCapital(name="capital",poids=4)

    geo.add(geo_question)
    geo.add(drapeau)
    geo.add(capital)

    #Histoire
    histoire_question = QuestionLeaves([],name="histoire_question")
    histoire.add(histoire_question)

    #generale
    default_question = QuestionLeaves([],"default",poids=1)
    autre.add(default_question)

    return root






def parseCSVQuestion(file_path:str):
    list_question = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        isFisrtRow = True
        for row in reader:
            #On ignore la premiere ligne
            if not isFisrtRow:
                #La categorie n'est pas toujours presente
                categorie = "default"
                if len(row) > 2:
                    categorie = row[2]
                question = QuestionText(row[0],row[1],categorie)
                list_question.append(question)
            else:
                isFisrtRow = False
    return list_question

def parseCSVQuestionFromOpenQuiz(file_path,categorie="default"):
    list_question = []
    with open(file_path, 'r',encoding="UTF-8") as file:
        reader = csv.reader(file,delimiter=';')
        isFisrtRow = True
        for row in reader:
            if len(row)>4 and row[1] == "fr":
                question = QuestionText(row[2], row[3], category=categorie)
                list_question.append(question)
    return list_question


def getRandomQuestion(question_list : [Question]):
    return random.choice(question_list)