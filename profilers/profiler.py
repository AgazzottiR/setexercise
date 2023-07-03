import cProfile
import pstats
from timeit import default_timer as timer
from profilers.profilingData import ProfilingData
import sys 

def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None

def profile(func: callable) -> callable: 
    def wrapper(*args, **kwargs): 
        if len(args) > 0 and hasattr(args[0], 'profile') and args[0].profile == True:
            if debugger_is_active():
                print("[Profiler] You are running the profiler with the debugger active.")
                
            print("[Profiler] Start Profiling...")
            prof = cProfile.Profile()
            prof.enable()
            st = timer()
            ret = func(*args,**kwargs)
            elapsedTime = timer() - st
            prof.disable()
            print(f"[Profiler] Time Spent {elapsedTime}")
            stats = pstats.Stats(prof).sort_stats('cumtime')
            if hasattr(args[0], 'profilingData'):
                pData = ProfilingData(str(func.__name__), stats, elapsedTime)
                args[0].profilingData[str(func.__name__)] = pData
            print("[Profiler] End Profiling")
            return ret
        else:
            return func(*args,**kwargs)
    return wrapper
    