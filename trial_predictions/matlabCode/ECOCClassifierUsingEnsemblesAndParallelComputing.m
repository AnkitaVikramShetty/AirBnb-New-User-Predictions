% Train a one-versus-all ECOC classifier using a GentleBoost ensemble of
% decision trees with surrogate splits. Estimate the classification error
% using 10-fold cross-validation.
X = csvread('train_users_2_reduced_input.csv',1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);

[n,p] = size(X);
isLabels = unique(Y);
nLabels = numel(isLabels);
tabulate(categorical(Y));

% Create an ensemble template. You must specify at least three arguments: a
% method, a number of learners, and the type of learner. For this example,
% specify 'GentleBoost' for the method, 100 for the number of learners, and
% a decision tree template that uses surrogate splits since there are
% missing observations.
tTree = templateTree('surrogate','on');
tEnsemble = templateEnsemble('GentleBoost',100,tTree);

% tEnsemble is a template object. Most of its properties are empty, but the
% software fills them with their default values during training.

% Train a one-versus-all ECOC classifier using the ensembles of decision
% trees as binary learners. If you have a Parallel Computing Toolbox™
% license, then you can speed up the computation by specifying to use
% parallel computing. This sends each binary learner to a worker in the
% pool (the number of workers depends on your system configuration). Also,
% specify that the prior probabilities are 1/K, where K = 13, which is the
% number of distinct classes.

pool = parpool; % Invoke workers
options = statset('UseParallel',1);
Mdl = fitcecoc(X,Y,'Coding','onevsall','Learners',tEnsemble,...
                'Prior','uniform','Options',options);

% Cross-validate the ECOC classifier using 10-fold cross-validation.
CVMdl = crossval(Mdl,'Options',options);

