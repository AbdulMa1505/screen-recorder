import cv2
import tkinter as tk
import numpy as np
from PIL import ImageGrab

# Global variables to control recording and pausing
is_paused = False
is_recording = False  # To check if the recording has started

def ScreenRecorder():
    global is_paused, is_recording
    is_recording = True
    # Setting up the video writer with the correct codec and frame size
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 8.0, (1366, 768))  # Correct width and height

    while is_recording:
        if not is_paused:
            # Capturing the screen
            img = ImageGrab.grab()
            img_np = np.array(img)

            # Converting RGB to BGR for OpenCV compatibility
            frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Show the screen capture in a window
            cv2.imshow("Screen Recorder", frame)

            # Write the frame to the output file
            out.write(frame)

        # Exit when 'Esc' key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Releases the video writer object and close windows
    out.release()
    cv2.destroyAllWindows()

def pause_resume():
    global is_paused
    if is_paused:
        is_paused = False
        pause_button.config(text="Pause")  # Update button text to "Pause"
    else:
        is_paused = True
        pause_button.config(text="Resume")  # Update button text to "Resume"

def stop_recording():
    global is_recording
    is_recording = False
    cv2.destroyAllWindows()

# Setup the Tkinter GUI
window = tk.Tk()
window.title("Screen Recorder")

frame = tk.Frame(window)
frame.pack()

# Start Recording Button
start_button = tk.Button(frame, text="Start Recording", command=ScreenRecorder)
start_button.pack(side=tk.LEFT)

# Pause/Resume Button
pause_button = tk.Button(frame, text="Pause", command=pause_resume)
pause_button.pack(side=tk.LEFT)

# Stop Button to stop recording
stop_button = tk.Button(frame, text="Stop", command=stop_recording)
stop_button.pack(side=tk.LEFT)

window.mainloop()
