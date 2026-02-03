### ------------ Folder name : models --------------------

- here is all the information about the 'models' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- in this folder we have the saved models from the training phase, that were tarined on the train data and were tested on the test data and are ready to validate the performance on the valid data.

- there are further 2 subfolders inside the folder : (trees) and (distance_based)


### Subfolder : trees

- it has all the saved tree based models inside that were trained and tested for the tree based data.

- the models are  : 
1. dtr.pkl : Decision tree regressor
2. rfr.pkl : Random forest regressor
3. abr.pkl : Adaboost regressor
4. gbr.pkl : Gradient boost regressor


### Subfolder : distance_based

- it has the distance based models, that were trained and tested on the distance based data

- the models are : 
1. lr.pkl : Linear Regression
2. svc.pkl : Support vector regressor
3. knn : KNeighbors regressor
