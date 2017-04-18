import future as future
import matlab.engine

# eng = matlab.engine.start_matlab()
# future =  matlab.engine.start_matlab(async=True)

# eng = future.result()
eng = matlab.engine.connect_matlab()
print(eng.sqrt(4.0))
eng.quit()