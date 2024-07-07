# Import necessary libraries
import pandas as pd
import numpy as np

# Upload your ratings.csv file to Google Colab
from google.colab import files
uploaded = files.upload()

# Load data into Pandas DataFrame
file_path = "ratings.csv"  # Make sure to use the correct file path after uploading
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to verify data loading
df.head()
# Function to create user-item matrix
def create_user_item_matrix(df):
    user_item_matrix = df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    return user_item_matrix

# Function to compute similarity between users based on ratings
def compute_user_similarity(user_item_matrix):
    user_similarity = np.dot(user_item_matrix, user_item_matrix.T)
    norms = np.array([np.sqrt(np.diagonal(user_similarity))])
    user_similarity = user_similarity / (norms * norms.T)
    return user_similarity

# Function to recommend movies for a given user
def get_top_n_recommendations(user_item_matrix, user_similarity, user_id, n=5):
    # Get movies not rated by user
    user_ratings = user_item_matrix.loc[user_id]
    unrated_movies = user_ratings[user_ratings == 0].index
    
    # Predict ratings for unrated movies based on similar users
    predicted_ratings = np.dot(user_similarity[user_id-1], user_item_matrix.values)
    
    # Sort predictions and get top n recommendations
    top_n_indices = np.argsort(predicted_ratings)[::-1][:n]
    top_n_movies = user_item_matrix.columns[top_n_indices]
    top_n_ratings = predicted_ratings[top_n_indices]
    
    recommendations = [(movie_id, rating) for movie_id, rating in zip(top_n_movies, top_n_ratings)]
    return recommendations

# Function to get top rated movies in general
def get_top_rated_movies(df, n=10):
    top_rated_movies = df.groupby('movie_id')['rating'].mean().sort_values(ascending=False).head(n)
    return top_rated_movies.index.tolist()

# Function to get movies similar to a given movie
def get_similar_movies(user_item_matrix, movie_id, n=5):
    movie_similarity = np.corrcoef(user_item_matrix.T)
    movie_idx = movie_id - 1
    similar_movies_idx = np.argsort(movie_similarity[movie_idx])[::-1][1:n+1]
    similar_movies = [idx + 1 for idx in similar_movies_idx]
    return similar_movies

# Function to recommend movies based on a user's top rated genres
def get_genre_based_recommendations(df, user_id, user_item_matrix, top_n=5):
    # Find movies rated highly by the user
    user_ratings = df[df['user_id'] == user_id]
    top_rated_movies = user_ratings.groupby('movie_id')['rating'].mean().sort_values(ascending=False).head(top_n)
    
    # Filter out movies the user has already rated
    user_item_matrix = user_item_matrix.loc[user_id]
    unrated_movies = top_rated_movies[~top_rated_movies.index.isin(user_item_matrix[user_item_matrix > 0].index)]
    
    return unrated_movies.index.tolist()[:5]

# Create user-item matrix
user_item_matrix = create_user_item_matrix(df)

# Compute user-user similarity
user_similarity = compute_user_similarity(user_item_matrix.values)

# Example: Recommend top 5 movies for user 1
user_id = 1
recommendations = get_top_n_recommendations(user_item_matrix, user_similarity, user_id)

print(f"Top 5 Movie Recommendations for User {user_id}:")
for movie_id, estimated_rating in recommendations:
    print(f"Movie ID: {movie_id}, Estimated Rating: {estimated_rating}")

# Example: Get top rated movies in general
top_rated_movies = get_top_rated_movies(df)
print("\nTop Rated Movies in General:")
for movie_id in top_rated_movies:
    print(f"Movie ID: {movie_id}")

# Example: Get movies similar to a given movie
movie_id = 1
similar_movies = get_similar_movies(user_item_matrix, movie_id)
print(f"\nMovies Similar to Movie ID {movie_id}:")
for movie_id in similar_movies:
    print(f"Movie ID: {movie_id}")

# Example: Recommend movies based on user's top rated genres
user_id = 1
genre_based_recommendations = get_genre_based_recommendations(df, user_id, user_item_matrix)
print(f"\nGenre-Based Recommendations for User {user_id}:")
for movie_id in genre_based_recommendations:
    print(f"Movie ID: {movie_id}")
