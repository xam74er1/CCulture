import string
import random


class Player:
    def __init__(self,pseudo = "default",last_session_id=""):
        self.uuid = self.generateRandomUUID(8);
        self.last_session_id = last_session_id;
        self.name : str = pseudo
        self.curent_party_id =""

        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def generateRandomUUID(self,size):

        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
    def get_id(self):
        return self.uuid