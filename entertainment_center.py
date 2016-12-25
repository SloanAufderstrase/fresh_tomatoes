import media
import fresh_tomatoes


# four parameters od Movie() : movie_title, movie_storyline, poster_image, trailer_youtube

shawshank = media.Movie("The Shawshank Redemption","Two imprisoned men bond over a number of years,"
                        "finding solace and eventual redemption through acts of common decency",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")


inception = media.Movie("Inception","A thief, who steals corporate secrets through use of dream-sharing technology,"
                        "is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=_5VDKVqvo8M")

boyhood = media.Movie("Boyhood","The life of Mason, from early childhood to his arrival at college.",
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                        "https://www.youtube.com/watch?v=Ys-mbHXyWX4")

truman_show = media.Movie("The Truman Show","An insurance salesman/adjuster discovers"
                         "his entire life is actually a television show.",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg",
                        "https://www.youtube.com/watch?v=c3gI9ms8Fdc")


movies = [shawshank, inception, boyhood, truman_show]

fresh_tomatoes.open_movies_page(movies)
