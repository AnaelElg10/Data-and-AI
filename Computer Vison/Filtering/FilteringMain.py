import cv2 as cv

def main():
    # Load the video
    video = cv.VideoCapture('TrafficJam.mp4')
    
    # Check if video opened successfully
    if not video.isOpened():
        print("Error: Could not open video.")
        return

    # Create background subtractor
    subtractor = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=80)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Apply the background subtractor to get the mask
        mask = subtractor.apply(frame)
        
        # Display the mask
        cv.imshow('Mask', mask)

        # Exit on 'q' key press
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and close all OpenCV windows
    video.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()