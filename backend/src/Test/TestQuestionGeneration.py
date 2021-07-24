from backend.src.Main.Model.Question.GenerateQuestion import generateQuestion
import pathlib
if __name__ == '__main__':
    pathlib.Path(__file__).parent.resolve()
    generateQuestion("../../ressouces/")