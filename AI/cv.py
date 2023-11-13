import cv2


def load_video():
    # Open the default camera (usually the built-in webcam)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open the camera.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = camera.read()

        if not ret:
            print("Error: Could not read a frame from the camera.")
            break

        # Display the frame in a window
        cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
        cv2.imshow("Camera Feed", frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    camera.release()
    cv2.destroyAllWindows()



