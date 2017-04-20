import future as future

import matlab.engine
eng = matlab.engine.connect_matlab()
print(matlab.engine.find_matlab())

x = matlab.double([1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19])

print("Calling function")
y = eng.predictUsingClassificationBaggedEnsembleByResampling("S:\Files\MASTERS\database design\project\\test.mat", x)

print(y)
eng.quit()
