import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies = pd.read_csv('./movies.csv')
ratings = pd.read_csv('./ratings.csv')

movies.info()
ratings.info()
movies.shape
ratings.shape
movies.describe()
ratings.describe()

genres = []
for genre in movies.genres:
    x = genre.split('|')
    for i in x:
    if i not in genres:
    genres.append(str(i))
genres = str(genres)
movie_title = []
for title in movies.title:
    movie_title.append(title[0:-7])
movie_title = str(movie_title)
df = pd.merge(ratings, movies, how='left', on='movieId')
df.head()
df1 = df.groupby(['title'])[['rating']].sum()
high_rated = df1.nlargest(20, 'rating')
high_rated.head()
plt.figure(figsize=(30, 10))

plt.title('Top 20 movies with highest rating', fontsize=40)
plt.ylabel('ratings', fontsize=30)
plt.xticks(fontsize=20, rotation=90)
plt.xlabel('movies title', fontsize=30)
plt.yticks(fontsize=25)
plt.bar(high_rated.index, high_rated['rating'], linewidth=3)

cv = TfidfVectorizer()
tfidf_matrix = cv.fit_transform(movies['genres'])
movie_user = df.pivot_table(index='userId', columns='title', values='rating')
movie_user.head()
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

#recommendations ('Toy Story (1995)')
list_inputs = []
input1 = input('Enter movie name with year of release: ')
for i in movies['title']:
    if input1 in i:
    list_inputs.append(i)
for i in range(len(list_inputs)):
    print('{} - {}'.format(i+1, list_inputs[i]))
input3 = int(input("Enter the number of movie you have watched: "))-1
input1 = list_inputs[input3]
input2 = int(input('Enter no. of recommendations needed: ')) + 1
print(recommendations(input1, input2).to_string(index=False))
sim_scores = recommendations2(input1, input2)
sim_list = []
for i in range(len(sim_scores)):
    tup_index = sim_scores[i][1]*100
    sim_list.append(tup_index)
sim_list
movie_recs_list = []
for i in range(len(sim_scores)):
    tup_index = sim_scores[i][0]
    movie_recs_list.append(movies.iloc[tup_index].title)
movie_recs_list
plt.figure(figsize=(30, 10))
plt.title('Our Top Recommendations based on your choice', fontsize=40)
plt.ylabel('Similarity(%) ', fontsize=30)
plt.xticks(fontsize=20, rotation=90)
plt.xlabel('Movies Title', fontsize=30)
plt.yticks(fontsize=25)
plt.ylim([90, 100])
plt.bar(movie_recs_list, sim_list)
