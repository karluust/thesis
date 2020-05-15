# %% Teekide importimine
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# %% Andmete sisselugemine
songs_df = pd.read_csv('all_songs.csv', sep=";", encoding = "ISO-8859-1")
playlist_df = pd.read_csv('playlists_dataset.csv', sep=";", encoding = "ISO-8859-1")

# Andmete eeltöötlus
playlist_df = playlist_df.dropna(how='any')
#songs_df = songs_df.sample(100000)
songs_df = songs_df.dropna(how='any')

base_songs = songs_df.iloc[:, 0:17].values
playlist_songs = playlist_df.iloc[:, 0:17].values
X = playlist_songs[:, 7:17]
Y = base_songs[:, 7:17]

# Laulude ja artistide nimed eraldi massiivi
song_names = np.column_stack((base_songs[:, 3], base_songs[:, 1]))

# %% Andmete skaleerimine
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X)
y_train = sc_y.fit_transform(Y)

# %% KNN algoritmi rakendamine
neigh = NearestNeighbors(n_neighbors = len(X))
neigh.fit(X_train)
result = neigh.kneighbors(y_train, return_distance=True)

# result enniku lahutamine kahte eraldi 1D massiivi, üks kauguse ja teine indeksite jaoks 
return_distance = result[0]
song_indexes = result[1]

# %% Moodustame massiivi laulude indeksitest ja kauguste summadest
song_array = np.zeros((len(Y), 1))
counter = 0
for i in range(len(Y)):
    song_array[i][0] = counter
    counter += 1

distance_sum = np.sum(return_distance, axis=1)
distances_and_indexes = np.column_stack((distance_sum, song_array))
# %% Sorteerime massiivi ning lisame 30 esitusloendile kõige sarnasemat laulu uute massiivi
sorted_array = distances_and_indexes[distances_and_indexes[:,0].argsort()]

songs = []
for i in range(30):
    songs.append(int(sorted_array[i][1]))

# %% Väljastame 30 soovitust artisti ja laulu nime kaudu
for name, count in zip(song_names, enumerate(song_names)):
    for song in songs:
        if song == count[0]:
            print(name)