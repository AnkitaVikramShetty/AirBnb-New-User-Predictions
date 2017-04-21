X = csvread('train_users_2_reduced_input.csv',1, 0);
Y = csvread('train_users_2_reduced_output.csv',1, 0);

[n,p] = size(X)
isLabels = unique(Y);
nLabels = numel(isLabels)
tabulate(categorical(Y))

tTree = templateTree('MaxNumSplits', 5, 'surrogate','on');
tEnsemble = templateEnsemble('Bag',100, tTree);

pool = parpool(16); % Invoke workers
options = statset('UseParallel',1);
Mdl = fitcecoc(X,Y,'Coding','onevsall','Learners',tEnsemble,...
                'Prior','uniform','Options',options);

save('MulticlassClassificationBagged.mat', 'Mdl', '-mat', '-v7.3');

%CVMdl = crossval(Mdl,'Options',options);

