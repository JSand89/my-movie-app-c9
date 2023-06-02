from ...models.movie import Movie

def test_movie_attributes():
    movie = Movie(title="Test Movie", overview="This is a test movie", year=2023, time=2.5, date_release="2023-06-01", release_country="USA")
    
    assert movie.title == "Test Movie"
    assert movie.overview == "This is a test movie"
    assert movie.year == 2023
    assert movie.time == 2.5
    assert movie.date_release == "2023-06-01"
    assert movie.release_country == "USA"
