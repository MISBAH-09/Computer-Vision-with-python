import cv2

# Path to video file
video_path = "Chapter 02/images/input.mp4"

cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties 
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("FPS:", fps)
print("Resolution:", width, "x", height)

# Create VideoWriter to save output
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter("Chapter 02/images/output.mp4", fourcc, fps, (width, height))
out2 = cv2.VideoWriter("Chapter 02/images/output_gray.mp4", fourcc, fps, (width, height))

# Read, Display, and Save frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("End of video reached.")
        break

    # Flip frame
    flipped_frame = cv2.flip(frame, -1)

    # Grayscale frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    # ----------------------------
    # Add FPS text to both frames
    # ----------------------------
    text = f"FPS: {fps:.2f}"
    cv2.putText(flipped_frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    cv2.putText(gray_frame_bgr, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # Show video
    cv2.imshow("Video", flipped_frame)

    # Save videos
    out.write(flipped_frame)
    out2.write(gray_frame_bgr)

    # Quit manually
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
out2.release()
cv2.destroyAllWindows()
