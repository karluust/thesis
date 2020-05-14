import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Andmete sisselugemine
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
result = neigh.kneighbors(X_train, return_distance=True)

# result enniku lahutamine kahte eraldi listi, üks kauguse ja teine indeksite jaoks 
return_distance = result[0]
song_indexes = result[1]

# Leiame laulu indeksi millel on kõige väiksemate kaugustega naabrid
distance_sum = np.sum(return_distance, axis=1).tolist()
smallest_distance_index = distance_sum.index(min(distance_sum))
songs = song_indexes[smallest_distance_index].tolist()

# Väljastame 30 soovitust laulule, millel on kõige sarnasemad naabrid
print("Recommending songs similar to ", end = ' ')
print(playlist_song_names[smallest_distance_index])

for name, count in zip(song_names, enumerate(song_names)):
    for song in songs:
        if song == count[0]:
            print(name)
