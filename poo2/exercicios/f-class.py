class Movie:  # criando classe = modelo
    def __init__(self):
        self.name = ""
        self.yearLaunch = 0
        self.includePlan = False
        self.note = 0
        self.durationMinutes = 0

    def __str__(self):
        return f"Movie(name='{self.name}', year_launch={self.yearLaunch}, include_plan={self.includePlan}, note={self.note}, duration_minutes={self.durationMinutes})"


     # criar objeto
movie = Movie()
movie.name = "Álucard"
movie.yearLaunch = 2024
movie.includePlan = True
movie.note = 28
movie.durationMinutes = 288

print(movie)
