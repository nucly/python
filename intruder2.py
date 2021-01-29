import cv2

static_back = None

motion_list = [None, None]

video = cv2.VideoCapture(0)

while True:
    
    check, frame = video.read()

    motion = 0
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if static_black None:
        static_black = gray
        continue

    diff_frame = cv2.absdiff(static_back, gray)

    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.TRESH_BINARY)[1]
    tresh_frame = cv2.dilate(tresh_grame, None, iterations = 2)

    cnts,_ = cv2.findContours(tresh_frame.copy(),
                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.countourArea(countour) < 10000:
            continue
        
        motion = 1

        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y) (x + w, y + h), (0, 255, 0), 3)
        
        motion_list.append(motion)

        motion_list = motion_list[-2:]

        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            if motion == 1:
                break

cv2.destroyAllWindows()
