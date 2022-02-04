# -*- coding: utf-8 -*-
"""
Repeated playback
=================
Module which repeatedly plays back a sound from a start time to a stop time. 

Currently the playback does not stop exactly at the stop time. The playback
continues to play until the recording is done after the stop time.

The module DOES NOT support repeated playbacks that go on for more than 24 hours. 
The duration between the start and stop times must be less than 24 hours.


Required inputs
---------------
1. Audio file path
2. Start time (HH:MM:SS)
3. Stop time (HH:MM:SS)



Author: Thejasvi Beleyur, Feb 2022
Written for the Brumm group's playback experiments

"""

#%%
import datetime as dt
import numpy as np
import soundfile as sf
import sounddevice as sd
import time 
import yaml 

from helpers_repplayback import make_posix_time_from_HHMMSS
from helpers_repplayback import add_one_day


# Load parameters
with open('parameters.txt', 'r') as file:
    parameters = yaml.safe_load(file)

start_hhmmss = parameters['start_HHMMSS']
stop_hhmmss = parameters['stop_HHMMSS']
file_name = parameters['playback_file']
playback_device = parameters['playback_device']
# 
start_posix_time = make_posix_time_from_HHMMSS(start_hhmmss)
stop_posix_time = make_posix_time_from_HHMMSS(stop_hhmmss)

# If the stop time apparently seems to be earlier than the start time. 
# One day is 'added' to the timestamp
if stop_posix_time<start_posix_time:
    stop_posix_time = add_one_day(stop_posix_time)

# load the playback file
audio, fs = sf.read(file_name)

if len(audio.shape)>1:
    if audio.shape[1]>1:
        nchannel = audio.shape[1]
else:
    nchannel = 1

# decide a blocksize by splitting the audio into X parts
num_parts = 20
audio_parts = np.array_split(audio, num_parts)
audio_parts = [np.ascontiguousarray(each, dtype=np.float32) for each in audio_parts]

# initiate the OutputStream
# the special value blocksize=0 allows the blocksize to vary across calls

if __name__ == '__main__':

    out_stream = sd.OutputStream(samplerate=fs, blocksize=0,
                                             channels=nchannel, device=playback_device)

    # wait for the start time 
    while time.time()<=start_posix_time:
        time.sleep(1)
        print('waiting for start time...')
    
    random_data = np.random.normal(0,0.01,441)
    timenow = dt.datetime.strftime(dt.datetime.now(),'%H-%M-%S')
    sf.write(f'succesful_runstart_{timenow}.wav', random_data, 44100)
    
    to_yymmddhhmmss = lambda X: dt.datetime.strftime(X, '%Y-%m-%d %H:%M:%S')
    now = to_yymmddhhmmss(dt.datetime.now())
    end_yymmdd_hhmmss = to_yymmddhhmmss(dt.datetime.fromtimestamp(stop_posix_time))
    
    print(f'\n starting playback at {now} \n scheduled end: {end_yymmdd_hhmmss}')
    out_stream.start()

    # Once the start time is here, keep playing until the last repeat that goes past
    # the stop time (playback may end before too)
    while np.logical_and(time.time()>=start_posix_time, time.time()<stop_posix_time):

        i = 0
        while i < len(audio_parts):
            out_stream.write(audio_parts[i])
            i += 1
    timenow = dt.datetime.strftime(dt.datetime.now(),'%H-%M-%S')
    sf.write(f'succesful_runend_{timenow}.wav', random_data, 44100)


    
