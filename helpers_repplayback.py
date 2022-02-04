# -*- coding: utf-8 -*-
"""
Helper functions for repeated_playback
======================================
Author: Thejasvi Beleyur
Feb 2022
"""
import datetime as dt
import time 



def add_one_day(posix_time):
    '''
    '''
    time_point = dt.datetime.fromtimestamp(posix_time)
    one_day_later = time_point + dt.timedelta(days=1)
    onedaylater_posixtime = time.mktime(one_day_later.timetuple())
    return onedaylater_posixtime

def make_posix_time_from_HHMMSS(HHMMSS):
    '''
    Generates the POSIX time stamp for the input start and stop HHMMSS.
    '''
    
    
    full_starttime = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d')+'_'+HHMMSS
    start_datetime = dt.datetime.strptime(full_starttime, '%Y-%m-%d_%H:%M:%S')

    return time.mktime(start_datetime.timetuple())