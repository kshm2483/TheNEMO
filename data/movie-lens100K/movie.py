import csv
import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def genre_make():
    with open('u.genre', 'r', encoding="UTF-8") as p:
        res = []
        for line in p.readlines():
            value = line.split('|')[0]
            res += [value]
    return res

def poster_url():
    with open('movie_poster.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, quotechar=',')
        res = {}
        for row in reader:
            res[row[0]] = row[1]
    return res

def movie_make(genre_name, poster):
    request_data = {'movies': []}
    with open('u.item', 'r', encoding = "ISO-8859-1") as p:
        for line in p.readlines():
            movie = line.split('|')[:-1]
            movie = {
                'id' : int(movie[0]),
                'title' : movie[1],
                'date' : movie[2],
                'genres' : [genre_name[i] for i in range(len(movie[5:])) if int(movie[5+i])],
                'poster_url' : poster.get(movie[0])
            }
            request_data['movies'].append(movie)
    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)

def create_user():
    request_data = {'profiles': []}
    with open('u.user', 'r', encoding="UTF-8") as p:
        for line in p.readlines():
            userid, age, gender, occupation, zip_code = line.split('|')
            username = 'user' + userid
            age = int(age)
            request_data['profiles'].append({
                'username': username,
                'password': username,
                'age': age,
                'gender': gender,
                'occupation': occupation,
                'zip_code' : zip_code,
                'group' : 1
            })


    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    # print(response.text)

def rating_create():
    request_data = {'ratings': []}
    with open('u.data', 'r', encoding="UTF-8") as p:
        for line in p.readlines():
            [UserID, MovieID, Rating, Timestamp] = line.split('\t')
            request_data['ratings'].append({
                'userid': int(UserID),
                'movieid': int(MovieID),
                'rating': int(Rating),
                'timestamp': Timestamp[:-1]
            })

    response = requests.post(API_URL + 'rating_many/', data=json.dumps(request_data), headers=headers)
    # print(response.text)

def setupCluster():
    requests.post(API_URL + 'cluster/', headers=headers)

if __name__ == '__main__':
    movie_make(genre_make(), poster_url())
    create_user()
    rating_create()
    setupCluster()