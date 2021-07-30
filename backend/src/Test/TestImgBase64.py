from backend.src.Main.Model.Question.QuestionImage import QuestionImage

question = QuestionImage("comment s'appele ce chat ?", response="chat kira",
              imagePath="../../ressouces/images/Test/chatKira.jpg", isBase64=True, category="Test")

print(question.image);