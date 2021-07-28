from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.QuestionTree.QuestionTree import *

if __name__ == '__main__':
    #Objectife cree des arbre pondere

    root = QuestionTree(1,"root")

    enfantA = QuestionTree(2,"enfant A")

    list_question_BA = [QuestionText("Question A", "Reponce A"), QuestionText("Question B", "Reponce B"),QuestionText("Question C", "Reponce C")]
    enfantAA = QuestionLeaves(list_question_BA, "enfant B", 1)

    list_question_BB = [QuestionText("Question A", "Reponce A"), QuestionText("Question B", "Reponce B"),QuestionText("Question C", "Reponce C")]
    enfantAB = QuestionLeaves(list_question_BB, "enfant B", 3)

    enfantA.add(enfantAB)
    enfantA.add(enfantAA)


    list_question_A = [QuestionText("Question A","Reponce A"),QuestionText("Question B","Reponce B"),QuestionText("Question C","Reponce C")]
    enfantB = QuestionLeaves(list_question_A,"enfant B",3)

    root.add(enfantA); #Enfant A proba : 2/5
    root.add(enfantB) #Enfant B probat 3/5




