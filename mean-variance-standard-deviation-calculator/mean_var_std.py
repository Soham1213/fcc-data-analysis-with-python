from pprint import pprint
import numpy as np

def calculate(list):
  if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
  else:
    m = np.array(list).reshape([3, 3])
    calculations = {
        "mean": [m.mean(0).tolist(),m.mean(1).tolist(),m.mean()],
        "variance": [m.var(0).tolist(), m.var(1).tolist(), m.var()],
        "standard deviation": [m.std(0).tolist(), m.std(1).tolist(), m.std()],
        "max": [m.max(0).tolist(), m.max(1).tolist(), m.max()],
        "min": [m.min(0).tolist(), m.min(1).tolist(), m.min()],
        "sum": [m.sum(0).tolist(), m.sum(1).tolist(), m.sum()],
    }
    return calculations
pprint(calculate([i for i in range(0, 9)]))
