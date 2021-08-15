from backend.src.Main.Model.Question.QuestionTree.QuestionLeaveCalculus import QuestionLeaveCalculus

q = QuestionLeaveCalculus()
for i in range(10):
    rep =q.get_question()
    print(rep.question+" = "+rep.response)
