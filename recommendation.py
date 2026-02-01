import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'Movie': ['Inception', 'Interstellar', 'Titanic', 'The Notebook', 'Avengers', 'Iron Man'],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Romance', 'Romance', 'Action', 'Action']
}

df = pd.DataFrame(data)
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['Genre'])
similarity = cosine_similarity(genre_matrix)
def recommend(movie_name):
    index = df[df['Movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended movies:")
    for i in scores[1:3]:
        print(df['Movie'][i[0]])
recommend('Inception')
