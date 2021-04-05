<a href="https://brainpickings.org">
	<img src="/img/logo.png" alt="brainpickings logo" title="BrainPickings" align="right" width="200"/>
</a>

"A museum of my mind": A Natural Language Processing perspective of BrainPickings.org
======================

"One of the great cruelties and great glories of creative work is the wild discrepancy of timelines between vision and execution. When we dream up a project, we invariably underestimate the amount of time and effort required to make it a reality. Rather than a cognitive bug, perhaps this is the supreme coping mechanism of the creative mind — if we could see clearly the toil ahead at the outset of any creative endeavor, we might be too dispirited to begin, too reluctant to gamble between the heroic and the foolish, too paralyzed to walk the long and tenuous tightrope of hope and fear by which any worthwhile destination is reached." -Maria Popova

## Contents
- [Overview](#overview)
- [The Posts](#the-posts)
- [Hypotheses and Method](#Hypotheses-and-Method)
- [Results](#Results)
- [Acknowledgements](#Acknowledgements)

___

## Overview

Began in 2007, Brain Pickings has grown into one of the most popular blogs worldwide in a very competitive space. With diverse topics including art, literature, science, and philosophy, the blog has been described as a "museum of the world" and a "treasure trove." It has millions of unique readers per month and both Tim Ferriss and James Altucher, popular authors and bloggers in their own right, say Brain Pickings is the only blog they read regularly. Given the amount of thoroughly-researched content on Brain Pickings, one would reasonably assume that a staff of writers is behind it. In fact, Maria Popova is the sole author of every article on the blog and she maintains her site without a single advertisement, relying, as Wikipedia does, on donations.

As of March 2021, Brain Pickings has amassed 5,700 articles totaling over 5 million words. To put this accomplishment in perspective, Ms. Popova has published a 1,000+ word article every 21 hours...for 13.5 years! This project gave me the opportunity to dive into the evolving themes of Brain Pickings based on frequently occurring words and phrases throughout the body of work.

___

## The Posts

**Stacked bar chart of pitch frequencies in 2020**

#### Total observations:
* Gerrit Cole: 1203
* Jacob deGrom: 1135

<img alt="" src="/img/mcghee.png" width='800'> 

___

**Boxplots of speed, spin rates, and movement lateral and vertical**

#### Key takeaways:
* Cole has a higher average speed and deGrom has a higher top speed. .
* Cole has a higher average spin rate and deGrom has a bigger range of spin rates.
* deGrom's stratgy may rely on changing spin and speeds.
* Cole has a higher average movement in both the x and z axes.

Release speeds             |  Release spin rates
:-------------------------:|:-------------------------:
<img alt="" src="src/visuals/release_speed_boxplot.png" width='400'>   |  <img alt="" src="src/visuals/release_spin_rate_boxplot.png" width='400'>

Lateral movements          |  Vertical movements
:-------------------------:|:-------------------------:
<img alt="" src="src/visuals/pfx_x_boxplot.png" width='400'>   |  <img alt="" src="src/visuals/pfx_z_boxplot.png" width='400'> 

___

## Hypotheses and Method

In this section, I describe the results of three hypotheses tests perfored with the `ttests.py` script. The tests examine four pitches thrown by each pitcher (fastballs, sliders, changeups, and curveballs) and four measurments for each of those pitches (release speed, release spin rate, late horizontal movement, and late vertical movement,) In all cases, I use a Welch's t-test; some of the sample sizes are uneven. Thos is due to the fact that Cole favors curveballs and deGrom favors changeups. In order to perform a Welch's t-test, I use `scipy.stats.ttest_ind`.

`result = scs.ttest_ind(df_cole[df_cole.pitch_type==pitch][stat], df_degrom[df_degrom.pitch_type==pitch][stat], equal_var=False)`


### Hypothesis the first: FF + release_speed

**Scientific Question**
    
   Are the the mean fastball release speeds between Jacob deGrom and Gerrit Cole the same?

**Null Hypothesis**
    
   The mean fastball release speeds between deGrom and Cole are the same.

**Alternative Hypothesis**
    
   The mean fastball release speeds between deGrom and Cole are not the same.
    
**Distribution under the null hypothesis**
    
   The distribution of the null hypothesis represents the difference between the mean of the two distributions. Comparing the release speeds for fastballs, it is
   the distribution of the difference of samples means where the assumption is that the mean of this distribution is zero:
   𝜇FF_speed deGrom - 𝜇FF_speed Cole = 0

**Significance level**
    
   I will select a standard significance level of 0.05. I will also use a Bonferonni correction of 4 to account for the fact that I will be comparing multiple means of fastball measurements between the pitchers. Therefore, my signficance for each individual test will be 𝛼=0.05/4 = 0.0125.

**p-value**

    Gerrit Cole mean release speed: 96.7
    Jacob deGrom mean release speed: 98.6
    Gerrit Cole sample size: 635
    Jacob deGrom sample size: 510
    t-stat: -28.6
    p-value: 4e-136

<img alt="" src="/img/mcghee.png" width='500'> 

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

### Slider

#### Total observations:
* Gerrit Cole: 294
* Jacob deGrom: 403

| Measurement       | p-value | 𝜇Cole     | 𝜇deGrom   | RTN |
|-------------------|---------|-----------|-----------|-----|
| release speed     | 2e-161  | 88.7      | **92.5**  | Y   |
| release spin rate | 0.1385  | **2580**  | 2565      | N   |
| lateral movement  | 7e-27   | **0.42**  | 0.31      | Y   |
| vertical movement | 4e-14   | 0.29      | **0.41**  | Y   |

___

	
## Acknowledgements
* Maria Popova, without whose disciplined habits and willingness to share her work, readers like myself would be deprived of an incredible resource of wisdom and erudition.
* Dan Rupp, data science instructor at Galvanize Austin, for his excellent suggestions regarding the selection of the feature space and interpretation of the model results and Dr. Juliana Duncan, lead data science instructor at Galvanize Austin, for her leading questions and conceptual help with statistical topics.

