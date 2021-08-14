import os

from backend.src.Main.Model.Question.QuestionTree.QuestionLeaveCountryFlag import QuestionLeaveCountryFlag
from backend.src.Main.Model.Utils.Config import Config
from backend.src.Main.Model.Utils.SqliteDAO import DAOConnextion

Config.RESSOUCE_FILE = "../../../"+Config.RESSOUCE_FILE
Config.SQLITE_DATABASE_FILE =Config.RESSOUCE_FILE +"database.db"
Config.IMAGE_FILE = Config.RESSOUCE_FILE+"images/"


qlcf = QuestionLeaveCountryFlag()
qlcf.get_question()