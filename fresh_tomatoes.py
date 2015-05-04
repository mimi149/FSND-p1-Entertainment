import webbrowser
import os
import re

main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
  
    <link href="css/styles.css" rel="stylesheet" type="text/css">
    <script src="js/script.js"></script>
   
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
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Entertainment</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container" stype="backgroud-color: #A0A193">
        {tab}
    </div>
  </body>
</html>
'''

# The main page UI with 4 tabs

entertain_tabs = '''
<div class="tabs">
    <ul class="tab-links">
        <li class="active"><a href="#tab1">Movies</a></li>
        <li><a href="#tab2">classical Music</a></li>
        <li><a href="#tab3">Classical Crossover Music</a></li>
        <li><a href="#tab4">Pop Music</a></li>
    </ul>
 
    <div class="tab-content">
        <div id="tab1" class="tab active">
            <p>{movie_content}</p>
        </div>
        <div id="tab2" class="tab">
            <p>{classical_music_content}</p>
        </div>
        <div id="tab3" class="tab">
            <p>{classical_crossover_music_content}</p>
        </div>
        <div id="tab4" class="tab">
            <p>{pop_music_content}</p>
        </div>
    </div>
</div>
'''

# A single movie entry html template

movie_tile_content = '''
<div class="col-md-6 col-lg-4 text-center"  style="display: block;padding-bottom: 40px">
    <div class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}"
        data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" style="width:220px; height:342px">
    </div>
    <div>
        <mytip class="mytooltip top" href="#">
            <h3>{movie_title}</h3>
            <span class="txt text-left">
                <li>Title: {movie_title}
                <li>Director: {director}
                <li>Actor: {actor}
                <li>Release: {data_release}
                <li>Duration: {duration}
            </span>
        </mytip>  
    </div>
    <div class="row"></div>
    <div>
        <a href="JavaScript:void(0)"  data-toggle = "popover" data-trigger="focus"
            title="{movie_title}" data-content = "{storyline}">
            Story Line 
        </a>
    </div>
</div>
'''

# A single music entry html template (a row in the music_table)

row = '''
    <tr>
        <td><div class="music-tile" data-trailer-youtube-id="{trailer_youtube_id}"
            data-toggle="modal" data-target="#trailer" href="#"><u>{music_title}</u></div></td>
        <td>{author}</td>
        <td>{performer}</td>
        <td>{duration}</td>
    </tr>
'''

music_table = '''
<div class="container">
  <table class="table">
    <thead>
      <tr>
        <th>Title</th>
        <th>Author</th>
        <th>Performer</th>
        <th>Duration</th>
      </tr>
    </thead>
    <tbody>
        {rows}
    </tbody>
  </table>
</div>
'''

# The accordion UI for different sorting ways for the music table 

different_sorting_ways = '''
<div class="bs-example">
    <div class="panel-group" id="accordion{tab_number}">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion{tab_number}" href="#collapseOne{tab_number}"><em>Sort by title</em></a>
                </h4>
            </div>
            <div id="collapseOne{tab_number}" class="panel-collapse collapse in">
                <div class="panel-body">
                    <p>
                        {title_sort}
                    </p>
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion{tab_number}" href="#collapseTwo{tab_number}"><em>Sort by author</em></a>
                </h4>
            </div>
            <div id="collapseTwo{tab_number}" class="panel-collapse collapse">
                <div class="panel-body">
                    <p>
                        {author_sort}
                    </p>
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion{tab_number}" href="#collapseThree{tab_number}"><em>Sort by performer</em></a>
                </h4>
            </div>
            <div id="collapseThree{tab_number}" class="panel-collapse collapse">
                <div class="panel-body">
                    <p>
                        {performer_sort}
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

'''
# Three functions help sort by music title, author, performer:

def getKeyTitle(music):
        return music.title

def getKeyAuthor(music):
        return music.author

def getKeyPerformer(music):
        return music.performer

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
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            storyline = movie.storyline,
            actor = movie.actor,
            director = movie.director,
            data_release = movie.data_release,
            duration = movie.duration
        )
    return content

def create_music_content(m_list):
    # The HTML content for this section of the page
    music_rows = ''
    for music in m_list:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', music.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', music.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the row for the music with its content filled in
        music_rows += row.format(    
            music_title = music.title,
            trailer_youtube_id = trailer_youtube_id,
            performer = music.performer,
            author = music.author,
            duration = music.duration
        )
    content = music_table.format(rows = music_rows)
   
    return content

def select_music(musics, category):
    # select music by category
    m_list = []
    for music in musics:
        if music.category == category:
            m_list.append(music)
    return m_list


def music_tab(musics, category, tab_number):
    # There are 3 way of sorting the music list on a music tab: by title, by author, and by performer.
    music_list = select_music(musics, category)
    
    title_sorted_musics = sorted(music_list, key = getKeyTitle)
    title_sort_table = create_music_content(title_sorted_musics)

    author_sorted_musics = sorted(music_list, key = getKeyAuthor)
    author_sort_table = create_music_content(author_sorted_musics)

    performer_sorted_musics = sorted(music_list, key = getKeyPerformer)
    performer_sort_table = create_music_content(performer_sorted_musics)

    return different_sorting_ways.format(title_sort = title_sort_table,
                            author_sort = author_sort_table,
                            performer_sort = performer_sort_table,
                            tab_number = tab_number)


def open_movies_page(movies, musics):

    # Replace the placeholder for the movie and music tiles with the actual dynamically generated content.

    movie_tiles = create_movie_tiles_content(movies)
    
    classical_music_tiles =  music_tab(musics, "classical", "1")
    classical_crossover_music_tiles = music_tab(musics, "classical crossover", "2")
    pop_music_tiles = music_tab(musics, "pop", "3")
    
    # Fill 4 tabs for the mainpage.
    entertain = entertain_tabs.format(movie_content = movie_tiles,
                            classical_music_content = classical_music_tiles,
                            classical_crossover_music_content = classical_crossover_music_tiles,
                            pop_music_content = pop_music_tiles)


    rendered_content = main_page_content.format(tab = entertain)

    # Create or overwrite the output file

    output_file = open('index.html', 'w')

    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=1) # open in a new tab, if possible

    return
