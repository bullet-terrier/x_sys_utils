"""
ticktock
"""

import time;
import sched

scale = 0.00001

def ticktock(msg=None,caller=None,last_time = None,init_time = None,scale = None):
    """
    test the relative scheduler.
    """
    tm = time.time();
    if scale is None: scale = 0.5
    if init_time is None: init_time = time.time();
    if last_time is None: last_time = tm;
    if msg is None: msg = "Tick";
    print("%s \t\tdelay: %s\ttotal: %s "%(msg,tm-last_time,tm-init_time));
    if msg is "Tick": msg = "Tock";
    else: msg = "Tick";
    if caller.empty(): caller.enter(scale,None,ticktock,(msg,caller,tm,init_time,scale));
    if caller.empty(): raise Exception("Looks like the caller wasn't ready!");
    return;
    
if __name__=="__main__":
    zed = sched.scheduler();
    zed.enter(scale,None,ticktock,("FIRST TICK!",zed,None,None,scale));
    print("Prepped and ready to roll");
    zed.run();