import numpy as np
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Andmete sisselugemine
songs_df = pd.read_csv('all_songs.csv', sep=";", encoding = "ISO-8859-1")
playlist_df = pd.read_csv('playlists_dataset.csv', sep=";", encoding = "ISO-8859-1")

# Andmete eeltöötlus
playlist_df = playlist_df.dropna(how='any')
songs_df = songs_df.dropna(how='any')

base_songs = songs_df.iloc[:, 0:17].values
playlist_songs = playlist_df.iloc[:, 0:17].values
X = playlist_songs[:, [4, 5, 7, 8, 10, 11, 13, 14, 15, 16]]
Y = base_songs[:, [4, 5, 7, 8, 10, 11, 13, 14, 15, 16]]

# Laulude ja artistide nimed eraldi massiivi
song_names = np.column_stack((base_songs[:, 3], base_songs[:, 1]))
playlist_song_names = np.column_stack((playlist_songs[:, 3], playlist_songs[:, 1]))

# Andmete skaleerimine
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X)
y_train = sc_y.fit_transform(Y)

# KNN algoritmi rakendamine
neigh = NearestNeighbors(n_neighbors = 30)
neigh.fit(y_train)
result = neigh.kneighbors(X_train, return_distance = False)

# Valime suvalise laulu esitusloendist
random_index = random.randrange(len(result))
songs = result[random_index].tolist()

# Kuvame 30 soovitust suvaliselt valitud laulu alusel
print("Recommending songs similar to ", end = ' ')
print(playlist_song_names[random_index])

# Väljastame soovitused artisti ja laulu nime kaudu
for name, count in zip(song_names, enumerate(song_names)):
    for song in songs:
        if song == count[0]:
            print(name)