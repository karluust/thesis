# Spotify Recommendation System
Repository for Bachelor Thesis **"Implementation Of A Music Recommendation System Using k-nearest neighbors Algorithm"**.
Get song recommendations based on a Spotify playlist of your choice.
Made with Python 3 using Spotipy, Pandas, NumPy and Scikit-learn libraries.

## Setup
1. Clone the repository
2. Make sure you have a Spotify account and Spotipy, Pandas, NumPy, Scikit-learn libraries installed.
3. Download this [Database](https://components.one/datasets/billboard-200/) from where the recommendations will be made. Extract the table "acoustic_features" into a .csv file using any SQLite GUI
3. Get your Spotify client data following [this tutorial](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app).
4. Set your Redirect URI in the Spotify App settings to http://localhost/
5. Set up the client data as environmental variables using a CLI (This is how to do it in Windows):
```
export SPOTIPY_CLIENT_ID = 'your client ID here'
export SPOTIPY_CLIENT_SECRET = 'your client secret here'
export SPOTIPY_REDIRECT_URI = 'http://localhost/'
```

## Usage
1. Run ```get_data.py``` from the CLI: ```py get_data.py 'your username here' 'your playlist id here' > playlists_dataset.csv``` to get your Spotify playlist data into a .csv file
2. Make sure the dataset names in ```KNN.py```, ```KNNAlt1.py```, ```KNNAlt2.py``` match your actual dataset names and that the datasets are in the same folder as the .py files.
3. Run the different versions ```KNN.py```, ```KNNAlt1.py```, ```KNNAlt2.py``` of the recommendation system and observe the results.
