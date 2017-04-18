%% Train Bagged Ensemble of Classification Trees
%%
% Load the |ionosphere| data set.
X = csvread('train_users_2_reduced_input.csv',1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);
%%
% Train a bagged ensemble of 100 classification trees using all
% measurements.
Mdl = fitensemble(X,Y,'bag',100,'Tree','Type','classification');
%%
% |Mdl| is a |ClassificationBaggedEnsemble| model object.
%%
% |Mdl.Trained| is the property that stores a 100-by-1 cell vector
% of the trained classification trees (|CompactClassificationTree| model
% objects) that compose the ensemble.

save('ClassificationBaggedModel.mat', 'Mdl', '-mat', '-v7.3');
