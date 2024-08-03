import cv2 as cv

# the argument 1 connects to the webcam
play = cv.VideoCapture(1)

while True:
    gotframes, frame = play.read()

    if not gotframes:
        break
    
    # displays each frame
    cv.imshow('Camera 1', frame)
    if cv.waitKey(0) == ord('q'):
        break

play.release()
cv.destroyAllWindows()
print(ret)
