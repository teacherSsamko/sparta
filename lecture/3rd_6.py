from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta 

movies = list(db.movie.find())

for movie in movies:
    if movie['title'] == '매트릭스':
        matrix_star = movie['star']

same_movies = list(db.movie.find({'star':matrix_star}))

# for movie in same_movies:
    # print(movie['title'])
    # db.movie.update_one({'title':movie['title']},{'$set':{'star':0}})

def get_star(title):
    for movie in movies:
        if movie['title'] == title:
            return movie['star']

def same_star_movies(title):
    star = get_star(title)
    same_movies = list(db.movie.find({'star':star}))
    for movie in same_movies:
        print(movie['title'])
    return same_movies

same_star_movies('클래식')