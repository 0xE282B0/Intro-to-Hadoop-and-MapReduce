Intro-to-Hadoop-and-MapReduce
=============================
This repository contains Hadoop MapReduce scripts which are written in python. The data that can be processed is from the Udacity course "Intro to Hadoop and MapReduce". You can find the dataset [here](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz). All scripts are using the forum_node.tsv file.

Index building
--------------
In lesson [4.7](https://www.udacity.com/course/viewer#!/c-ud617/l-713848763/e-711119083/m-705049030) an Inverted Index was needed to answer the Quiz. The index building mechanism was very simple. The text was split by a set of definied chars and the tokens were listed with the post id.
The script in the index directory improves this approach. Instead of splitting the text by a list of chars, the striping and tokenizing tasks are separated. Further the reducer can be used as combiner to save network traffic.

List of top contributors
------------------------
This script counts the number of forum contributions of a user and lists the top 10 users with the number of total contributions, questions, answers and comments.

List of most discussed Questions
--------------------------------
This script counts the number of answers and comments a Question has and lists  the top 10 questions by number of contributions. 

Compute mean time a question is discussed
-----------------------------------------
The mapper computes the difference between the time a question was added and the last time a user was active. The reducer computes the mean active time for all questions and finds the longest active time.