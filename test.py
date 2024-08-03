import cv2 as cv

# the argument 1 connects to the webcam
play = cv.VideoCapture(1)

while True:
    ret, frame = play.read()

    if not ret:
        break
    
    # displays each frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

play.release()
cv.destroyAllWindows()
print(ret)