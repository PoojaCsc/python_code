import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys which come alive",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

hugo = media.Movie("Hugo",
                   "A boy and his atomatron",
                   "https://upload.wikimedia.org/wikipedia/en/7/73/Hugo_Poster.jpg",
                   "https://www.youtube.com/watch?v=kI-k8CuAZSw")

#print(toy_story.storyline)
#toy_story.show_trailer()

movies = [toy_story,hugo]

#fresh_tomatoes.open_movies_page(movies)

print(hugo.__doc__)
print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.VALID_RATINGS)