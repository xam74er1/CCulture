import base64

from backend.src.Main.Model.Question.QuestionText import QuestionText


class QuestionImage(QuestionText):
    def __init__(self,question: str, response: str, imagePath="",isBase64 = True,url = "",id=0, category: str = "default"):
        super().__init__(question,response,id, category);
        self.image = ''
        self.type = str(type (self));
        self.isBase64 = isBase64;
        self.url = url;
        self.toBase64(imagePath);
        self.extention = imagePath.split(".")[-1]

    '''
    Image mise en base 64 pour evite que lon ne regarde l'url ou dans le dossier , car souvent les image porte le nom ce qui peux donne une reponce
    '''
    def toBase64(self,imagePath):
        with open(imagePath, "rb") as image_file:
            self.image = base64.b64encode(image_file.read())
        print(self.image)