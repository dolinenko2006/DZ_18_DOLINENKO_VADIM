from dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()


    def get_one(self, gid):
        return self.dao.get_by_id(gid)


    def create(self, data):
        return self.dao.create(data)

    def updete(self, data):
        self.dao.update(data)
        return self.dao


    def delete(self, gid):
        self.dao.delete(gid)
