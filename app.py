import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

def prompt_add_movies():
    title = input("movie title : ")
    release_date = input("Realease date (dd-mm-yy): ")
    parsed_date = datetime.datetime.strptime(release_date,"%d-%m-%y")
    timestramp = parsed_date.timestamp()

    database.add_movies(title , timestramp)

def print_movie_list(heading ,movies):
    print(f"--{heading } movies--")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie["release_timestramp"])
        human_date = movie_date.strftime("%b %d %y")
        print(f"{movie['title']} released on {human_date}")
    print("----\n")

def prompt_watch_movie():
    movie_title = input("Enter the movie you've watched")
    database.watch_movies(movie_title)

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movies()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("upcomming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("all",movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movie_list("watched" ,movies)
    else:
        print("Invalid input, please try again!")