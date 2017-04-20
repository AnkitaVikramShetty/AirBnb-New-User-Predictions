function a = predictUsingClassificationBaggedEnsembleByResampling(ModelPath, x)
Model = load(ModelPath);
a = predict(Model.Mdl, x);
end