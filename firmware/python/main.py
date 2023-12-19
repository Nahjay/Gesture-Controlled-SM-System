import cv2
import numpy as np
import os


def create_image_list():
    folderpath = "images"
    mylist = os.listdir(folderpath)
    print(mylist)
    list = []
    for img in mylist:
        curImg = cv2.imread(f"{folderpath}/{img}")
        curImg = cv2.resize(curImg, (200, 200))
        list.append(curImg)

    return list


# def detect_hand(frame):
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian blur to the grayscale image
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Use thresholding to create a binary image
#     _, threshold = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)

#     # Find contours in the binary image
#     contours, _ = cv2.findContours(
#         threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
#     )

#     # Find the largest contour (assuming it's the hand)
#     if contours:
#         hand_contour = max(contours, key=cv2.contourArea)

#         # Perform convex hull to get a polygon around the hand
#         hull = cv2.convexHull(hand_contour)

#         # Calculate the area of the convex hull and the original hand contour
#         hull_area = cv2.contourArea(hull)
#         hand_area = cv2.contourArea(hand_contour)

#         # Calculate the solidity (ratio of convex hull area to hand area)
#         solidity = hull_area / hand_area if hand_area > 0 else 0

#         # If the solidity is within a certain range, consider it a thumbs-up
#         if 0.2 < solidity < 0.4:
#             return True

#     return False


def main():
    cap = cv2.VideoCapture("/dev/video0")  # Adjust the device path as needed'

    overlay = create_image_list()

    while True:
        ret, image = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        else:
            image[0:200, 0:200] = overlay[1]

            cv2.imshow("Hand Gesture Recognition", image)
            cv2.waitKey(1)

            # # Flip the frame horizontally for a more natural appearance
            # frame = cv2.flip(frame, 1)

            # # Detect thumbs-up
            # thumbs_up = detect_hand(frame)

            # # Display the frame with a text overlay
            # text = "Thumbs Up!" if thumbs_up else "No Thumbs Up"
            # cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # cv2.imshow("Hand Gesture Recognition", frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
