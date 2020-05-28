# Subreddit Recommender

Try it at: http://similar-subreddits.herokuapp.com/

Reddit is a website with communities called **subreddits**, where users may discuss topics they share interest in, such as cooking or art.

My subreddit recommender allows a user to select a subreddit and see which other subreddits are likely to pique their interest.

![alt text](https://github.com/nalimuradov/Subreddit_Recommender/blob/master/static/rdt_rcmnd.png "gaming subreddit recommendations")

Recommended subreddits are determined by tracking the liked posts of active users on Reddit, and creating maps of overlapping likes and their corresponding subreddits.

> For example, if many users who like posts in /r/cars also like posts in /r/gaming, their recommendation scores will be higher.

A higher **recommendation score** means there is a much higher overlap when compared to the average. On the other hand, a 0% score means that there is an average amount of overlap and therefore no correlation.

A *tf-idf* inspired statistic is used to drown out the extremely popular subreddits. Some subreddits such as **/r/Askreddit** are so popular that they are constantly recommended, but if we track their distribution, we can adjust their impact on the rankings accordingly.


