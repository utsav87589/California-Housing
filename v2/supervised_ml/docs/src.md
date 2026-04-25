### ------------ Folder name : src --------------------

- In the src folder, we have the block of codes (oython files) in form of functions, that were called again and again inside the notebooks mutiple times. Now, the idea behind is that while doing the Data Science on any dataset, often times it become messy and unorganised in a way that mananaging everything feels next to impossible.

- Another drawback is that, if we mistakenly performs an action i.e. dropping a feature that was not supposed or scaling the features for the tree based data, then we have to re run all the blocks in the notebboks, which consume extra time and effort.

- So, by having these src files, we bridge the gap between the flowstate and the different entry/exit points of the project.

- Further the 'src' folder has 3 subfolders : 
1. basic
2. predictions
3. processing

1. basic : it has the functions related to the operations on the raw data like making the earliest possible split, checking the shape of the data or missing values inside the data.

2. processing : all the featured engineering related tasks and logics are inside this file, whether it be transformations or the label encoding on certain features.

3. predictions : train/test split, training of the models, predictions or the plotting, all the post featured engineering/EDA related tasks are inside this folder.

- So, that way when we look at the folder and their names, we get a good idea about the possible contents inside the folder as well, what they might be responsible for. Now, let's say I wanna check the shape of the Valid, train and test data, instead of writing the same line many times, I can call a function and use it, that way notebooks looks not only clean but managed and avoids the confusion.
