# Script: .\karaoke_sl_compose.py

from scripts import gui_controller, audio_routing, persistence

# Global Variables
VIDEO_FOLDER = "/home/user/Videos/Karaoke"
MIC_VOLUME = 50
SECOND_LIFE_VOLUME = 50
SETTINGS_FILE = "data/persistence.yaml"

def main():
    # Load persisted settings
    settings = persistence.load_settings()
    global VIDEO_FOLDER, MIC_VOLUME, SECOND_LIFE_VOLUME
    VIDEO_FOLDER = settings.get('video_folder', VIDEO_FOLDER)
    MIC_VOLUME = settings.get('mic_volume', MIC_VOLUME)
    SECOND_LIFE_VOLUME = settings.get('second_life_volume', SECOND_LIFE_VOLUME)
    
    # Initialize GUI
    gui_controller.start_gui()
    
    # Initialize Audio Routing
    audio_routing.initialize_audio_routing()

if __name__ == "__main__":
    main()
