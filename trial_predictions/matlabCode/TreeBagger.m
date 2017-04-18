%% Classifying Radar Returns for Ionosphere Data Using TreeBagger
% You can also use ensembles of decision trees for classification. For this
% example, use ionosphere data with 351 observations and 34 real-valued
% predictors. The response variable is categorical with two levels:
%
% * 'g' represents good radar returns.
% * 'b' represents bad radar returns.
%
% The goal is to predict good or bad returns using a set of 34 measurements. 
%%
% Fix the initial random seed, grow 50 trees, inspect how the ensemble
% error changes with accumulation of trees, and estimate feature
% importance. For classification, it is best to set the minimal leaf size
% to 1 and select the square root of the total number of features for each
% decision split at random. These settings are defaults for 
% |TreeBagger| used for classification.

X = csvread('train_users_2_reduced_input.csv',1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);

b = TreeBagger(50,X,Y,'OOBVarImp','On');

%%
% For classification ensembles, in addition to classification error
% (fraction of misclassified observations), you can also monitor the
% average classification margin. For each observation, the _margin_ is
% defined as the difference between the score for the true class and the
% maximal score for other classes predicted by this tree. The cumulative
% classification margin uses the scores averaged over all trees and the
% mean cumulative classification margin is the cumulative margin averaged
% over all observations. The |oobMeanMargin| method with the |'mode'|
% argument set to |'cumulative'| (default) shows how the mean cumulative
% margin changes as the ensemble grows: every new element in the returned
% array represents the cumulative margin obtained by including a new tree
% in the ensemble. If training is successful, you would expect to see a
% gradual increase in the mean classification margin.
%%
% The method trains ensembles with few trees on observations that are in
% bag for all trees. For such observations, it is impossible to compute the
% true out-of-bag prediction, and |TreeBagger| returns the most probable
% class for classification and the sample mean for regression.

save('TreeBaggerModel.mat', 'b', '-mat', '-v7.3');
