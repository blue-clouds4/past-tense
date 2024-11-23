import os
import subprocess
import threading
import tkinter as tk
import pygame

# Paths
CORE_SCRIPT_PATH = r"D:\past tense\core.py"
AUDIO_PATH = r"D:\past tense\audio\main_menu.wav"

# Initialize pygame mixer
pygame.mixer.init()

# Global flag to control music playback
music_playing = False

def play_audio():
    """Play background audio in a loop."""
    global music_playing
    if os.path.exists(AUDIO_PATH):  # Ensure file exists
        pygame.mixer.music.load(AUDIO_PATH)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        music_playing = True
    else:
        print(f"Error: Audio file not found at {AUDIO_PATH}")

def stop_audio():
    """Stop the background audio."""
    global music_playing
    if music_playing:
        pygame.mixer.music.stop()
        music_playing = False

class PastTenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Past Tense")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(fill="both", expand=True)

        # Upper section for ASCII art or images
        self.upper_label = tk.Label(self.main_frame, text="", font=("Consolas", 12), fg="white", bg="black",
                                    justify="left")
        self.upper_label.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Lower section for input/output
        self.output_box = tk.Text(self.main_frame, height=10, bg="black", fg="white", font=("Consolas", 12),
                                  state="disabled")
        self.output_box.pack(side="top", fill="both", expand=False, padx=10, pady=5)

        self.input_box = tk.Entry(self.main_frame, bg="black", fg="white", font=("Consolas", 12))
        self.input_box.pack(side="bottom", fill="x", padx=10, pady=5)
        self.input_box.bind("<Return>", self.process_command)

        # Initial game state
        self.show_ascii_art()
        self.display_intro()

    def show_ascii_art(self):
        """Display ASCII art in the upper label."""
        ascii_art = (
            "██████╗  █████╗ ███████╗████████╗    ████████╗███████╗███╗   ██╗███████╗███████╗\n"
            "██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    ╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔════╝\n"
            "██████╔╝███████║███████╗   ██║          ██║   █████╗  ██╔██╗ ██║███████╗█████╗  \n"
            "██╔═══╝ ██╔══██║╚════██║   ██║          ██║   ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  \n"
            "██║     ██║  ██║███████║   ██║          ██║   ███████╗██║ ╚████║███████║███████╗\n"
            "╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝"
        )
        self.upper_label.config(text=ascii_art)

    def display_intro(self):
        """Display the introductory game instructions."""
        intro_text = (
            "This is a CLI-based game, whether you like it or not. Sure, there will be a GUI later in the game, "
            "but now face the pain.\n\n"
            "Input 'play' to enter the game.\n"
            "Enter 'credits' to see the credits.\n"
            "Enter 'exit' to quit the game."
        )
        self.write_output(intro_text)

    def process_command(self, event=None):
        """Process the user's command."""
        command = self.input_box.get().strip().lower()
        self.input_box.delete(0, tk.END)
        self.write_output(f"> {command}\n")

        # Add command handling with a try-except block
        try:
            if command == "play":
                self.start_game()
            elif command == "credits":
                self.show_credits()
            elif command == "exit":
                self.quit_game()
            else:
                self.write_output("Invalid command. Please type 'play', 'credits', or 'exit'.\n")
        except Exception as e:
            self.write_output(f"Error processing command: {e}")

    def write_output(self, text):
        """Write text to the output box."""
        self.output_box.configure(state="normal")
        try:
            self.output_box.insert("end", text + "\n")
        except Exception as e:
            print(f"Error while writing output: {e}")
        finally:
            self.output_box.see("end")
            self.output_box.configure(state="disabled")

    def show_credits(self):
        """Show credits for the game."""
        credits = (
            "Credits:\n"
            "Developed by: vaishnavi,lalshmi, harsha\n"
            "Music by: harsha\n"
            "Graphics by: lakshmi\n"
        )
        self.write_output(credits)

    def start_game(self):
        """Start the main game by running core.py."""
        self.write_output("Starting the game...")

        # Stop music before starting the game
        stop_audio()


        def run_core():
            if os.path.exists(CORE_SCRIPT_PATH):
                try:
                    result = subprocess.run(["python",CORE_SCRIPT_PATH], check=True, capture_output=True,
                                            text=True)
                    self.write_output("Game finished, returning to the menu...")
                except subprocess.CalledProcessError as e:
                    self.write_output(f"Error while running core.py: {e}")
                    self.write_output(f"Error Output: {e.stderr}")
            else:
                self.write_output("Error: core.py not found.")

            # Restart the audio after game is finished
            play_audio()

        # Run core.py in a separate thread to avoid freezing the UI
        threading.Thread(target=run_core, daemon=True).start()

    def quit_game(self):
        """Exit the application."""
        self.write_output("Exiting the game. Goodbye!")
        stop_audio()  # Stop music before quitting
        self.root.after(1000, self.root.destroy)  # Close the app after a short delay


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = PastTenseApp(root)
    root.mainloop()
