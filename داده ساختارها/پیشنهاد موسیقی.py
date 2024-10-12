import itertools

all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = dict(
        age=age,
        city=city,
        albums=albums,
    )


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = dict(
        artist_name=artist_name,
        genre=genre,
        tracks=tracks,
    )


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    user_albums = all_users[username]['albums']
    songs = 0
    for album in user_albums:
        if all_albums[album]['artist_name'] == artist_name:
            songs += all_albums[album]['tracks']
    print(songs)


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    user_albums = all_users[username]['albums']
    songs = 0
    for album in user_albums:
        if all_albums[album]['genre'] == genre:
            songs += all_albums[album]['tracks']
    print(songs)


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    artist_albums = {}
    for key, value in all_albums.items():
        if value['artist_name'] == artist_name:
            artist_albums[key] = value

    albums_of_same_age = []
    for name, features in all_users.items():
        if features['age'] == age:
            albums_of_same_age.append(features['albums'])
    albums_of_same_age = list(itertools.chain(*albums_of_same_age))

    songs = 0
    for album in albums_of_same_age:
        if album in artist_albums:
            songs += artist_albums[album]['tracks']
    print(songs)


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    artist_albums = {}
    for key, value in all_albums.items():
        if value['genre'] == genre:
            artist_albums[key] = value

    albums_of_same_age = []
    for name, features in all_users.items():
        if features['age'] == age:
            albums_of_same_age.append(features['albums'])
    albums_of_same_age = list(itertools.chain(*albums_of_same_age))

    songs = 0
    for album in albums_of_same_age:
        if album in artist_albums:
            songs += artist_albums[album]['tracks']
    print(songs)


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    artist_albums = {}
    for key, value in all_albums.items():
        if value['artist_name'] == artist_name:
            artist_albums[key] = value

    albums_of_same_city = []
    for name, features in all_users.items():
        if features['city'] == city:
            albums_of_same_city.append(features['albums'])
    albums_of_same_city = list(itertools.chain(*albums_of_same_city))

    songs = 0
    for album in albums_of_same_city:
        if album in artist_albums:
            songs += artist_albums[album]['tracks']
    print(songs)


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    artist_albums = {}
    for key, value in all_albums.items():
        if value['genre'] == genre:
            artist_albums[key] = value

    albums_of_same_city = []
    for name, features in all_users.items():
        if features['city'] == city:
            albums_of_same_city.append(features['albums'])
    albums_of_same_city = list(itertools.chain(*albums_of_same_city))

    songs = 0
    for album in albums_of_same_city:
        if album in artist_albums:
            songs += artist_albums[album]['tracks']
    print(songs)


# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD


if __name__ == '__main__':
    all_users = {}
    all_albums = {}

    add_user("SAliB", 19, "Tehran", [
             "tekunbede", "barf", "gavazn"], all_users, all_albums)
    add_user("Saeid", 22, "Esfehan", [
             "eclipse", "barf", "gavazn"], all_users, all_albums)
    add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)

    add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
    add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
    add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
    add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
    add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
    add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)

    # query_user_artist("Ali", "ghorbani", all_users, all_albums)
    # query_user_genre("Ali", "classic", all_users, all_albums)
    # query_age_artist(12, "shajarian", all_users, all_albums)
    # query_age_artist(22, "malmsteen", all_users, all_albums)
    # query_age_genre(12, "pop", all_users, all_albums)
    # query_age_genre(19, "pop", all_users, all_albums)

    # query_city_artist("Bushehr", "ghorbani", all_users, all_albums)
    query_city_genre("Bushehr", "pop", all_users, all_albums)
