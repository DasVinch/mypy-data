from numpy import ndarray, DtypeType, ShapeType

def rand(*args: int) -> ndarray[float]: ...
def ranf(*args: int) -> ndarray[float]: ...
def random(size: ShapeType=None) -> float: ...
def randint(low: int, high: int=None, size: ShapeType=None, dtype: DtypeType=int) -> ndarray[int]: ...
