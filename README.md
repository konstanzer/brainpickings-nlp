<a href="https://brainpickings.org">
	<img src="/img/logo.png" alt="brainpickings logo" title="BrainPickings" align="right" width="200"/>
</a>

"A museum of my mind": A Natural Language Processing Perspective of BrainPickings.org
======================

"One of the great cruelties and great glories of creative work is the wild discrepancy of timelines between vision and execution. When we dream up a project, we invariably underestimate the amount of time and effort required to make it a reality. Rather than a cognitive bug, perhaps this is the supreme coping mechanism of the creative mind — if we could see clearly the toil ahead at the outset of any creative endeavor, we might be too dispirited to begin, too reluctant to gamble between the heroic and the foolish, too paralyzed to walk the long and tenuous tightrope of hope and fear by which any worthwhile destination is reached." -Maria Popova

## Contents
- [Overview](#overview)
- [The Site](#ovethe-siterview)
- [The Posts](#the-posts)
- [Hypotheses and Method](#Hypotheses-and-Method)
- [Results](#Results)
- [Acknowledgements](#Acknowledgements)

___

## Overview

Began in 2007, Brain Pickings has grown into one of the most popular blogs worldwide in a very competitive space. With diverse topics including art, literature, science, and philosophy, the blog has been described as a "museum of the world" and a "treasure trove." It has millions of unique readers per month and both Tim Ferriss and James Altucher, popular authors and bloggers in their own right, say Brain Pickings is the only blog they read regularly. Given the amount of thoroughly-researched content on Brain Pickings, one would reasonably assume that a staff of writers is behind it. In fact, Maria Popova is the sole author of every article on the blog and she maintains her site without a single advertisement, relying, as Wikipedia does, on donations.

As of April 2021, Brain Pickings has amassed 5,700 articles totaling over 5 million words. To put this accomplishment in perspective, Ms. Popova has published a 900+ word article every 21 hours...for 13.5 years. This project gave me the opportunity to dive into the evolving themes of Brain Pickings based on frequently occurring words and phrases throughout the body of work.
___

## The Site
Brainpickings.org is conveniently organized in chronological fashion, with most recent posts appearing on page 1 and the oldest posts appearing on the last page, numbered 1426 at time of writing. This fact made acquiring the data for the following steps via Requests relatively straightforward. From there, a search of the articles' HTML revealed the header below which posts are recorded. I parsed this data, including title, date, subtitle, and the articles themselves, with the help of BeautifulSoup. Finally, I added a word count function before saving the data in a .csv file.
___

## The Posts

By way of summary.

Word output peaked in 2014 |  Post-frequency increased in 2011
:-------------------------:|:-------------------------:
<img alt="" src="img/words.png" width='400'>   |  <img alt="" src="img/posts.png" width='400'>

For this graph, I removed the "culture" tag as it showed up in an overwhelming majority of posts. Based only on tags, one would assume the blog is usually about culture and books.

<img alt="" src="/img/tags.png" width='400'> 


**Thematic trends**

For these graphs I did remove the "books" tag to show lesser-used tags in greater detail. The same statement applies, that is, in both periods, culture and books are the most used tags.

Popular tags (2007-mid 2014) |  Popular tags (mid 2014-April 2021)
:-------------------------:|:-------------------------:
<img alt="" src="img/early_tags.png" width='800'>   |  <img alt="" src="img/late_tags.png" width='800'>

In reply to direct communication with Ms. Popva, I generated this plot showing the trends of three tags in particular. Most evident is an increasing interest in poetry.

<img alt="" src="/img/lovepoetsci.png" width='800'> 

___

## Hypotheses and Method

In this section, I describe the results of three hypotheses tests perfored with the `ttests.py` script. The tests examine four pitches thrown by each pitcher (fastballs, sliders, changeups, and curveballs) and four measurments for each of those pitches (release speed, release spin rate, late horizontal movement, and late vertical movement,) In all cases, I use a Welch's t-test; some of the sample sizes are uneven. Thos is due to the fact that Cole favors curveballs and deGrom favors changeups. In order to perform a Welch's t-test, I use `scipy.stats.ttest_ind`.

`result = scs.ttest_ind(df_cole[df_cole.pitch_type==pitch][stat], df_degrom[df_degrom.pitch_type==pitch][stat], equal_var=False)`


### Hypothesis the first: FF + release_speed

**Scientific Question**
    
   Are the the mean fastball release speeds between Jacob deGrom and Gerrit Cole the same?

**Conclusion**

   We have a p-value and need to compare it to our significance level of 0.0125. The p-value (the probability of seeing this result or a result more extreme given the null hypothesis) is far less than the significance level. Therefore, my conclusion is:
   
   I **reject the null** hypothesis that the release speed means are the same.
   
___

   
## Results

Continuing in this way with through each of rhe four pitches thrown by Jacob deGrom and Gerrit Cole in 2020 (faastball, slider, curveball, and changeup) for each of the four meaurements in my DataFrame, I was able to draw the following conclusions. In all tests, I use a Bonferonni correction of 4 to account for the fact that I am comparing multiple means of pitch measurements. Therefore, my signficance for each individual test is 𝛼=0.05/4 = 0.0125.

### Fastball

#### Total observations:
* Gerrit Cole: 635
* Jacob deGrom: 510

| Measurement       | p-value | 𝜇Cole     | 𝜇deGrom   | RTN |
|-------------------|---------|-----------|-----------|-----|
| release speed     | 4e-136  | 96.7      | **98.6**  | Y   |
| release spin rate | 0.0001  | **2505**  | 2477      | Y   |
| lateral movement  | 5e-282  | **-1.01** | -0.58     | Y   |
| vertical movement | 4e-35   | **1.49**  | 1.39      | Y   |

___

	
## Acknowledgements
* Maria Popova, without whose disciplined habits and willingness to share her work, readers like myself would be deprived of an incredible resource of wisdom and erudition.
* Dan Rupp, data science instructor at Galvanize Austin, for his excellent suggestions regarding the selection of the feature space and interpretation of the model results and Dr. Juliana Duncan, lead data science instructor at Galvanize Austin, for her leading questions and conceptual help with statistical topics.

