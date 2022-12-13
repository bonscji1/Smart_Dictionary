
import cv2
import easyocr
import pytesseract


def preprocess(img):
    # pre-process
    imageShape = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    return blur

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
    # configurations
    config = ('-l spa+ces --oem 1 --psm 3')

    #read image
    img = cv2.imread('Images/page1_v2.jpg')
    pimg = preprocess(img)

    #preprocess
    pimg = preprocess(img)


    text = pytesseract.image_to_string(pimg, config=config)

     # print results
    #text = text.split('\n')
    print(text)


def testingTessaract():
    # Testing
    # configurations
    config = ('-l eng --oem 1 --psm 3')


    # read image
    img0 = cv2.imread('Images/Test.jpg')
    img1 = cv2.imread('Images/test_1.png')
    img2 = cv2.imread('Images/test_2.png')

    pimg0 = preprocess(img0)
    pimg1 = preprocess(img1)
    pimg2 = preprocess(img2)

    text0 = pytesseract.image_to_string(pimg0, config=config)
    text1 = pytesseract.image_to_string(pimg1, config=config)
    text2 = pytesseract.image_to_string(pimg2, config=config)

    # print results
    # text = text.split('\n')
    print(text0)
    print("----------******************************-------------")
    print(text1)
    print("----------******************************-------------")
    print(text2)




if __name__ == '__main__':
    #mainTessaract()
    #mainEasyOCR()
    mainKeras()

    #testingTessaract()
