import csv, requests, json, os

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def movie_detail():
    def movie_imdbid():
        with open('movie_url.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, quotechar=',')
            res = {}
            for row in reader:
                # if row[0] != '1516':
                if row[0] != '1516' and int(row[0]) >= 25:
                    res[int(row[0])] = row[1].split('/')[4]
        return res

    apiKey = os.getenv('TMDBapiKey')


    for id, imdbId in movie_imdbid().items():
        url = f'https://api.themoviedb.org/3/find/{imdbId}?api_key={apiKey}&external_source=imdb_id'
        print(url)
        res = requests.get(url)
        movie = res.json()["movie_results"]
        if movie:
            movie = movie[0]
        else:
            continue

        request_data = {
            'id':id,
            'backdrop_path' : movie['backdrop_path'],
            'adult' : False if movie['adult'] == "False" else True,
            'overview' : movie['overview']
            }
        print(id)
        requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)

if __name__ == '__main__':
    movie_detail()