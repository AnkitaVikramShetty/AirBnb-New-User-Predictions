%% Reduce Size of Bag of Trees
% Create a compact bag of trees for efficiently making
% predictions on new data.
%%
% Load the |ionosphere| data set.
X = csvread('train_users_2_reduced_input.csv', 1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);
%%
% Train a bag of 100 classification trees using all measurements and the
% |AdaBoostM1| method.
Mdl = TreeBagger(100,X,Y,'Method','classification')
%%
% |Mdl| is a |TreeBagger| model object that contains the
% training data, among other things.
%%
% Create a compact version of |Mdl|.
%%CMdl = compact(Mdl)

% |CMdl| is a |CompactTreeBagger| model object.  |CMdl|
% is almost the same as |Mdl|.  One exception is that it does not store the
% training data.
%%
% Compare the amounts of space consumed by |Mdl| and |CMdl|.
mdlInfo = whos('Mdl');
cMdlInfo = whos('CMdl');
[mdlInfo.bytes cMdlInfo.bytes]
%%
% |Mdl| consumes more space than |CMdl|.
%%
% |CMdl.Trees| stores the trained classification trees
% (|CompactClassificationTree| model objects) that compose |Mdl|.
%%
% Display a graph of the first tree in the compact model.
view(CMdl.Trees{1},'Mode','graph');
%%
% By default, |TreeBagger| grows deep trees.
%%
% Predict the label of the mean of |X| using the compact ensemble.
predMeanX = predict(CMdl,mean(X))