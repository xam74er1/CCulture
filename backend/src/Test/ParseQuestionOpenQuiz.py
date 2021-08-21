from backend.src.Main.Model.Question.GenerateQuestion import parseCSVQuestionFromOpenQuiz

list = parseCSVQuestionFromOpenQuiz("../../ressouces/fromage.csv")
for q in list:
    print(q.question+" "+q.response)