import string
import random


class Player:
    def __init__(self, pseudo="default", last_session_id=""):
        self.uuid = self.generate_random_uuid(8);
        self.last_session_id = last_session_id;
        self.name: str = pseudo
        self.current_party_id = ""

        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def generate_random_uuid(self, size):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    def get_id(self):
        return self.uuid
