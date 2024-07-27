# Movie Recommendation Web App

## Author: Anand Dubey

## Description
This project is a self-initiated data science endeavor that leverages collaborative filtering to recommend movies. The recommendation engine uses Netflix movie and rating data. Given that the ratings file contains over 10 million rows, performing data analysis was challenging. To enhance performance, the data format was converted from CSV to Parquet.

## Key Features
- **Collaborative Filtering**: Utilizes collaborative filtering to provide personalized movie recommendations based on user ratings.
- **Data Format Conversion**: To manage and analyze large datasets efficiently, the ratings file was converted from CSV to Parquet.
- **TF-IDF Vectorization**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization for movie title matching and similarity calculations.
- **Debounced Search**: Implements a debounced search mechanism to optimize search performance and provide relevant results with minimal delay.
- **Widget Integration**: Incorporates interactive widgets for dynamic user input and real-time recommendations.

## Project Components
1. **Data Loading and Preparation**:
   - **Movies Dataset**: Contains movie details including titles and metadata.
   - **Ratings Dataset**: Contains user ratings for various movies.
   - **Data Cleaning**: Processes movie titles to remove special characters and standardizes text for improved matching.

2. **Similarity Calculation**:
   - **TF-IDF Vectorization**: Converts movie titles into numerical vectors.
   - **Cosine Similarity**: Measures the similarity between the search query and movie titles to find the most relevant matches.

3. **User Interaction**:
   - **Search Functionality**: Allows users to input a movie title and receive a list of similar movies.
   - **Debouncing**: Reduces the frequency of search function calls to improve performance.

4. **Recommendation Generation**:
   - **Collaborative Filtering**: Recommends movies by identifying users with similar tastes and suggesting movies they have rated highly.
   - **Recommendation Scoring**: Calculates recommendation scores based on the overlap between similar users' preferences and the overall user base.

## How It Works
- **Data Ingestion**: Load the movie and rating datasets.
- **Data Transformation**: Clean and preprocess the data for analysis.
- **Vectorization**: Apply TF-IDF vectorization to movie titles.
- **Search Mechanism**: Implement a search function that leverages cosine similarity to find matching movie titles.
- **Recommendation System**: Use collaborative filtering to identify and recommend movies that similar users have enjoyed.

## Benefits
- **Enhanced Performance**: Converting the data format to Parquet significantly improves data processing speed and efficiency.
- **Personalized Recommendations**: By using collaborative filtering, the system provides personalized movie suggestions tailored to individual user preferences.
- **Real-Time Interaction**: The integration of interactive widgets allows for real-time user input and immediate recommendation feedback.

## Future Improvements
- **Expanded Dataset**: Incorporate additional data sources to enrich the recommendation engine.
- **Advanced Filtering**: Implement more sophisticated filtering techniques to further refine recommendations.
- **User Interface**: Develop a more user-friendly interface for better user experience.

This project showcases the application of data science techniques to build a robust and efficient movie recommendation system, demonstrating practical skills in data manipulation, machine learning, and user interaction.
