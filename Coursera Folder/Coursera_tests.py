
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

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



# 2
def extract_movie_titles(movie):
    extracted_movies = []
    for lvl1 in movie['Similar']['Results']:
        extracted_movies.append(lvl1['Name'])
    print(extracted_movies)
    return extracted_movies


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
            params_dict['type'] = 'movies'
            params_dict['limit'] = '5'
            resp = requests_with_caching.get(baseurl,params = params_dict)
            movies_ds = resp.json()
            for lvl1 in movies_ds['Similar']['Results']:
                if lvl1['Name'] in extracted_movies:
                    pass
                else:
                    extracted_movies.append(lvl1['Name'])
        return extracted_movies


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


# 5
def get_movie_rating(dict):
    try:
        for item in dict["Ratings"]:
            if 'Rotten Tomatoes' in item['Source']:
                return int(item['Value'][:2])
        return int(0)
    except:
        return int(0)

# 6
def takeSecond(elem):
    return elem[1]

def get_sorted_recommendations(list_movies):
    related_list = get_related_titles(list_movies)
    rating_list = []
    for movie in related_list:
        movie_data = get_movie_data(movie)
        rating_list.append(get_movie_rating(movie_data))
    zipped = zip (related_list,rating_list)
    zipped.sort(key = takeSecond,reverse = True)
    sorted_list = []
    for x in zipped:
        sorted_list.append(x[0])
    return sorted_list
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
