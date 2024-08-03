import cv2 as cv

# the argument 1 connects to the webcam
play = cv.VideoCapture(1)

while True:
    gotframes, frame = play.read()

    if not gotframes:
        break
    
    # displays each frame
<<<<<<< HEAD:test.py
    cv.imshow('frame', frame)
=======
    cv.imshow('Camera 1', frame)
>>>>>>> 97d6e506c11ab5ede73a3cf94cd6958e0043caaa:camerafeed.py
    if cv.waitKey(0) == ord('q'):
        break

play.release()
cv.destroyAllWindows()
print(ret)
