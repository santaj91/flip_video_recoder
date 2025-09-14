import cv2

ip_cam_url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'

cap=cv2.VideoCapture(ip_cam_url)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

is_recording = False
is_flipped = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if is_flipped:
        frame = cv2.flip(frame, 1)

    frame_copy = frame.copy()

    if is_recording:
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        out.write(frame_copy)

    cv2.imshow('IP Camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC -> quit
        break
    elif key == 32:  # Space -> recoder
        is_recording = not is_recording
        print("Recording:", is_recording)
    elif key == ord('f'):  # f -> flip
        is_flipped = not is_flipped
        print("Flip:", is_flipped)

cap.release()
out.release()
cv2.destroyAllWindows()