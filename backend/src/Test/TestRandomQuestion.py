from backend.src.Main.Model.Question.GenerateQuestion import generateQuestion
from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves
from backend.src.Main.Model.Question.QuestionTree.QuestionTree import QuestionTree
from backend.src.Main.Model.Utils.Config import Config

Config.RESSOUCE_FILE = "../../../"+Config.RESSOUCE_FILE
Config.SQLITE_DATABASE_FILE =Config.RESSOUCE_FILE +"database.db"
Config.IMAGE_FILE = Config.RESSOUCE_FILE+"images/"

root :QuestionTree= generateQuestion("../../ressouces/")

cntmap = {}
i =0
while i <10:
    q : QuestionText = root.get_question()
    if q != None:
        print("categorie : "+q.category)
        i+=1
        if cntmap.get(q.category) ==None:
            cntmap[q.category] = 1
        else:
            cntmap[q.category] +=1
    else :
        print(q)

print(cntmap)