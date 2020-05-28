# Subreddit Recommender

Try it at: http://similar-subreddits.herokuapp.com/

**NOTE:** Case-sensitive, 

Reddit is a website with communities called **subreddits**, where users may discuss topics they share interest in, such as cooking or art.

While , Reddit doesn't provide a feature to find new subreddits based on the ones you already like.

The recommendation scores on the right signify. 0% recommendation score implies there is no correlation, and the subreddits are

My application allows a user to 
Recomomended subreddits are determined by tracking the liked posts of active users on Reddit. 


A *tf-idf* inspired statistic is used to drown out the extremely popular subreddits. Some subreddits such as /r/Askreddit are so popular that they are recommended, but now we track how often the recommended subreddits are distributed among other subreddits. If they are distributed evenly, they are given less weight.

>tf-idf stands for **term frequency - inverse document frequency**, and is used in NLP to give less weight to words that appear frequently everywhere (such as 'and')
