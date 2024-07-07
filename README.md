# Movie Magic: Personalized Movie Recommendations

Welcome to Movie Magic, your personalized movie recommendation system! This project leverages collaborative filtering techniques to suggest movies based on user ratings. Whether you're a cinephile or just looking for something new to watch, Movie Magic has you covered.

## How It Works

Movie Magic analyzes user ratings from a dataset (`ratings.csv`) to generate recommendations. It creates a user-item matrix, computes user similarity, and uses these insights to suggest movies tailored to your taste.

## Features

- **User-Item Matrix**: Converts ratings data into a matrix where rows represent users and columns represent movies, capturing user preferences.
- **User Similarity**: Calculates how similar users are based on their movie ratings, helping find users with similar tastes.
- **Top-N Recommendations**: Suggests top movies for a user by predicting ratings for unrated movies.
- **Top Rated Movies**: Highlights the highest-rated movies across all users to discover crowd favorites.
- **Similar Movies**: Identifies movies similar to a chosen film, perfect for finding movies with comparable themes or styles.
- **Genre-Based Recommendations**: Recommends movies based on genres you enjoy the most, making it easier to discover new favorites.

## Getting Started

1. **Upload Your Data**: Use Google Colab to upload `ratings.csv` with movie ratings data.
   
2. **Explore Your Data**: Load and examine your dataset to ensure it's ready for analysis.
   
3. **Run the Functions**: Execute functions to create the user-item matrix, compute user similarity, and generate recommendations.

## Example Usage

- **Top 5 Recommendations for User 1**:
  ```python
  user_id = 1
  recommendations = get_top_n_recommendations(user_item_matrix, user_similarity, user_id)
  ```

- **Top Rated Movies Overall**:
  ```python
  top_rated_movies = get_top_rated_movies(df)
  ```

- **Movies Similar to 'Titanic'**:
  ```python
  movie_id = 1  # Replace with the movie ID of 'Titanic'
  similar_movies = get_similar_movies(user_item_matrix, movie_id)
  ```

- **Genre-Based Recommendations for User 1**:
  ```python
  user_id = 1
  genre_based_recommendations = get_genre_based_recommendations(df, user_id, user_item_matrix)
  ```

## Dependencies

Ensure you have the following libraries installed:
- `pandas`
- `numpy`

## Notes

- Experiment with different parameters (`n` for top-N recommendations, `top_n` for genre-based recommendations) to personalize results.
- Enhance user experience by integrating with web interfaces or APIs for broader accessibility.
- Movie Magic thrives on data quality; ensure your dataset is comprehensive and reflects user preferences accurately.

## Let's Get Started!

Discover your next movie gem with Movie Magic. Sit back, relax, and let the magic of movies unfold!
