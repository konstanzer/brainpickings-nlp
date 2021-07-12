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
- [Building a classifier](#building-a-classifier)
- [Results](#results)
- [Acknowledgements](#acknowledgements)

___

## Overview

Began in 2007, Brain Pickings has grown into one of the most popular blogs worldwide in a very competitive space. With diverse topics including art, literature, science, and philosophy, the blog has been described as a "museum of the world" and a "treasure trove." It has millions of unique readers per month and both Tim Ferriss and James Altucher, popular authors and bloggers in their own right, say Brain Pickings is the only blog they read regularly. Given the amount of thoroughly-researched content on Brain Pickings, one would reasonably assume that a staff of writers is behind it. In fact, Maria Popova is the sole author of every article on the blog and she maintains her site without a single advertisement, relying, as Wikipedia does, on donations.

Ms. Popova defined herself as a "spiritual embryo" at the outset of her blog. Initially, she distributed her work in the form of an email to a few close friends. As her reading and writing habit evolved from a pastime into a morning-to-night obsession, her writing adopted a highly-referential, associative style evoking long-dead authors and little-known historical events. The reader rarely encounters a personal remark in her writing, adding an element of detachment and even mystique to her insights. Rather than explore her struggles both personal and intellectual in the first-person therapy, she finds answers in the "original hypertext," her phrase for the literary canon our generation has inherited but frequently ignored. In trailblazing a path through the common record, she has found an enormous following online, demonstrating that the personal truly is the universal.

As of April 2021, Brain Pickings has amassed 5,700 articles totaling over 5 million words. To put this accomplishment in perspective, Ms. Popova has published a 900+ word article every 21 hours...for 13.5 years. This project gave me the opportunity to dive into the evolving themes of Brain Pickings based on frequently occurring words and phrases throughout the body of work.

___

## The Site

Brainpickings.org is conveniently organized in chronological fashion, with most recent posts appearing on page 1 and the oldest posts appearing on the last page, numbered 1426 at time of writing. This fact made acquiring the data for the following steps via Requests relatively straightforward. From there, a search of the articles' HTML revealed the specific header below which each post is recorded. I parsed this data, including title, date, subtitle, and the articles themselves, with the help of BeautifulSoup. Finally, I added a word count function before saving the data in a .csv file.

<p align="center">
	<img alt="" src="img/techslide.png" width='700'>
</p>

___

## The Posts

By way of summary, I observe an increase in ouput to multiple postings per day as the blog gained in popularity. Posting frequency has tapered off to a mere mortal rate of every-other-day in recent years.

Word output peaked in 2014 |  Post-frequency picked up in 2011
:-------------------------:|:-------------------------:
<img alt="" src="img/words.png" width='1000' height='250'>   |  <img alt="" src="img/posts.png" width='1000' height='250'>

**Thematic trends**

For these graph, I omitted the "culture" and "books" tags as they showed up in a vast majority of posts, dwarfing the relative differences between lesser used but more informational tags. Based only on these tags, one would assume the blog is about culture and books, and while this is true, the actual topics Ms. Popova covers in this "museum of the mind" are far more diverse. The changes I identify in between her early to late periods are from sensory- to textual-based topics, or seen another way, from right-brain to left-brain if I may make a neurological inference. Design, cinema, and music morph to philosophy, poetry, and letters.

Popular tags (2007-mid 2014) |  Popular tags (mid 2014-2021)
:---------------------------:|:-------------------------:
<img alt="" src="img/early_tags.png" width='1000' height='250'>   |  <img alt="" src="img/late_tags.png" width='1000' height='250'>

<p align="center">
	<img alt="" src="/img/venn_di.png" width='400'> 
</p>

Ms. Popova expressed an interest in three particular categories, love, poetry, and science, in a single email exchange at the outset of this project. In corcordance with this interest, I generated a plot showing the relative frequency of these tags over time. Most evident is an increasing interest in poetry.

<p align="center">
	<img alt="" src="/img/lovepoetsci.png" width='800'> 
</p>

___

## Building a classifier

I built a classification model that would predict whether an article was from Ms. Popova's early or late era, defined here as 2007-2013 and 2015-2021. These dates coincide nicely with her twenties and thirties respectively. I hoped to capture some of what defines these epochs in terms of creative and intellectual development. 

### Dividing the classes

|                   | Early class  | Late class  |
|-------------------|--------------|-------------|
| years             | 2007-2013    | 2015-2021   |
| article count     | 3,069        | 1,931       |
| word count        | 1.94 million | 2.29 million|

While I have published true article counts here, I balanced the classes at 1,927 before modeling. I originally accomplished this with SMOTE (synthetic minority oversampling) of the late class. However, after further research, I chose to simply drop articles from the early class of the shortest length until the classes were even. This decision was based on the preponderance of very short articles in the early class versus the late class, the shortness of which would provide fewer key words to classify the text. In practice, this resulted in dropping 1,168 articles of under 290 words. Below is a histogram of word counts across all articles, evidently some kind of gamma distribution.

<p align="center">
	<img alt="" src="/img/wordcount.png" width='1200'> 
</p>

Astute obsevers will notice the omission of 2014 posts. This decision was made after an initial logit model showed half of all errors occurring in this dividing year. It makes sense that a classification model would have the most trouble distinguishing articles published closest together. Style is only binary to literary critics. Although 2014 was Ms. Popova's most productive year as a writer in terms of word count, I excluded it from the further models in order to increase class contarst and make a stronger classifier.

<p align="center">
	<img alt="" src="/img/logiterrorswith2014.png" width='500'> 
</p>

### Train-test split

With the data now labeled "early" or "late," I used an 80/20 split to divide the documents into training and testing data. 

### Creating the feature matrix

The `sklearn.feature_extraction` module provides a way to transform raw text documents into a numerical feature matrix suitable for machine learning algorithms. Vectorizing a text document requires tokenization, counting, and normalizing. Tf-idf (term frequency-inverse document frequency) is a term weighting scheme used to accomplish this feat. For each document (matrix row), the tf-idf vectorizer outputs a floating point for each feature (matrix column) that rewards both a high *intra*-document freqeuncy and a low *inter*-document frequency. In other words, the words most informative with regards to content receive the highest value. Significantly, this approach to language processing ignores semantic similarities.

#### Document frequency parameters

Having already identified broad themes with tags, I wanted to extract phrases, or *n-grams*, as a means of interpreting the documents. With a tf-idf vectorizer set to use bigrams (two-word phrases), I tuned the required document frequency of words using 5-fold cross-validation on a random forest classification model. My final parameters for this step were a minimum document frequency (`min_df`) of 1 percent and a maximum (`max_df`) of 10 percent. This model maintained a 93 percent classification accuracy with 3,500 features (out of an initial 973,0000 bigrams.)

#### Stop words and maximum features

Guessing the date of a blog post is absurd and a tool to reattach lost dates to posts is of use to no one. With this in mind, my aim was feature interpretability. Thus, adding stop words to the standard NLTK list was a process of repeatedly breaking a good model in order to simplify it. I honed in on proper names and unique phrases during this process whilst removing uninterpretable phrases such as "make sense" and "half century" that classified well but provided little insight. I whittled my initial list of 295 bigrams (with 88 percent accuracy using basic stop words) to 35 with a custom stop word list and the `max_feature` parameter. This very simple model had a cross-validation accuracy of 82 percent - decent not great. The final feature set ranked by average information gain across all weak learners is displayed below. 

<img alt="" src="/img/ginibigrams.png" width='600'> 

### Test set results

The final test set accuracy was 90 percent. I attribute this rise in accuracy over the cross-validation score to the fact that I did not artifically suppress phrases I deemed worthless, although total features were still capped at 35. As the confusion matrix shows, there is a discrepancy between recall (95 percent) and precision (86 percent) and this result is explored in the following partial dependence plots.

<img alt="" src="/img/matrixRF.png" width='350'> 


### Insights from a single decision tree

<img alt="" src="/img/tagtreefull.png" width='900'> 
<img alt="" src="/img/impurity.png" width='500'> 
<img alt="" src="/img/depth.png" width='400'> 

___

   
## Results

<img alt="" src="/img/pdps.png" width='900'> 
<img alt="" src="/img/pdp2d.png" width='500'> 
<img alt="" src="/img/pdp2d2.png" width='600'> 
<img alt="" src="/img/pdp2d3.png" width='500'> 

___
	
## Acknowledgements

* Maria Popova, without whose discipline, erudition, and wisdom, readers like myself would be deprived of a unique and valuable resource.

* Dan Rupp for suggestions regarding the selection of the feature space and interpretation of the classification model and Juliana Duncan for her leading questions and conceptual help with statistical topics.

