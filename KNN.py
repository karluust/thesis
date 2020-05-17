import numpy as np
import pandas as pd
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

# Andmete skaleerimine
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X)
y_train = sc_y.fit_transform(Y)

# KNN algoritmi rakendamine
neigh = NearestNeighbors()
neigh.fit(y_train)
result = neigh.kneighbors(X_train, 1, return_distance=True)

# result enniku lahutamine kahte eraldi listi, üks kauguse ja teine indeksite jaoks 
return_distance = result[0]
song_indexes = result[1]

# Sorteerime leitud laulud kauguste järgi
song_array = np.column_stack((song_indexes, return_distance))
sorted_array = song_array[song_array[:,1].argsort()]

# Uus list, kuhu valime laulud, mis on kõige väiksemate kaugustega (10% kõigist)
songs = []
for i in range(int(len(sorted_array)*0.1)):
    songs.append(int(sorted_array[i][0]))

# Duplikaatide eemaldamine
songs = list(set(songs)) 
 
# Väljastame soovitused artisti ja laulu nime kaudu
for item, count in zip(song_names, enumerate(song_names)):
    for song in songs:
        if song == count[0]:
            print(item)