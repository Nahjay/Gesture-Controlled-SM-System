# File that creates gesture recognition logic using OpenCV
import cv2


def test_camera(device_path):
    # Open the webcam using the provided device path
    cap = cv2.VideoCapture(device_path)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow("Webcam Test", frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Specify the device path based on your setup
    device_path = "/dev/video5"  # Change this to '/dev/video6' if needed

    # Call the test_camera function
    test_camera(device_path)
