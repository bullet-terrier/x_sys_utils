#!/bin/python3
"""
"log_msg.py"

/etc/linfo/log_msg.py

positional args: 
    1: file to read
    2: lines to display
    3: display time to completion

This third option isn't actually using the value passed, just 
checking for its existence to simplify use.

the first argument is the only argument that is required.

Passing no arguments will generate this message, then show
output from this file. Give it a shot to show only the N
most recent events in a log that works by appending data to 
file.
"""

import sys;
import time;
import os;


# I'll use this for some benchmarking to see if there is a better
# way to handle this algorithm.

def open_file(file_path,lines_2_read=5):
    """
    Generating a process to read the lines in various logs with arguments
    passed from a shell.
    """
    pass
    # I'm going to have to get creative to keep this from eating up memory
    # I'll just try to stream it concisely.
    lines =[];
    with open(file_path,'r') as data:
        zed = data.readline();
        while zed not in (None,""):
            if len(lines)<=lines_2_read: lines.append(zed)
            else:
                # pushing in a FIFO aproach
                t_lines = lines[1:]
                t_lines.append(zed)
                lines = t_lines;
            zed = data.readline(); # this is important.
    for a in lines:
        print(a)
    return;

            
if __name__=="__main__":
    it_ = time.time()
    # i'm just initializing these into something helpful.
    line_count = 5;
    line_src__ = './log_msg.py';
    flag_time = False;
    if len(sys.argv)>3: flag_time = True;
    if len(sys.argv)>2:
        try:
            line_count = int(sys.argv[2])
        except Exception:
            line_count = 5;
            print('that wasn\'t a valid number, reverting to default')
    if len(sys.argv)>1: 
        if os.path.isfile(sys.argv[1]):
            line_src__ = sys.argv[1];
        else:
            print('That doesn\'t appear to be a regular file...');        
    if len(sys.argv) ==1 : help(__name__);
    open_file(line_src__,line_count);
    et_ = time.time();
    if flag_time: print("Seconds to completion: %s."%(et_-it_))
  
