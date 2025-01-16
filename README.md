<h1>  TMDB Movie Recommender System 🎬  </h1>
A content-based movie recommendation system built using the TMDB Movies Dataset. This system analyzes movie features like plot overviews and genres to recommend similar movies based on content similarity.

📝 Description
This project implements a movie recommendation system using content-based filtering techniques. The system processes movie descriptions and genres using natural language processing to find similar movies based on their content. It uses cosine similarity to measure the relationships between movies and provide personalized recommendations.

🔑 Key Features
- Content-based movie recommendations
- Processes both movie overviews and genres
- Handles a dataset of 10,000 movies
- Supports multiple languages (43 different original languages)
- Uses advanced NLP techniques for text processing
- Provides top 5 similar movie recommendations

🛠️ Technologies Used
- Python 3.x
- Pandas
- Scikit-learn
- NLTK
- Pickle

💾 Dataset Information
The TMDB Movies dataset includes:
- 10,000 movies
- 2,123 unique genre combinations
- 43 different original languages
- Vote ratings from 4.6 to 8.7
- Movies released up to 2017-10-20

📊 Model Files
Due to file size limitations on GitHub, the model files are hosted on Google Drive (https://intip.in/moviemodel):
- movies.pkl (processed movie data)
- similarity.pkl (similarity matrix)

Download these files from the Google Drive link above and place them in your project directory before running the system.

📈 Performance
The system currently achieves:
- Average processing time: < 1 second per recommendation
- Dataset coverage: 99.87% (9,987 movies with complete information)
- Supports multiple genre combinations for better recommendations

📄 License
This project is licensed under the MIT License - see the LICENSE.md file for details

👥 Authors
Elia Samuel
Muhammad Fa'iz Ismail

🙏 Acknowledgments

TMDB for providing the movie dataset
Scikit-learn team for their machine learning tools
Anthropic for assistance in development
