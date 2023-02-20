from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director


class MovieDAO:

    def __init__(self, session):
        self.session = session
        self.model = Movie


    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['director_id']).all()

        elif filters['genre_id']:
            return self.session.query(self.model).filter(
                self.model.genre_id == filters['genre_id']).all()

        elif filters['year']:
            return self.session.query(self.model).filter(
                self.model.year == filters['year']).all()

        return self.session.query(self.model).all()


    def get_by_id(self, mid):
        return self.session.query(self.model).get(mid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        mid = data.pop('id')   #    pop = get
        movie = self.get_by_id(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)

            self.session.add(movie)
            self.session.commit()


    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()


