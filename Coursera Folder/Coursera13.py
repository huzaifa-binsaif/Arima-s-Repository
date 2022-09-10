# Caching responce Content:

import requests_with_caching
# its not found in permanent cache
res = requests_with_caching.get('https://api.datamuse.com/words?rel_rhy = happy', permanent_cache_file = 'datamuse_cache_txt')
print(res.txt[:100])
# This time it will be found in the temporary cache
res = requests_with_caching.get('https://api.datamuse.com/words?rel_rhy = happy', permanent_cache_file = 'datamuse_cache_txt')
# This one is in the permanent cache
res = requests_with_caching.get('https://api.datamuse.com/words?rel_rhy = funny', permanent_cache_file = 'datamuse_cache_txt')


# 1
import requests_with_caching
def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params_dict = {}
    params_dict['q'] = movie
    params_dict['type'] = 'movies'
    params_dict['limit'] = '5'
    resp = requests_with_caching.get(baseurl,params = params_dict)
    movies_ds = resp.json()
    return movies_ds
movie = get_movies_from_tastedive('Bridesmaids')
movie = get_movies_from_tastedive('Black Panther')


# 2
def extract_movie_titles(movie):
    extracted_movies = []
    for lvl1 in movie['Similar']['Results']:
        extracted_movies.append(lvl1['Name'])
    print(extracted_movies)
    return extracted_movies
ex_movies = extract_movie_titles(movie)


# 3
def get_related_titles(list):
    extracted_movies = []
    if len(list) == 0:
        return extracted_movies
    else:
        for movie in list:
            baseurl = "https://tastedive.com/api/similar"
            params_dict = {}
            params_dict['q'] = movie
            print(params_dict['q'])
            params_dict['type'] = 'movies'
            params_dict['limit'] = '5'
            resp = requests_with_caching.get(baseurl,params = params_dict)
            movies_ds = resp.json()
            for lvl1 in movies_ds['Similar']['Results']:
                if lvl1['Name'] in extracted_movies:
                    pass
                else:
                    extracted_movies.append(lvl1['Name'])
        print(extracted_movies)
        return extracted_movies
list_movies = get_related_titles([])


# 4
import requests_with_caching
def get_movie_data(movie):
    baseurl = 'http://www.omdbapi.com/'
    params_dict = {}
    params_dict['t'] = movie
    params_dict['r'] = 'json'
    resp = requests_with_caching.get(baseurl,params = params_dict)
    movies_ds = resp.json()
    print(resp)
    return movies_ds
movie_data = get_movie_data("Venom")


# 5
def get_movie_rating(dict):
    for item in dict["Ratings"]["Source"]:
        if 'rotten tomatos' in item['Source']:
            return int(item['Value'][:2])
    return int(0)
