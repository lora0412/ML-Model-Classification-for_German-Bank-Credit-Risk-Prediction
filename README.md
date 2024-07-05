# IRONHACK Data Analytics Week 7 Project Risky Business: ML’s Guide to German Credit Scores"

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Data Description](#data-description)
4. [Analysis and Methodology](#analysis-and-methodology)
5. [Results and Insights](#results-and-insights)
6. [Installation and Usage](#installation-and-usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact Information](#contact-information)

## Introduction
Welcome to the Music Recommendation System project! This project aims to develop a content-based music recommendation system using data from Spotify's Top 50 EDM Playlists from Germany, Netherlands, Portugal, Spain, US, and the UK. The system leverages Spotify's API to collect data and provides personalized music recommendations.

## Project Overview
- Collecting data from Spotify's API for the Top 50 EDM Playlists from the specified countries.
- Analyzing and processing the collected data.
- Developing a content-based recommendation algorithm using machine learning models.
- Evaluating the performance of the recommendation system.
- Providing insights and visualizations based on the analysis.

## Data Description
The data for this project is obtained from Spotify's API, focusing on the Top 50 EDM Playlists from Germany, Netherlands, Portugal, Spain, US, and the UK. The data includes:

- Track information (e.g.,track_id, track_name, artist_name, album_name, release_date, duration_ms, popularity)
- Audio features (e.g.,danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo)

## Analysis and Methodology
The analysis and methodology section covers the following:
- Data Collection: Using Spotify's API to gather playlist and track data.
- Data Cleaning and Preprocessing: Using Python to handling duplicates and missing values and normalizing data.
- Feature Engineering: Extracting relevant features for the recommendation system.
- Machine Learning Models: Utilizing K-means clustering and dimensionality reduction techniques like PCA and ISOMAP to enhance the recommendation system.
- Evaluation: Assessing the performance of the recommendation system using appropriate metrics - Silhouette Score.
- Content-Based Recommendation: Developing an algorithm that recommends tracks based on audio features similarity.

## Results and Insights
This section will present the findings from the analysis, including:
- Insights into the characteristics of the Top 50 EDM tracks in each country.
- Performance metrics of the recommendation system: Best performance clusters: 5 with Silhouette Score 0.26.
- Visualizations that highlight key trends and patterns in the data by radar chart.

## Installation and Usage
1. Python 3.8 or higher
  - Install required libraries: `pip install numpy, pandas, glob, requests, base64, time, logging, spotipy, statsmodels.api, matplotlib.pyplot, seaborn, sklearn`.
  - Run the analysis script: `Spotify_Machine Learning_6_features.ipynb`,  `Spotify_API_EU_US_TOP_50_EDM_playlists_tracks.ipynb`
2. Spotify Developer Account (to access Spotify API)

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
No license need for this project.

## Contact Information
For any questions, please contact:
- Name: Lora Chuaner Ding, Eileen Hesseling, João Sousa, Toan
- Email: chuanerding0412@gmail.com
