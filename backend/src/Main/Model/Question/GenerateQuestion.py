import csv
import pathlib
#backend/ressouces/question.csv
from random import random

from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.question import Question

#Statistique pour le nombre de question :
# Question sur les drapeau : 197
# Question sur les captitalle : 197 (A faire)

list_csv_file=["question.csv"]
def generateQuestion(root_path="backend/ressouces/"):
    list_question = []
    for f in list_csv_file:
       questions= parseCSVQuestion(root_path+f)
       list_question.append(questions)
    return list_question

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

def getRandomQuestion(question_list : [Question]):
    return random.choice(question_list)