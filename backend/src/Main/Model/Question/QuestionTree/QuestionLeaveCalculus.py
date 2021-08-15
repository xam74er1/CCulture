import random

from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.QuestionTree.QuestionLeaves import QuestionLeaves


class QuestionLeaveCalculus(QuestionLeaves):
    sign_list = ["+","-","/","*"]
    def __init__(self,  name: str = "root", poids=1):
        super().__init__(None,name,poids)

    def get_question(self):
        eq= self.generate_equoition(["+","-","/","*"])
        res = eval(eq)
        #Si on a une divition un resulta non entier on recomence mais en simplifian pour avoir un resulta entier
        if res%1 != 0:
            print("PBR")
            eq= self.generate_equoition(["+","-","*"])
            res = eval(eq)
        return QuestionText("Resoudre le calcule suivant : "+eq,"La solution est : "+str(res))

    def generate_equoition(self,sign_list):
        formule ="";

        #Une chance sur 2 d'avoir des parenthese

        formule += "("+self.sub_sequence()+")"



        sign = random.choice(sign_list)
        if sign == "/" :
            formule += self.divistion(formule)
        else :
            formule += sign+"("+self.sub_sequence()+")"
        return formule


    def sub_sequence(self):
        formule = ""
        formule += self.random_numer()

        sign = random.choice(self.sign_list)

        if sign == "/":
            formule+=self.divistion(formule)
        else :
            formule +=  sign + self.random_numer()
        return formule

    #Le but est de definire un calcule qui fasse une divistion entiere
    """
    @:arg Une expretion matematique qui est sois de la forme (a+-b) sois de la forme (i*j) avec [i,j] € [1,9] donc arg est forcement un nombre dont les facteur premier son inferire a 10
    """
    def divistion(self,arg : str):
        #print("arg : "+arg)
        num = eval(arg)
        if num == 0 or num == 1:
            return "*("+self.sub_sequence()+")"

        primes = self.prime_factors(num)
        max = int(random.random()*min(len(primes),3))
        #Pour avoir des truc un peux plus interesseq que a/a
        if max == 1 and primes[1] == num:
            max=2
        #print("Max : "+str(max))
        if len(primes) == 1 or max ==1:
            return "/"+str(primes[0])
        elif len(primes) >1:
            #On melange la liste
            random.shuffle(primes)
            #On met le premier numbre
            formule ="/("+str(primes[0])
            #borne max

            #On multuplie les autre
            for i in range(1,max):
                formule +="*"+str(primes[i])
            formule+=")"
            return formule
        else:
            return "/"+str(num)


    def random_numer(self):
        return str(random.randint(1,9))

    def prime_factors(self,m):
        i = 2
        factors = []
        n = abs(m)
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(int(i))
        if n > 1:
            factors.append(int(n))
        return factors