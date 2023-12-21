""" Create a python script that will detect 5 fingers and make an API call to the server """
import os
import sys

# Get the absolute path of the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root path to the system path
sys.path.append(project_root)


import cv2
import numpy as np
import requests
import time
import mediapipe as mp
from led import LED


def recognize_fingers():
    # Initialize the camera
    cap = cv2.VideoCapture("/dev/video0")  # Adjust the device path as needed

    # Initialize the LED
    strip = LED()

    # Initialize mediapipe
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        else:
            # Convert the frame to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Flip the frame horizontally for a more natural appearance
            image = cv2.flip(image, 1)

            # Set the image data
            image.flags.writeable = False

            # Make a prediction
            results = hands.process(image)

            # Set the image data back to writable
            image.flags.writeable = True

            # Convert the frame back to BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw the hand annotations on the frame
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(
                            color=(121, 22, 76), thickness=2, circle_radius=4
                        ),
                        mp_drawing.DrawingSpec(
                            color=(250, 44, 250), thickness=2, circle_radius=2
                        ),
                    )

                    # Get the landmark coordinates
                    landmark_list = []
                    for i in range(21):
                        landmark = hand_landmarks.landmark[i]
                        landmark_x = min(
                            int(landmark.x * image.shape[1]), image.shape[1] - 1
                        )
                        landmark_y = min(
                            int(landmark.y * image.shape[0]), image.shape[0] - 1
                        )
                        landmark_list.append((landmark_x, landmark_y))

                    # Get the thumb coordinates
                    thumb_tip_x, thumb_tip_y = landmark_list[4]
                    thumb_mcp_x, thumb_mcp_y = landmark_list[2]

                    # Get the index finger coordinates
                    index_tip_x, index_tip_y = landmark_list[8]
                    index_mcp_x, index_mcp_y = landmark_list[6]

                    # Get the middle finger coordinates
                    middle_tip_x, middle_tip_y = landmark_list[12]
                    middle_mcp_x, middle_mcp_y = landmark_list[10]

                    # Get the ring finger coordinates
                    ring_tip_x, ring_tip_y = landmark_list[16]
                    ring_mcp_x, ring_mcp_y = landmark_list[14]

                    # Get the pinky finger coordinates
                    pinky_tip_x, pinky_tip_y = landmark_list[20]
                    pinky_mcp_x, pinky_mcp_y = landmark_list[18]

                    # Calculate the distance between the thumb and index finger
                    thumb_index_distance = np.sqrt(
                        (thumb_tip_x - index_tip_x) ** 2
                        + (thumb_tip_y - index_tip_y) ** 2
                    )

                    # Calculate the distance between the index and middle finger
                    index_middle_distance = np.sqrt(
                        (index_tip_x - middle_tip_x) ** 2
                        + (index_tip_y - middle_tip_y) ** 2
                    )

                    # Calculate the distance between the middle and ring finger
                    middle_ring_distance = np.sqrt(
                        (middle_tip_x - ring_tip_x) ** 2
                        + (middle_tip_y - ring_tip_y) ** 2
                    )

                    # Calculate the distance between the ring and pinky finger
                    ring_pinky_distance = np.sqrt(
                        (ring_tip_x - pinky_tip_x) ** 2
                        + (ring_tip_y - pinky_tip_y) ** 2
                    )

                    # Calculate the distance between the thumb and middle finger
                    thumb_middle_distance = np.sqrt(
                        (thumb_tip_x - middle_tip_x) ** 2
                        + (thumb_tip_y - middle_tip_y) ** 2
                    )

                    # Calculate the distance between the thumb and ring finger
                    thumb_ring_distance = np.sqrt(
                        (thumb_tip_x - ring_tip_x) ** 2
                        + (thumb_tip_y - ring_tip_y) ** 2
                    )

                    # Calculate the distance between the thumb and pinky finger
                    thumb_pinky_distance = np.sqrt(
                        (thumb_tip_x - pinky_tip_x) ** 2
                        + (thumb_tip_y - pinky_tip_y) ** 2
                    )

                    # Draw circles around every finger
                    cv2.circle(image, (thumb_tip_x, thumb_tip_y), 5, (0, 255, 0), -1)
                    cv2.circle(image, (index_tip_x, index_tip_y), 5, (0, 255, 0), -1)
                    cv2.circle(image, (middle_tip_x, middle_tip_y), 5, (0, 255, 0), -1)
                    cv2.circle(image, (ring_tip_x, ring_tip_y), 5, (0, 255, 0), -1)
                    cv2.circle(image, (pinky_tip_x, pinky_tip_y), 5, (0, 255, 0), -1)

                    # Establish three different gestures to be recognized

                    # Open hand gesture
                    if thumb_pinky_distance > 50 and thumb_ring_distance > 50:
                        print("Open hand gesture")
                        # strip.set_color(0, 255, 0)

                    # Fist gesture
                    elif (
                        thumb_index_distance < 50
                        and index_middle_distance < 50
                        and thumb_tip_y > index_mcp_y
                    ):
                        print("Fist gesture")
                        # strip.set_color(255, 0, 0)

                    # Peace gesture
                    elif (
                        thumb_index_distance > 50
                        and index_middle_distance > 50
                        and thumb_tip_y > index_mcp_y
                        and thumb_ring_distance < 50
                    ):
                        print("Peace gesture")
                        # strip.set_color(0, 0, 255)

            cv2.imshow("Hand Gesture Recognition", image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    recognize_fingers()
