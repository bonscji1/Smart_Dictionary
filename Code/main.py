
import cv2
import easyocr
import pytesseract





def mainEasyOCR():
    # downloads packages, takes a while on the first run
    #reader = easyocr.Reader(['en', 'cs', 'es'])
    reader = easyocr.Reader(['en'])

    # read image
    img = cv2.imread('Images/Test.jpg')

    output = reader.readtext(img, detail=1)  # detail 0 for simple output, 1 for expanded

    # options
    # width_ths (float, default = 0.5) - Maximum horizontal distance to merge boxes.

    print('\n')
    print(output)

def mainTessaract():
    # read image
    #img = cv2.imread('Images/Test.jpg')
    img = cv2.imread('Images/page1.jpg')


    # pre-process
    imageShape = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)



    # configurations
    #config = ('-l eng --oem 1 --psm 3')
    config = ('-l spa+ces --oem 1 --psm 3')

    text = pytesseract.image_to_string(blur, config=config)

     # print results
    #text = text.split('\n')
    print(text)




if __name__ == '__main__':
    mainTessaract()
