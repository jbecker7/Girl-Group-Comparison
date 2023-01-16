import re
import matplotlib.pyplot as plt
import lyricsgenius as genius
import matplotlib.font_manager as fm
from korean_romanizer.romanizer import Romanizer



# initialize Genius API object
genius_api = genius.Genius("key")

# search for GFriend songs
gfriend_songs = genius_api.search_artist("GFriend", max_songs=10)
twice_songs = genius_api.search_artist("Twice", max_songs=10)
blackpink_songs = genius_api.search_artist("BlackPink", max_songs=10)

# get the lyrics of all the songs
gfriend_lyrics = ""
twice_lyrics = ""
blackpink_lyrics = ""

for song in gfriend_songs.songs:
    gfriend_lyrics +=song.lyrics + " "
for song in twice_songs.songs:
    twice_lyrics +=song.lyrics + " "
for song in blackpink_songs.songs:
    blackpink_lyrics +=song.lyrics + " "

# split lyrics into words
gfriend_words = gfriend_lyrics.split()
twice_words = twice_lyrics.split()
blackpink_words = blackpink_lyrics.split()

# list of words to exclude, just 가사 which means lyrics (and kept coming up)
exclude_words = ["가사]"]

# function to check if a word is Korean
def is_korean(word):
    korean_pattern = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
    return bool(korean_pattern.match(word))

# count the frequency of each word for GFriend
gfriend_word_freq = {}
for word in gfriend_words:
    # check if word is in exclude list
    if word not in exclude_words and is_korean(word) and word.isalpha():
        gfriend_word_freq[word] = gfriend_word_freq.get(word, 0) + 1

# count the frequency of each word for Twice
twice_word_freq = {}
for word in twice_words:
    # check if word is in exclude list
    if word not in exclude_words and is_korean(word) and word.isalpha():
        twice_word_freq[word] = twice_word_freq.get(word, 0) + 1

# count the frequency of each word for BlackPink
blackpink_word_freq = {}
for word in blackpink_words:
    # check if word is in exclude list
    if word not in exclude_words and is_korean(word) and word.isalpha():
        blackpink_word_freq[word] = blackpink_word_freq.get(word, 0) + 1

# find the 30 most common words for GFriend
gfriend_most_common = sorted(gfriend_word_freq.items(), key=lambda x: x[1], reverse=True)[:30]

# find the 30 most common words for Twice
twice_most_common = sorted(twice_word_freq.items(), key=lambda x: x[1], reverse=True)[:30]

# find the 30 most common words for BlackPink
blackpink_most_common = sorted(blackpink_word_freq.items(), key=lambda x: x[1], reverse=True)[:30]

# extract the words and frequency counts for GFriend
gfriend_words = [word for word, freq in gfriend_most_common]
gfriend_freqs = [freq for word, freq in gfriend_most_common]

# extract the words and frequency counts for Twice
twice_words = [word for word, freq in twice_most_common]
twice_freqs = [freq for word, freq in twice_most_common]

# extract the words and frequency counts for BlackPink
blackpink_words = [word for word, freq in blackpink_most_common]
blackpink_freqs = [freq for word, freq in blackpink_most_common]

# I am so done with configuring fonts that I am just gonna romanize 

gfriend_words_romanized = []
for word in gfriend_words:
    romanizer = Romanizer(word)
    gfriend_words_romanized.append(romanizer.romanize())

twice_words_romanized = []
for word in twice_words:
    romanizer = Romanizer(word)
    twice_words_romanized.append(romanizer.romanize())

blackpink_words_romanized = []
for word in blackpink_words:
    romanizer = Romanizer(word)
    blackpink_words_romanized.append(romanizer.romanize())


# create bar chart for each group

plt.figure(figsize=(20,10))
plt.bar(gfriend_words_romanized, gfriend_freqs)
plt.title('GFriend word frequency')
plt.xlabel('Words')
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(20,10))
plt.bar(twice_words_romanized, twice_freqs)
plt.title('Twice word frequency')
plt.xlabel('Words')
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(20,10))
plt.bar(blackpink_words_romanized, blackpink_freqs)
plt.title('BlackPink word frequency')
plt.xlabel('Words')
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.show()



