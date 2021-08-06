# K-Pop: How Popular Is It?
## Comparing 10 Years of Popular Music from *Billboard* Hot 100 Using Spotify API's Audio Features
Made in collaboration between [Jessica Veilleux](https://github.com/jveilleux2314), [Kailey Davis](https://github.com/kaileymd), [Kenneth Beadle](https://github.com/K-Beadle), and [Miranda Wylie](https://github.com/mirandawylie)

K-Pop, or popular music from Korea, is having its moment in the U.S.: its popularity and dedicated fan base have caused cultural waves that touched [the 2020 election, sparked political activism](https://www.cnn.com/2020/06/22/asia/k-pop-fandom-activism-intl-hnk/index.html) and created wildly popular merchandising deals, like [one K-Pop band's McDonald's Meal](https://www.businessinsider.com/mcdonalds-bts-meal-drives-traffic-to-restaurants-over-travis-scott-meal-2021-6). With as much influence as K-Pop has outside of the music world, we wanted to know: how popular is K-Pop music, actually?

### Music Popularity
There are many elements to what makes music popular. We decided to rely on the *Billboard* charts from 2010 - 2020 to indicate which songs we should look at and use Spotify's API to pull the audio feature breakdown for each song.

### What Do We Hope to Find?
Using the data from Spotify on the last 10 years of popular music, we hope to see if K-Pop's rankings in the charts reflects its popularity in news headlines. Specifically, we will be looking at the popularity of the top 7 music genres from *Billboard* over the last 10 years to discover trends that show how they rank compared to each other and if Spotify's audio feature data can reveal signature audio features for any genre that may make it more or less popular.

Additionally, we will be training a machine learning model using Spotify's audio features to predict if a song will stay on the Hot 100 charts for longer than the average (12 weeks).

## Music Analysis

### Popularity
[Popularity of Genre Over Time](/Kailey/Images/Genre_over_time.png)

K-Pop is a new genre to the U.S. It hit the Hot 100 in 2012 with Psy's *Gangnam Style* and has consistently stayed on the charts since. While its popularity on this graph appears to be low, it is largely influenced by the number of songs in that genre that hit the charts.

[Average Weeks on Board](/Kailey/Images/Avg_Weeks_on_Board.png)

The K-Pop songs that do hit the Hot 100 are much more popular than songs of other genres. The average length of time for any song to stay on the Hot 100 is 12 weeks; K-Pop songs average 17.8 weeks and its nearest competitor, Dance songs, average 13 weeks.

Due to the low number of K-Pop songs on the charts over the last 10 years (8,000 compared to nearly 216,000 dance songs) it is hard to say if this staying power is because only the best of the best make it to U.S. audiences, or if there is some other quality that makes K-Pop stand out.

### Spotify Audio Features
[Audio Features](Kailey/Images/Audio_Features.png)

Spotify assigns every song audio feature values, a value between 0 and 1 representing how much of that feature Spotify believes is present in that song. What immediately stands out is how many features are similar to each other across genres - indicating that songs popular enough to hit the Hot 100 already have a lot in common in areas like energy and acousticness.

[Audio Features](Kailey/Images/Audio_Features_kpop.png)

K-Pop mostly differs on instrumentalness, liveness, and speechiness. instrumentalness and speechiness are similar measurements, where speechiness indicates a ration of spoken words vs. music in a track and instrumentalness predicts if a song contains vocals, indicating the presence of vocals and how much they *sound* like spoken words, discounting lyrical noises like "ooh" and "ahh". Liveness detects the presence of an audience.

These are unique features - scoring low in both instrumentalness and speechiness could indicate either a key difference in song composition, or a flaw in Spotify's algorithm when analyzing foreign languages. Scoring so different in liveness is a commentary on how K-Pop bands represent themselves online. In Korea, these bands are known as "idol groups" and are meant to be role models - primarily releasing polished, studio versions of their songs fits the perfect, polished image of these idols.

## Can AI Predict Everyone's New Favorite Song?

### Machine Learning
While Spotify's audio features are difficult to interpret when grouped by genre, can they still tell us something about a song's popularity? The average song on the Hot 100 stayed for 12 weeks. We asked our machine learning model to predict if a song would meet or beat the average, or would the song underperform?

We tested our data using a neural network model and a Random Forest model due to what we assumed would be complex relationships between our data points. From our complete data set, we only used pre-existing numeric fields - the Spotify audio features, Spotify's popularity metric, and the Hot 100 song ranking. No further numeric manipulation was necessary to scale the features since they were already similar.

The Random Forest model was our best performing model, at 73.3% accuracy.

[Random Forest Model Performance](Kenneth/ML png's/RandomForest_confusion_matrix.png)

To help us understand what influenced our model, we had it list the features it used in order of importance.

[Random Forest Feature Importance](Kenneth/ML png's/RandomForest_features.png)

A song's ranking on the Hot 100 had the most importance and influence on our model by a significant margin. Spotify's audio features were not very useful to our model, but we were able to create a model that can predict with some accuracy if a popular song will stay on the charts for longer than average.

## Conclusion
Since 2012, K-Pop has shown that it has the ability to stay relevant to U.S. audiences. As massively popular groups like BTS (the band behind *Butter* and *Permission to Dance*, both #1 hits summer 2021) continue to spread awareness of the genre, interest in K-Pop will continue to grow in the U.S.

Spotify's audio features, while interesting, are mostly inconclusive. Our machine learning model shows that the most important feature for helping to determine how long a song will stay on the Hot 100 *is* its ranking - in other words, the more popular you already are, the more likely you are to stay. Spotify shows that popular songs often have similar features, but at this level of popularity, those features aren't very useful to differentiate songs from each other.

So does K-Pop's reputation in the headlines as a hot new trend reflect its popularity in the music world? While nothing conclusive stands out from its audio features, K-Pop hits are beloved - meaning that their popularity likely lies *within* their reputation, and with other indicators outside of the purely musical realm.




## Data Sources
- [Billboard Hot 100 from Kaggle](https://www.kaggle.com/dhruvildave/billboard-the-hot-100-songs) which documents the position of every song on the Hot 100 from week to week since the 1950's.
- [Spotify API](https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-recommendations) to discover a song's acousticness, danceability, energy, and other audio features.
- [Spotify csv from Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv) to assist with genre classification.
