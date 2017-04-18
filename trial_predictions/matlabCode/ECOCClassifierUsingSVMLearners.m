%% Train Multiclass Model Using SVM Learners
% Train an error-correcting output codes (ECOC) multiclass model using
% support vector machine (SVM) binary learners.
%%
% Load Fisher's iris data set.
X = csvread('train_users_2_reduced_input.csv', 1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);
%%
% Train an ECOC multiclass model using the default options.
ECOC_Mdl = fitcecoc(X,Y);

save('ECOC_ClassificationUsingSvmLearnersModel.mat', 'ECOC_Mdl', '-mat', '-v7.3');
