from pstats import Stats


class ProfilingData:
    __slots__ = ('funcName', 'stats', 'elapsedTime')
    def __init__(self, funcName: str, stats: Stats, elapsedTime: float):
        self.funcName = funcName
        self.stats = stats
        self.elapsedTime = elapsedTime
    
    def __str__(self):
        return f"Function {self.funcName} executed in {self.elapsedTime}"
        