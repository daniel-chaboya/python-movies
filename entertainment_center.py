'''
Communicates between the media module \
which has the constructor to build the \
movie instances, and the fresh tomatoes \
modules which creates the html page \
that displays the movies and plays the trailers.
'''

import fresh_tomatoes
import media

#test get_movi

#create movie instances
rs = media.get_movie("reservoir dogs")
reservoir_dogs = media.Movie(rs['Title'],
                             rs['Director'],
                             rs['Year'],
                             rs['Plot'],
                             rs['Poster'],
                             "https://www.youtube.com/watch?v=vayksn4Y93A",
                             "https://www.youtube.com/watch?v=vayksn4Y93A")

bcwc = media.get_movie("black cat, white cat")
black_cat_white_cat = media.Movie(bcwc['Title'],
                                  bcwc['Director'],
                                  bcwc['Year'],
                                  bcwc['Plot'],
                                  bcwc['Poster'],
                                  "https://www.youtube.com/watch?v=drTgrPzSd-Y",
                                  "https://www.youtube.com/watch?v=X1wN_KHr4Ng")

cc = media.get_movie("coffee and cigarettes")
coffee_and_cigarettes = media.Movie(cc['Title'],
                                    cc['Director'],
                                    cc['Year'],
                                    cc['Plot'],
                                    cc['Poster'],
                                    "https://www.youtube.com/watch?v=mM6Mpn0-eyQ",
                                    "https://www.youtube.com/watch?v=k1hAilewhdY")
h = media.get_movie("helvetica")
helvetica = media.Movie(h['Title'],
                        h['Director'],
                        h['Year'],
                        h['Plot'],
                        h['Poster'],
                        "https://www.youtube.com/watch?v=7JkpYgjbYRg",
                        "https://www.youtube.com/watch?v=CttXWjR1dr4")

fb = media.get_movie("ferris bueller's day off")
ferris_beuller = media.Movie(fb['Title'],
                        fb['Director'],
                        fb['Year'],
                        fb['Plot'],
                        fb['Poster'],
                        "https://www.youtube.com/watch?v=0KFVLWX7eEY",
                        "https://www.youtube.com/watch?v=0KFVLWX7eEY")

rb = media.get_movie("raging bull")
raging_bull = media.Movie(fb['Title'],
                        rb['Director'],
                        rb['Year'],
                        rb['Plot'],
                        rb['Poster'],
                        "https://www.youtube.com/watch?v=YiVOwxsa4OM",
                        "https://www.youtube.com/watch?v=YiVOwxsa4OM")


'''Create an array of movies.  \
This gets passed into the open_movies_page function \
on the fresh tomates module.'''
movies = [reservoir_dogs, black_cat_white_cat, coffee_and_cigarettes, helvetica, ferris_beuller, raging_bull]

#build fresh_tomatoes.htlm page. Pass in array of movie instances.
fresh_tomatoes.open_movies_page(movies)
