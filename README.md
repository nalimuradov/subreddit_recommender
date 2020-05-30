# Subreddit Recommender

Try it at: http://similar-subreddits.herokuapp.com/

Reddit is a site of communities called **subreddits** where users may discuss topics they share interest in, such as cooking or art.

My *Subreddit Recommender* allows a user to select a subreddit and find other communities that are likely to pique their interest. 

Recommended subreddits are determined by tracking the **liked posts of active users** on Reddit, and creating maps of overlapping likes and their corresponding subreddits.

![alt text](https://github.com/nalimuradov/Subreddit_Recommender/blob/master/static/rdt_rcmnd.png "gardening subreddit recommendations")

> Above are some recommended subreddits for /r/gardening. It's interesting to note that many users who like /r/gardening also like /r/cats.

The **recommendation score** on the left signifies the amount of user overlap. The greater the value, the greater the overlap in activity.

> If many users who like posts in /r/cars also like posts in /r/gaming, their recommendation scores will be higher.

A *tf-idf* inspired statistic is used to drown out the extremely popular subreddits (such as **/r/AskReddit**) which were often recommended despite not having any significant correlation to the evaluated subreddit.



