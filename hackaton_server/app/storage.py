from app.model.tables import Profession


class storage(object):

    def __init__(self):
        sessions = {}



class DbSnapshot(object):

    def __init__(self):
        session = self.application.session
        self.professions = {profession.id: profession.name for profession in session.query(Profession)}




