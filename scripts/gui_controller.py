# Script: .\scripts\gui_controller.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from persistence import save_settings
from audio_routing import play_video

# Global Variables
VIDEO_FOLDER = "/home/user/Videos/Karaoke"
MIC_VOLUME = 50
SECOND_LIFE_VOLUME = 50

class KaraokeApp(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Karaoke Controller")
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)

        # Video folder selector
        video_folder_label = Gtk.Label(label="Video Folder")
        grid.attach(video_folder_label, 0, 0, 1, 1)

        video_folder_button = Gtk.Button(label="Select Folder")
        video_folder_button.connect("clicked", self.on_video_folder_clicked)
        grid.attach(video_folder_button, 1, 0, 1, 1)

        # Mic volume control
        mic_volume_label = Gtk.Label(label="Microphone Volume")
        grid.attach(mic_volume_label, 0, 1, 1, 1)

        self.mic_volume = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        self.mic_volume.set_value(MIC_VOLUME)
        grid.attach(self.mic_volume, 1, 1, 1, 1)

        # Second Life volume control
        second_life_volume_label = Gtk.Label(label="Second Life Volume")
        grid.attach(second_life_volume_label, 0, 2, 1, 1)

        self.second_life_volume = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        self.second_life_volume.set_value(SECOND_LIFE_VOLUME)
        grid.attach(self.second_life_volume, 1, 2, 1, 1)

        # Video player controls (Play)
        play_button = Gtk.Button(label="Play Video")
        play_button.connect("clicked", self.on_play_video_clicked)
        grid.attach(play_button, 0, 3, 2, 1)

        self.show_all()

    def on_video_folder_clicked(self, widget):
        """Select video folder."""
        dialog = Gtk.FileChooserDialog(
            title="Choose Video Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                           Gtk.STOCK_OPEN, Gtk.ResponseType.OK)

        if dialog.run() == Gtk.ResponseType.OK:
            global VIDEO_FOLDER
            VIDEO_FOLDER = dialog.get_filename()
            save_settings({'video_folder': VIDEO_FOLDER})
        dialog.destroy()

    def on_play_video_clicked(self, widget):
        """Play video from the selected folder."""
        # Placeholder for actual video file selection logic
        video_path = f"{VIDEO_FOLDER}/example.mp4"
        play_video(video_path)

def start_gui():
    """Start the GTK GUI."""
    win = KaraokeApp()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
