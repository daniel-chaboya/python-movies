import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <!-- Google Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
    <!-- Font Awesome -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #BDC3C7;
        }
        a {
            text-decoration: none !important;
        }
        a:hover {
             cursor:pointer;
        }
        small {
            text-align: left;
        }
        .navbar {
            padding-top: 25px;
            padding-bottom: 30px;
        }
        .navbar-header {
            float: left;
            padding: 15px;
            text-align: center;
            width: 100%;
        }
        .navbar-default .havbar-header .navbar-brand {
            color: '#D91E18'
        }
        .navbar-brand {
            float: none;
            font-family: 'Montserrat', sans-serif;
            font-size: 25px;
            color: 'red';
            font-weight: 700;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-content {
            margin-top: 60px;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .pop > div {
            width: 250px;
        }
        .pop .popover-title {
            background-color: #96281B;
        }
        .popover-title {
            color: #fff;
            font-size: 18px;
        }
        .popover-title small {
            font-size: 12px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
    
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.trailer-link', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });     
         
        // Animate movie tile display and prepare functionality of popover
        $(document).ready(function () {

            // Popover(on hover) for movie details.  Utilizes bootstrap popover functionality
            $(".popover-details").popover({html: true,
                    placement: "right",
                    trigger: "manual",
                    title: function () {
                        return $(this).siblings('.pop-title').text()
                    },
                    content: function () {
                        return $(this).siblings('.pop-content').html()
                    }
            }).on("mouseenter", function () {
                var _this = this;
                $(this).popover("show");
                $(".popover").on("mouseleave", function () {
                    $(_this).popover('hide');
                });
            }).on("mouseleave", function () {
                var _this = this;
                setTimeout(function () {
                    if (!$(".popover:hover").length) {
                        $(_this).popover("hide");
                    }
                }, 100);
            });
            
            //Animate the display of movie images once the DOM is ready.
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
           
        });
        
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" id="brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container movie-content">
      {movie_tiles}
    </div>
  </body>
</html>
'''

movie_tile_content = '''
<div class="pop movie-tile col-md-6 col-lg-4 " >
    <img class="popover-details" src="{poster_image_url}" width="220" height="342">
    <div class="pop-title hide">
        <h2>{movie_title}</h2>     
    </div>
    <div class="pop-content hide">
        <p><small>{storyline}</small></p>
        <div>
            <strong>Year:</strong>
            <span><small>{movie_year}</small></span>
        </div>
        <div>
            <strong>Director:</strong>
            <span>{movie_director}</span>
        </div>
        <hr/>
        <a class="trailer-link" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><i class="fa fa-video-camera"></i>&nbsp;Watch Trailer</a>
    </div>
</div>
'''
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            storyline=movie.storyline,
            movie_director=movie.director,
            movie_year=movie.movie_year,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    print(content)
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
