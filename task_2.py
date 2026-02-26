class Movies:
    def __init__(self):
        # инициализируем пустой список фильмов
        self.movies = []

    def add_movie(self, movie):
        # добавляем фильм в конец списка
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        # используем логику родительского класса
        super().add_movie(movie)
        # возвращаем строку нужного формата
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


# Вызовы по условию задания
comedy = Comedy()
print(comedy.add_movie("Большой куш"))

drama = Drama()
print(drama.add_movie("Оружейный барон"))
