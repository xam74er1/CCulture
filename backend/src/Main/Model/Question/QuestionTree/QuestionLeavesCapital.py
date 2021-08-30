from backend.src.Main.Model.Question.QuestionImage import QuestionImage
from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves
from backend.src.Main.Model.Utils.Config import Config
from backend.src.Main.Model.Utils.SqliteDAO import DAOConnextion

"""
Question qui genere automatiqument des nom de captiatale
"""
class QuestionLeaveCapital(QuestionLeaves):

    def __init__(self,  name: str = "root", poids=1):
        super().__init__(None,name,poids)


    def get_question(self):
        row = DAOConnextion.select_random_country()
        capital = row[0][5]
        article = row[0][3]
        country_name = row[0][0]

        if(article==None):
            article = ""

        try:
            return QuestionText(question="Quelle est la capitale de "+article+" "+country_name+" ?",response=capital,category="geo")
        except :
            return None