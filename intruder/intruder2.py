import cv2, smtplib, ssl
import time

port = 465
password = input("Type your email password and press enter: ")
sender_email = "koksychelmar@gmail.com"
receiver_email = "kaminski.darek@icloud.com"
message = "Intruuuuuuuuuz"
context = ssl.create_default_context()

def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login("koksychelmar@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

def test_email():
    print('sending email')

def start_motion():
    video = cv2.VideoCapture(0)
    static_back = None

    while True:

        motion = 0
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if static_back is None:
            static_back = gray
            continue

        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 100, 255, cv2.THRESH_BINARY)[1] 
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
        cnts,_ = cv2.findContours(thresh_frame.copy(),
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue
            motion = 1

            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if motion == 1:
            video.release()
            cv2.destroyAllWindows()
            test_email();
            time.sleep(5)
            start_motion()

start_motion()
