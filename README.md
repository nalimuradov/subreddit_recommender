# Subreddit Recommender

Try it at: http://similar-subreddits.herokuapp.com/

**NOTE:** Case-sensitive, 

Reddit is a website with communities called **subreddits**, where users may discuss topics they share interest in, such as cooking or art. While , Reddit doesn't provide a feature to find new subreddits based on the ones you already like.

My application allows a user to 
Recomomended subreddits are determined .
A tf-idf inspired filter is used to drown out the extremely popular subreddits. Some subreddits such as /r/Askreddit are so popular that they are recommended, but now we track how often the recommended subreddits are distributed among other subreddits. If they are distributed evenly, they are given less weight.


