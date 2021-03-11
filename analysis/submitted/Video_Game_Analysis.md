# Videogame Analysis EDA
---------------------



## Instructions:
- You should remain focused on your research question(s) - it is very easy to get lost down rabbit holes in data analyses projects.

- If you find that your research questions are not that interesting, or you find more interesting questions (especially after your EDA) you may revise them, or add more.

- Use the lab times, as well as our office hours (TAs and instructors), to get help and guidance on your analyses.

- You should experiment with “plenty of” data visualizations to try and visualize your dataset and answer your research questions.

- Give us a narrative/story of your explorations as you go along, in-line with your data - use the new Markdown skills you learned in Task 1!

--------------------------
## Initialization:
```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas_profiling as pdp

sns.set_style("ticks")
import sys
sys.path.insert(1, '../scripts')

# Imports the project_functions.py file containing the different functions
import project_functions
```
-----------------------
## Intro
This analysis looks at the different aspects of videogames over the past ~40 years using a random samples of videogames, representative of the entire industry, to relate real life qualitative events to measurable changes in the sales and consumption of videogames.

The data used in this analysis was obtained from [kaggle]("https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings"), and is a user compiled data set of videogames, which extends a scrape already performed by Metacritic, *"a website that aggregates reviews of films, TV shows, music albums, video games and formerly, books"* [Wikipedia] (https://en.wikipedia.org/wiki/Metacritic). It includes over 16,000 unique video games, of which 6,825 have all entries complete.

This dataset does not contain all videogames from 1980-2016, and and so in this analysis it is considered a sample of that set of all videogames.
each videogame can have up to 16 associated pieces of information, here is a description of each of them:

| Column Name     | Description |
| ----------- | ----------- |
| Name      | The name of the videogame       |
| Platform   | The hardware need to play this videogame        |
| Year_of_Release      | The year this game was first released       |
| Genre   | What genre this videogame falls under(i.e. sports, shooter, racing)        |
| Publisher      | The name of the company that finances the development and production of this videogame       |
| NA_Sales   | The Number of units sold from its release until 2016 in North America(millions) |
| EU_Sales      | The Number of units sold from its release until 2016 in Europe (millions|
| JP_Sales   | The Number of units sold from its release until 2016 in Japan (millions)|
| Other_Sales      | The Number of units sold from its release until 2016 in Regions outside of North America, Europe and Japan       |
| Global_Sales   | The Number of units sold from its release until 2016 World Wide(millions)      |
| Critic_Score      | mean of all ratings given by 'Critics'  (1-10)  |
| Critic_Count   | the number of 'critic' ratings |
| User_Score      | mean of all ratings given by 'non-Critics'  (1-100)  |
| User_Count   | The number of 'non-Critic' ratings |
| Developer      | The name of the company who developed or programmed the videogame |
| Rating   |the ESRB rating of the game (according to the ESRB [ratings guide](https://www.esrb.org/ratings-guide/))|
*critics are considered to be "Metacritic staff", non-Critics are considered to be Metacritic subscribers*

all analysis performed first cleans the data as described below:
  - removing all rows with na entries
  - removing user scores with TBD
  - casting all entries in the table to their proper datatypes (they are all saved as strings), i.e. integers, floats, categories
below is the head of our cleaned data:
```
Cleaned_DataFrame = project_functions.load_and_process()
Cleaned_DataFrame.head()
```
-----------------
## Platform
A videogame platform is the hardware used to play the videogame, and although it may seem arbitrary which culmination of plastic, circuitry and ingenuity is used to play a videogame, there are very big differences between them, both statistically and culturally.

Because of these differences, different platforms *can* act as an isolated instance of videogame markets, where we can see how videogames succeed based on certain conditions which vary for each platform.
*figure xxx* below shows the total number of videogame units sold on each platform, worldwide, if this number is more than 8,000:

//insert global sales over all time for each platform//
*figure xxx*

We should first consider that biases towards certain platforms will exist. This bias, although minimal, is most obvious when comparing by region. The culture and history of each region most certainly has an effect on the platform purchased by a particular individual.

Hopefully from this we can find some basic indicators for the success of a videogame, by looking at the different Platforms games are released on. The focus will be on three things:

- ** *What correlation, if any, exists between the number of videogames available and the sales of videogames?* **
- ** *how does the timeframe the console is active for affect its sales?* **
- ** *Is competition a big factor in sales(does less competition mean more profits)?* **
#
### **data setup**
for the analysis of this section, the data was organized as follows:
- the data was filtered to only include the columns with names: **'Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'EU_Sales', 'NA_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'User_Score'**
- then sorted by console, and name
These changes made the data easier to process for the purpose of platform comparison

#
### **Regional Bias**
As mentioned previously, we will look at how the sales of videogames from particular platforms differ by region, mainly just to see how the bias changes. We will do this by counting the number of videogames on each platform, which have sales greater than 10,000 USD in each region.
If one were to use only videogames available to all platforms, there would be very little data to observe so for this purposes of this analysis we will consider all videogames available to each platform.
the data is shown below in *figures 1.1-1.6*:


//insert regional biases//
*figure 1.1* *figure 1.2* *figure 1.3* *fig*

Although the order of the number of videogames bought in each region for each platform varies from region to region, the general proportion of unique videogames purchased on each platform remains very similar.
the region which sticks out the most is Japan, the general groupings of the Platforms remains the same but the order of those groupings change, i.e. the top 3 platforms with the most unique videogames are the same as the other regions however, PS2 is not #1 but #3.

Regional bias does play a part in the popularity of platform, but there are other factors which play a more significant role in determining the success of a platform.
#
### ** Number of available videogames **
We started with the data from *figure xxx*, which shows the PS2, Xbox-360 (X360), and PS3 far ahead of the competition, this is hardly surprising given the increase in popularity of videogames after the release of the original Playstation (PS). From here we plotted the number of unique videogames available to the number of global sales on that platform, to obtain the *figure zzz*:

///insert global sales and games available///
*figure zzz*

from *figure zzz* we could see that there was a clear correlation between the number of videogames available and the videogame units sold worldwide, which is to be expected. This didn't really reveal much, as having more goods available will genrally lead to more sales, so we decided to normalize the data, according to the number of videogames available, so we could see the mean number of videogame units sold for each console.

We then looked at the same figures after they were normalized, first *figure yyy*:

///insert mean global sales over all time for each platform///
*figure yyy*

and then *figure aaa*:

///insert Normalized global sales and games available///
*figure aaa*

from *figures aaa and yyy* we can see that the PS and Wii platforms, have teh highest mean number of units sold per videogame, and that the previous leaders, were still competetitive but did not standout as they did previously. Particularly *figure aaa* provided clear insight that releasing lots of videogames for a particular console had no straight-forward correlation to the number of units those videogames would sell. 
We think this is pretty clear, but if you believe otherwise I challenge you to divine a simple relationship between the mean number of units sold per videogame, and the number of videogames available(using *figure aaa*). 

It should be safe to say that releasing lots of videogames for a particular platform does not guarantee the quality of those videogames, and this is very strongly reflected in *figure aaa*
#
### ** Platform timeframe **
You would assume that a platform which has been releasing videogames over a longer period of time would be more succesful, as they would have more experience in the market. This is not necessarily true though as is shown below.

Let's first have a look at the distrbution of videogame releases for each platform, by making a box and whisker plot, *figure bbb*:

///insert distribution of games for each console///
*figure bbb*

here we can see that the lifespan of all of these platforms tends to be 4-10 years, with the GBA having active videogame releases for only 4 years, and the PS2 having active releases for a little over 10 years. The PC is the obvious outlier having released videogames for over 30 years, so we will end up removing it after confirming there is no fair comparison to it, as of 2016.

Let's know have a look at the mean year of release for videogames on each platform, which is representation of what years the console was active for, and see if we can discuss what events may be behind the trends, see *figure ccc*:

///insert Expected year of release vs global sales///
*figure ccc*

from *figure ccc* we can see that there is an outlier in the PS2 and a spike in 2008-10 for certain platforms. Given our knowledge of the massive success of the PS, we can safely assume that the PS2's success was somewhat thanks to the rapport that people had with SONY (creator of the PS). This in turn propbably caused an increased demand for videogames, allowing the next generation of platforms (PS3, X360, Wii) to all experience great sales.

The generation after *that* was different yet again and was when, we believe, the competition between platform developers started to impact sales more definitively.
#
### **competition and true comparison**
The competition between platform developers was somewhat limited before 2010. One reason for this could be the limited online multiplayer experience before then, as once this environment became popular it was very important which platform you were playing on.

So lets compare two consoles who have had feirce competition after this boom in online gaming, and are also somewhat similar in the lenght of time they have been around, see *figure ddd.1*:

///insert global sales and years active for consoles///
*figure ddd*

obviously PC is an outlier, so we removed it as predicted:

///insert global sales and years active for consoles///
*figure ddd.1*

The XOne and PS4 are a pretty good choice, although relatively new, they are very similar, having been released within 7 days of each other.

The global sales of the XOne, are half that of the PS4, and the mean global sales of PS4 are 1.3 times that of the XOne, so there are some comparisons to be made.
the figures however appear to say that the only difference is found in the regional sales, where PS4 beats out XOne everywhere except north America, suggesting simply a high quality of product.

///insert X and PS4 pngs///

Microsoft produces XOne consoles and is based in North America, which leads to the assumption of brand loyalty and this idea of American Manufactoring and Nationalism tipping the scales in favor of XOne only in NA, whereas the rest of the world appears to choose the PS4.


We could also look at the critic and user score averages for the games, and we can see that the critic ratings are approximately the same:( */100)

XOne: 73.729560
PS4: 72.669456

but the user scores: ( */10)

XOne: 6.493082
PS4: 6.739331

lean slightly in favour of the PS4, by about 2.4\% compared to the difference in critic scores: 1.1\%

This in combination with the larger number of games might explain the PS4 mean Global Sales being slightly higher than the XOne mean global sales

#

- There doesn't appear to be any correlation between the number of videogames available and the mean sales of those videogames (there will be good selling videogames and badselling videogames, making more doesn't guarantee good or bad)
- the timefram a console is active for does appear to have a big impact on global sales, see PS3, X360, and Wii, following well selling consoles
- Competition does have a relatively large impact on sales


--------------------
## Genres, Ratings, and Sales
When it comes to videogames, people, like with music, movies, books, etc., have their natural preferences. The main objective of this section is to try and establish which are the more common preferences of people with regards to the different videogame genres that there are, and if there is a specific rating that these games or genre tends to fall under. 

To answer this, there are two main questions to focus on:
- Which videogame *genre* tends to *sell better / more*?

- What is the *correlation* between *game ratings, sales, and genre*?

On the topic of videogame ratings, this dataset uses Entertainment Software Rating Board (ESRB) Ratings ratings to rate the videogames. The ESRB was created in 1994 (under a different name back then) and the ratings have changed over time. In 1999, the ratings took form into those we see and recognize today.

Through the EDA conducted while looking to answering the question on the potential correlations between the videogame ratings, sales, and genre, we came across games which had been rated by the ESRB but predated 1994...

How was this possible? This lead to us introducing and seeking to answer a third question for this section:
- When did the ratings first begin for videogames? 
  If the game was from before 1994, how/why was it rated?

#

Knowing what the areas of interest were in the column, we started off the EDA by focusing the data down to what was of interest: Names,For the top three genres, we want to quickly take a look at some of the top sellers in each genre and check if there are any game series or titles that are easily recognizable.  Genres, Ratings, Global Sales, and Years of Release. We created a new dataset which was specifically to help answer these three questions, and chose to drop all the other dataset columns minus these five select ones.

When looking into the Ratings column, we saw that there were still *"outdated"* ratings being used, in particular, the *K-A* rating. In 1994, the *K-A* rating, which was for Kids-Adults, was replaced with the *E* rating, which was for Everyone. To keep things consistent with the later games (since there is only one *K-A* rating in the entire cleaned dataset), we changed the *K-A* to *E* rating - avoiding any outliers in the data.

With things cleaned further, we first made sure to take note and store the unique values for the Genres and the Ratings. These variables, kept as lists, would become useful later in the code when answering the questions of interest.

With everything set up and ready for the EDA, we can now begin looking to answering each of these three questions. 

#

### *Which videogame genre tends to sell better / more?*
To answer this, we plotted the unique genres versus the total global sales for that genre.
Below, the plot for the Videogame Genres vs Global Sales can be seen.

![Videogame Genres vs Global Sales](https://github.com/data301-2020-winter2/course-project-group_1019/blob/main/analysis/Eduardo/Milestone%202/Eduardo_EDA_Plots/sales_by_genre.png)

From the above bar chart, we see that the *most popular game genre* is Action, followed by Sports and Shooter close behind.

Action games include your Grand Theft Auto (GTA) games, Assassin's Creed games, Uncharted games, etc. Most of these games are a part of larger series, often having more than two, three, and more in the overall game collection. As a result of this, and the sheer amount of games, there are 1630 games which are Action games. 

For Sport games, we see that there is a total of 943 games. Sport games are fairly self explanatory, and include games like FIFA games, Wii Sports, NBA games, Madden, etc.

Finally, Shooter games tend to be first person shooters, like the well known Call of Duty game series, and more games similar to that. In this genre, there are 864 games.

Since there is such a variation in both the sales, roughly 1.2 billion, 833 million, and 816 million units in sales for Action, Sports, and Action games respectively, and the number of games in each genre, we were left wondering if the Action games genre came out first solely due to the fact that it had the most games, and therefore the more selling potential. 

To address this, we chose to normalize the bar chart, to show how much a game of each genre will make *on average*! Like this, we can more accurately see which game genre tends to make the most sales per game.

![Videogame Genres vs Global Sales Normalized](https://github.com/data301-2020-winter2/course-project-group_1019/blob/main/analysis/Eduardo/Milestone%202/Eduardo_EDA_Plots/sales_by_genre_normalized.png)

Here we now see that the majority of  game genres sell between 650-850 thousand units with the high being for the Misc genre, which on average makes roughly 1.1 million units per game. Now, Misc, Platformers and Shooters, and Sports games genres tend to sell the most units per game on average.

The genre Misc includes a varied array of games, the category itself being a game which does not fit into any of the other mentioned categories. These games tend to be the digital board games or card games, Chess games, Wii Play, Kinnect games, the Just Dance series and more. As a result, the games in this section appeal to many, and makes logical sense that such a diverse genre tends to garner the most attention and sells the most units per game on average!

Therefore, to answer the original question, the top game genres sell roughly between 800,000 units to a million units on average, with the majority of the rest falling between 650,000 to 750,000 units on average. The most popular genres are Misc, Platformers, Shooters, Sports, and Racing games. The least popular games came out to be Strategy and Adventure games, doing significantly worse than the other genres. 

#

### *What is the correlation between game ratings, sales, and genre?*
To address the next question, we looked predominantly into the ratings and the sales for the games. Knowing that most genres tend to gravitate towards certain ratings (like shooters tend to be rated M, and most sports games would be rated as E), we wanted to see if a game's rating influences the sales it could make. 

Again, like in the previous question, the unique Ratings for videogames was plotted against the sales, and then this plot was normalized, as the same issue with the first question (of having significantly different batch sizes for the ratings) would present itself once again.

In this dataset, the ratings that are present are E, M, T, E10+, AO, and RP. These ratings are for Everyone (all ages), Mature (ages 17+), Teen a(ages 13+), Everyone 10+ (ages 10+), Adults Only (ages 18+), and finally Rating Pending, for games which have not yet recieved a final ESRB rating. 

![Videogame Ratings vs Global Sales](https://github.com/data301-2020-winter2/course-project-group_1019/blob/main/analysis/Eduardo/Milestone%202/Eduardo_EDA_Plots/sales_by_rating.png)

From the above bar chart, we see that the games which are rated *E* for Everyone are the *most sold game rating*. Follwoing closely behind are those games rated *M* for Mature and *T* for Teen. Games rated *E* sold almost 2 billion units worth of games, while games rated *M* and *T* sold roughly 1.4 and 1.3 billion units worth of games apiece.

Now, as we did with the previous question, we will normalize this plot and check again to see which videogame rating tends to sell the most units again on average. We make sure to do this because we have in total 2083 E rated games, 1433 M rated games, and 2377 T rated games. There is some differences between the the number of games rated *E* and those rated *T*. Yet, interestingly enough, we see clearly here that more of a game rating does not mean that the game will sell more! This was not the case represented in the previous question!

![Videogame Ratings vs Global Sales Normalized](https://github.com/data301-2020-winter2/course-project-group_1019/blob/main/analysis/Eduardo/Milestone%202/Eduardo_EDA_Plots/sales_by_rating_normalized.png)

From this normalized plot, we can see that M rated  games and E rated games appeal to the greatest and most general audience, which makes sense that they should be topping the global sales list with roughly a million units sold on average per game. The other two ratings which are for T and E10+ both made roughly 600 thousand units sold. RP did not have very many entries in the dataset, and finally, the major outlier in this graph is the AO. 

In the entire dataset, we see that there is only 1 game that is rated AO. This game is Grand Theft Auto: San Andreas, which released in 2005.

However this game also appears to originally have been sold in 2004 and was rated *M*. So, we went on to see what was unique about this seperate release. It just so happens that the developers had removed some more explicit features from the original base game which released in 2004, but that gamers had found a way to access this *"removed"* content which was hidden, yet left in the game's source code... 

This version of the game came into circulation and sold almost two million units, and the ERSB rated this game as Adult Only AO in an effort to warn people about the graphic content portrayed in the game. 

With the exception then of the AO rating, we see the majority of the games rated sell at roughly 550 thousand units to a million units on average. E and M rated games sell best, with T and E10+ selling decently but behind E and M rated games. These results show that E and M rated games sell best, and they also (together) cover one of the greatest ranges of games and game genres! 

#

### *When did the ratings first begin for videogames? If the game was from before 1994, how/why was it rated?*

This final question can be answered quite simply, and we did not need any plots or major tables to answer it. It only took a few lines of code and some analysis to reach our conclusions. 

With this analysis, to check what was the earliest rated game on the list, the year it came out in (originally - this distinction will be important!) and the name of the game, we use dataframe code to find it. 

In the end, we found that this game was *"Alter Ego"*, which was released in 1985 for the Commodore 64, MS-DOS, Apple II, and the Apple Macintosh, and is rated as T by the ESRB. As mentioned earlier when this question was raised, how is it that a game released prior to the creation of the ESRB has an ESRB rating?

The answer to this is that the game *"Alter Ego"* was in fact re-released on the PC in 2010, and that it is this version (which is virtually idential to the original 1985 version) that was rated by the ESRB, and the rating for the 2010 version extended to the 1985 version. We checked the two other games which are listed as being rated but were also originally released prior to 1994. These games are *SimCity* and *Doom* - both of which have since been re-released multiple times over since their original releases, thus these games being rated makes sense.

The first game (according to the dataset after it was cleaned) that was rated by the ESRB on its *original* release was *"Battle Arena Toshinden"*, which released on the original PlayStation in 1994 and was rated T for Teen. This confirms that the original games rated by the ESRB was in the year it was created in, in 1994. In the years following 1994 and the creation of the ESRB, we see more and more games steadily gain their ratings, which makes sense and is what we expect to see. 

------------------
### *Which Publisher has the Most Sales Per Regin?*
#The Publisher with the Most Sales per Game Globally is: Nintendo
#The Publisher with the Most Sales per Game in North America is: RedOctane
#The Publisher with the Most Sales per Game in Europe is: GT Interactive
#The Publisher with the Most Sales per Game in Japan is: SquareSoft
#The Publisher with the Most Sales per Game in Other Regions is: Hello Games



------------------
## more stuff
------------------
## Conclusions