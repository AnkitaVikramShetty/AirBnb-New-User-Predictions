import future as future
import matlab.engine

def start_matlab():
    eng = matlab.engine.connect_matlab()
    # print(matlab.engine.find_matlab())

    return eng

def make_predictions(eng, x):
    print("Calling function")
    y = eng.predictUsingClassificationBaggedEnsembleByResampling("S:\Files\MASTERS\database design\project\\test.mat",x);

    return y

def stop_matlab(eng):
    eng.quit()

def user_prediction():
    eng = start_matlab()

    x = matlab.double([1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19])
    y = make_predictions(eng, x)
    print(y)

    stop_matlab(eng)