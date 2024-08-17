import pygame
import customtkinter as ctk
from tkinter import filedialog
import os

class MusicPlayer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("(Asylum) Music Player V1  ")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        pygame.init()
        pygame.mixer.init()

        self.track = ctk.StringVar()
        self.status = ctk.StringVar()

        self.create_widgets()

        self.playlist = []
        self.current_track = 0
        self.is_paused = False  # New variable to track pause state

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Track info
        track_frame = ctk.CTkFrame(main_frame)
        track_frame.pack(pady=10, fill="x")

        ctk.CTkLabel(track_frame, textvariable=self.track, font=("Helvetica", 14)).pack(side="left", padx=10)
        ctk.CTkLabel(track_frame, textvariable=self.status, font=("Helvetica", 12)).pack(side="right", padx=10)

        # Progress bar (placeholder, not functional in this example)
        self.progress = ctk.CTkProgressBar(main_frame)
        self.progress.pack(pady=10, fill="x")
        self.progress.set(0)

        # Control buttons
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Play", command=self.playsong, width=60).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Pause", command=self.pausesong, width=60).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Stop", command=self.stopsong, width=60).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Load", command=self.load, width=60).pack(side="left", padx=5)

        # Volume slider
        volume_frame = ctk.CTkFrame(main_frame)
        volume_frame.pack(pady=10, fill="x")

        ctk.CTkLabel(volume_frame, text="Volume", font=("Helvetica", 12)).pack(side="left", padx=10)
        self.volume_slider = ctk.CTkSlider(volume_frame, from_=0, to=1, number_of_steps=10, command=self.set_volume)
        self.volume_slider.pack(side="right", padx=10, fill="x", expand=True)
        self.volume_slider.set(0.5)

    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if filename:
            self.playlist.clear()
            self.playlist.append(filename)
            self.track.set(os.path.basename(filename))
            self.status.set("Ready")
            self.is_paused = False

    def playsong(self):
        if self.playlist:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
            self.status.set("Playing")

    def pausesong(self):
        if pygame.mixer.music.get_busy():
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.status.set("Playing")
                self.is_paused = False
            else:
                pygame.mixer.music.pause()
                self.status.set("Paused")
                self.is_paused = True

    def stopsong(self):
        pygame.mixer.music.stop()
        self.status.set("Stopped")
        self.is_paused = False

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()