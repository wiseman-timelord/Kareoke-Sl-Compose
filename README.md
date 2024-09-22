# Kareoke-Sl-Compose
Status : Alpha, not working

### Concise Description:
It enables, automatic audience mute when video played and intelligent mixing of, video and mic, streams, its for kareoke over voip. The `Kareoke-Sl-Compose` project provides an interactive karaoke experience on **Second Life** using **WSL2 on Windows**. It handles audio routing, video playback, and user settings through a graphical interface and command-line tools.

### Features:
- **Audio Routing**: Manages sound input/output via PulseAudio, including virtual sinks and dynamic muting for Second Life.
- **Video Playback**: Plays karaoke videos using VLC, with automatic audio management.
- **Graphical User Interface (GUI)**: Uses GTK to allow users to select folders, adjust volumes, and control playback.
- **Setup and Installer**: Automatically installs required Python libraries and updates pip for WSL.
- **Distro Management**: Allows users to select and switch WSL Linux distributions easily.
- **Persistent Settings**: Saves and loads user configurations, such as selected distro and audio settings.

### Remaining Work:
Some features and configurations require completion, particularly in terms of user interaction and distro management. Below is a list of remaining tasks:
- **Video File Selection**: Implement file selection for karaoke videos in the GUI.
- **Error Handling**: Improve error detection and handling in the installer and audio routing modules.
- **Distro Switching Validation**: Ensure robust handling when switching between WSL distros.
- **Pre-Launch Configuration**: Expand the configuration options available before launching the karaoke session.
- **Testing and Debugging**: Perform comprehensive testing across different WSL distros and Windows configurations. 
