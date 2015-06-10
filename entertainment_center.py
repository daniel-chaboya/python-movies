import fresh_tomatoes
import media


black_cat_white_cat = media.Movie("Black Cat, White Cat",
                                  "Emir Kustirica",
                                  "1998",
                                  "Gypsy mobsters, dirty deals and shotgun weddings. This could be the start of a beautiful friendship.",
                                  "http://upload.wikimedia.org/wikipedia/en/e/e4/Poster1234.jpg",
                                  "https://www.youtube.com/watch?v=drTgrPzSd-Y",
                                  "https://www.youtube.com/watch?v=X1wN_KHr4Ng")

coffee_and_cigarettes = media.Movie("Coffee and Cigarettes",
                                    "Jim Jarmusch",
                                    "2003",
                                    "A series of vignettes that all have coffee and cigarettes in common.",
                                    "http://upload.wikimedia.org/wikipedia/en/8/8d/Coffee_and_Cigarettes_movie.jpg",
                                    "https://www.youtube.com/watch?v=mM6Mpn0-eyQ",
                                    "https://www.youtube.com/watch?v=k1hAilewhdY")

helvetica = media.Movie("Helvetica",
                        "Gary Hustwit",
                        "2007",
                        "A documentary about typography, graphic design, and global visual culture.",
                        "http://upload.wikimedia.org/wikipedia/commons/2/28/HelveticaSpecimenCH.svg",
                        "https://www.youtube.com/watch?v=7JkpYgjbYRg",
                        "https://www.youtube.com/watch?v=CttXWjR1dr4")

movies = [black_cat_white_cat, coffee_and_cigarettes, helvetica]

fresh_tomatoes.open_movies_page(movies)
