from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)


    def get_one(self, mid):
        return self.dao.get_by_id(mid)


    def create(self, data):
        return self.dao.create(data)

    def updete(self, data):
        self.dao.update(data)
        return self.dao


    def delete(self, mid):
        self.dao.delete(mid)
