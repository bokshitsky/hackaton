import frontik.handler
from app.model.tables import Profession
from app.storage import DbSnapshot


class Page(frontik.handler.PageHandler):
    def get_page(self):
        # backer = Profession(id = 1, name='Пекарь')
        # self.application.session.add(backer)
        # self.application.session.commit()


        str = self.application.session.query(Profession).get(1).name

        snapshot = DbSnapshot(self.application.session)

        self.json.put({
            'text': 'Hello, world1! ' + str + ' ' + snapshot.professions.get(1)
        })
