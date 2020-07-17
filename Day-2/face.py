import cv2

cap = cv2.VideoCapture(0)
Classifier =  cv2. CascadeClassifier(r"C:\Users\admin\Desktop\charm\haarcascade_frontalface_default.xml")

while True:
    ret ,frame = cap.read()
    if ret:
        faces = Classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        cv2.imshow("my window", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindowa()
