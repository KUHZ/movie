import media
import fresh_tomatoes

toy_story = media.Movie("toy story",
                        "a boy with his toy that come to life",
                        "https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=c3986gGp3Qs")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "a marine on a alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/results?search_query=avatar")
#print(avatar.storyline)
#toy_story.show_trailer()

movie = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movie)

