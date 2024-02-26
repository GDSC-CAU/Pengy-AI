import cv2
import argparse
from ultralytics import YOLO

# Setup command line arguments.
parser = argparse.ArgumentParser(description='Run YOLOv8 model on video or webcam.')
parser.add_argument('model', type=str, help='Path to the YOLOv8 model file.')
args = parser.parse_args()

# Load the YOLOv8 model
model = YOLO(args.model)

# Use your webcam
cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results.render()[0]

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Break the loop if the end of the video is reached or any error occurs
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
