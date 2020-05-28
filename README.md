# Subreddit Recommender

Try it at: http://similar-subreddits.herokuapp.com/

Reddit is a website with communities called **subreddits**, where users may discuss topics they share interest in, such as cooking or art.

My application allows a user to select a subreddit and see which other subreddits are likely to pique your interest.

![alt text](https://github.com/nalimuradov/Video-View-Predictor/blob/master/images/img5.png "Sample data for a video")

Recomomended subreddits are determined by tracking the liked posts of active users on Reddit, and creating maps of overlapping subreddits.

> For example, if many users who like posts in /r/cars also like posts in /r/gaming, their recommendation scores will be higher.

The recommendation scores on the left signify. A 0% recommendation score implies there is no correlation, and the higher the value is, the stronger the similarities.



A *tf-idf* inspired statistic is used to drown out the extremely popular subreddits. Some subreddits such as **/r/Askreddit** are so popular that they are constantly recommended, but if we track how the subreddits are distributed, we can adjust their impact on the rankings accordingly.

