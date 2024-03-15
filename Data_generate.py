import cv2
import numpy as np
import time

# Initialize the webcam
cap = cv2.VideoCapture(1)  # Change the argument to 1, 2, etc., if you have multiple cameras

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Set up variables for capturing images every 5 seconds
capture_interval = 5  # seconds
last_capture_time = time.time()

# Minimum contour area for considering motion
min_contour_area = 250

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Threshold the foreground mask
    _, thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)

    # Apply morphological operations
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if motion is detected
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            motion_detected = True
            break

    # If motion is detected, capture images at 5-second intervals
    if motion_detected and time.time() - last_capture_time >= capture_interval:
        # Save the frame as an image
        cv2.imwrite(f"motion_detected_image_{int(time.time())}.jpg", frame)
        last_capture_time = time.time()

    # Display the resulting frame
    cv2.imshow('Motion Detection', frame)
    cv2.imshow('Fgmask' , fgmask)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
