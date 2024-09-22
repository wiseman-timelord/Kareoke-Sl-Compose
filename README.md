# Kareoke-Sl-Compose
Status : Alpha, not working

### Concise Description:
Its for kareoke over voip; the `Kareoke-Sl-Compose` project provides an interactive karaoke experience on **Second Life** using **WSL2 on Windows**. It handles audio routing, video playback, and user settings through a graphical interface and command-line tools It will enables... 
1. Automatic audience mute when video playing.
2. Intelligent mixing of video + mic, streams.
3. Processing of video/mic levels, to being automatically optimal, with the users voice just a little louder than the music level, which should be automatic and re-assessed upon ongoing basis, while somehow smoothed out. over long period for music and shorter period for the mic input, for the average.

### Features:
- **Audio Routing**: Manages sound input/output via PulseAudio, including virtual sinks and dynamic muting for Second Life.
- **Video Playback**: Plays karaoke videos using VLC, with automatic audio management.
- **Graphical User Interface (GUI)**: Uses GTK to allow users to select folders, adjust volumes, and control playback.
- **Setup and Installer**: Automatically installs required Python libraries and updates pip for WSL.
- **Distro Management**: Allows users to select and switch WSL Linux distributions easily.
- **Persistent Settings**: Saves and loads user configurations, such as selected distro and audio settings.

### PREVIEW:
- End of Session 1...
```
========================================================================================================================================================
    Kareoke-Sl-Compose
========================================================================================================================================================

    1. Run Kareoke-Sl-Compose.

    2. Change Wsl Distro Used.
     (Current: **distro-name**)

    3. Setup and Installer.

========================================================================================================================================================
Selection; Menu Options = 1-3, Exit Program = X:

```


## DEVELOPMENT:
Some features and configurations require completion, particularly in terms of user interaction and distro management. Below is a list of remaining tasks:
- **Video File Selection**: Implement file selection for karaoke videos in the GUI.
- **Error Handling**: Improve error detection and handling in the installer and audio routing modules.
- **Distro Switching Validation**: Ensure robust handling when switching between WSL distros.
- **Pre-Launch Configuration**: Expand the configuration options available before launching the karaoke session.
- **Testing and Debugging**: Perform comprehensive testing across different WSL distros and Windows configurations. 

