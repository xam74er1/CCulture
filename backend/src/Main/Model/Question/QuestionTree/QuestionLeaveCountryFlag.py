from pathlib import Path

from backend.src.Main.Model.Question.QuestionImage import QuestionImage
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves
from backend.src.Main.Model.Utils.Config import Config
from backend.src.Main.Model.Utils.SqliteDAO import DAOConnextion

"""
Question qui genere automatiqument des drapeaux de pays
"""
class QuestionLeaveCountryFlag(QuestionLeaves):

    def __init__(self,  name: str = "root", poids=1):
        super().__init__(None,name,poids)


    def get_question(self):
        row = DAOConnextion.select_random_country()
        flag_code :str= row[0][2]
        country_name = row[0][0]
        flag_name = flag_code[0]+flag_code[1];
        flag_name = flag_name.lower()
        path =Config.IMAGE_FILE+"country_flag/"+flag_name+".png";
        try:
            return QuestionImage("Quelle pays represente ce drapeau ?",country_name,path,True,category="geo")
        except :
            return None