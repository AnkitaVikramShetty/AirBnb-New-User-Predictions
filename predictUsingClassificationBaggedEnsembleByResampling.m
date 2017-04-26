function a = predictUsingClassificationBaggedEnsembleByResampling(ModelPath,xPath)
Model = load(ModelPath);
x = csvread(xPath, 1, 1);
a = predict(Model.Mdl, x);
end