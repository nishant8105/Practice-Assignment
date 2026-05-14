import cv2

video = cv2.VideoCapture("./nature.mp4")


width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

output = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (width, height)
)

while video.isOpened():
    ret, frame = video.read()

    if ret:
        output.write(frame)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(10) & 0xFF == ord('s'):
            break
    else:
        break

video.release()
output.release()
cv2.destroyAllWindows()