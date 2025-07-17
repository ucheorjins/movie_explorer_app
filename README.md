# Top 300 Movie of All Time (Maybe) Explorer App

Search, filter, and compare 300 of the best movies of all time — by year, rating, genre, and runtime. Built with Python, BeautifulSoup Pandas, IMDbPY(Ass API btw), OMDB (could haave just used this from the beginning) and Streamlit.

This is basically a project to go through what i've learnt, starting surface python and i think i kinda went ahead of myself here (LOL). It features basic python functionalities (except classes) and webscraping. All of the scrapping and suffer are in a notebook file.

## Features

- Search movies by title, year range, genre, rating, and runtime
- Compare IMDb and Rotten Tomatoes scores
- Export results to CSV

## Tech Stack

- Python
- Pandas
- BeautifulSoup
- IMDbPY
- Time
- OMDB
- Streamlit

## 🛠 Getting Started (Run Locally)

To run this project on your machine:

1.  Clone/download the Repository
2.  Create virtual environment (optional)
    python3 -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate

    or just load it on you code editor

3.  Install dependencies

    pip install pandas streamlit imdbpy

4.  Run the app
    streamlit run app.py

5.  You can now use the app in your browser at http://localhost:8501. Have fun, i guess.

NB: You really only need the app.py and the final_movie_info.csv files. The scraper.ipynb file is basically what is it; the file where i scrapped the info i used and read it into a csv file. The other CSV files are earlier movie info files.

## 👨🏾‍💻 Author

Built by Uche Ekpendu (ucheorjins)
