from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves

"""
Question qui genere automatiqument des drapeaux de pays
"""
class QuestionLeaveCountryFlag(QuestionLeaves):
    country_list = None
    def __init__(self,  name: str = "root", poids=1):
        super(QuestionLeaveCountryFlag, self).__init__(None,name,poids)
        if self.country_list == None:
            self.readCountryList()

    def readCountryList(self):
        print ("hey")