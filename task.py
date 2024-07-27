import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ipywidgets as widgets
from IPython.display import display, clear_output

# Load datasets
ratings = pd.read_csv("Netflix_Dataset_Rating.csv")
movies = pd.read_csv("Netflix_Dataset_Movie.csv")

# Create Term Frequency matrix using TF-IDF with original titles
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
tfidf = vectorizer.fit_transform(movies["Name"])

def search(Name):
    query_vec = vectorizer.transform([Name])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argsort(similarity)[::-1][:5]  # Sort in descending order
    results = movies.iloc[indices]
    if results.empty:
        return pd.DataFrame(columns=["Movie_ID", "Year", "Name"])
    return results

# Create and display widgets
movie_input = widgets.Text(
    value="Character",
    description="Movie Title: ",
    disabled=False
)
movie_list = widgets.Output()

def on_type(data):
    with movie_list:
        clear_output()
        title = data["new"]
        if len(title) > 5:
            results = search(title)
            display(results)

movie_input.observe(on_type, names='value')
display(movie_input, movie_list)

def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["Movie_ID"] == movie_id) & (ratings["Rating"] >= 4)]["User_ID"].unique()
    similar_users_recs = ratings[(ratings["User_ID"].isin(similar_users)) & (ratings["Rating"] >= 4)]["Movie_ID"]
    similar_users_recs = similar_users_recs.value_counts() / len(similar_users)
    similar_users_recs = similar_users_recs[similar_users_recs > 0.1]
    all_users = ratings[(ratings["Movie_ID"].isin(similar_users_recs.index)) & (ratings["Rating"] >=4)]
    all_users_recs = all_users["Movie_ID"].value_counts() / len(all_users["User_ID"].unique())
    rec_percentages = pd.concat([similar_users_recs, all_users_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_on="Movie_ID", right_on="Movie_ID")[["Movie_ID", "Year", "Name"]]

movie_name_input = widgets.Text(
    value="",
    description="Movie Title",
    disabled=False
)
recommendation_list = widgets.Output()

def on_type_recommendation(data):
    with recommendation_list:
        clear_output()
        Name = data["new"]
        if len(Name) > 5:
            results = search(Name)
            if not results.empty:
                movie_id = results.iloc[0]["Movie_ID"]
                display(find_similar_movies(movie_id))

movie_name_input.observe(on_type_recommendation, names="value")
display(movie_name_input, recommendation_list)

# Example standalone test
movie = input("Enter the movie name: ")
print(search(movie))