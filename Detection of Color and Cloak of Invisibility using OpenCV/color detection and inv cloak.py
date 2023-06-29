import cv2
import numpy as np


# Function to detect the color and create a mask
def color_detection(frame, color_lower, color_upper):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv, color_lower, color_upper)

    return mask


# Main function
def main():
    # Define the color range for detection (here, we're detecting red color)
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])

    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    # Allow the camera to warm up
    cv2.waitKey(2)

    # Capture the background image
    for i in range(30):
        _, background = cap.read()

    while True:
        # Read the current frame from the video stream
        _, frame = cap.read()

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Detect the color in the frame
        mask = color_detection(frame, red_lower, red_upper)

        # Perform morphological operations to remove noise
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=1)

        # Invert the mask to create the invisibility effect
        inv = cv2.bitwise_not(mask)

        # Apply the mask to the frame
        result = cv2.bitwise_and(frame, frame, mask=inv)

        # Display the output
        cv2.imshow("(Detection of Color and the Cloak of Invisibility) ", result)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()