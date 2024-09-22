# Script: .\scripts\audio_routing.py

import pulsectl
import vlc

# Global Variables
SECOND_LIFE_SINK = "SecondLifeSink"
VIRTUAL_SINK = "KaraokeSink"
VIDEO_PLAYER = vlc.MediaPlayer()  # VLC player for video control
VIDEO_PLAYING = False

def initialize_audio_routing():
    """Initialize PulseAudio routing and monitor video status."""
    create_virtual_sink()
    monitor_video_status()

def create_virtual_sink():
    """Create a virtual sink in PulseAudio."""
    pulse = pulsectl.Pulse('karaoke-sink')
    pulse.module_load('module-null-sink', args=f"sink_name={VIRTUAL_SINK}")

def mute_second_life():
    """Mute Second Life output."""
    pulse = pulsectl.Pulse('karaoke-sink')
    for sink in pulse.sink_list():
        if sink.name == SECOND_LIFE_SINK:
            pulse.sink_mute(sink.index, mute=True)

def unmute_second_life():
    """Unmute Second Life output."""
    pulse = pulsectl.Pulse('karaoke-sink')
    for sink in pulse.sink_list():
        if sink.name == SECOND_LIFE_SINK:
            pulse.sink_mute(sink.index, mute=False)

def play_video(video_path):
    """Play karaoke video using VLC."""
    VIDEO_PLAYER.set_media(vlc.Media(video_path))
    VIDEO_PLAYER.play()

def monitor_video_status():
    """Continuously monitor if the video is playing and mute/unmute Second Life."""
    global VIDEO_PLAYING
    while True:
        if VIDEO_PLAYER.is_playing():
            if not VIDEO_PLAYING:
                mute_second_life()
                VIDEO_PLAYING = True
        else:
            if VIDEO_PLAYING:
                unmute_second_life()
                VIDEO_PLAYING = False
