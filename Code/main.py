import cv2
import easyocr
import pytesseract


def preprocess(img):
    # pre-process
    imageShape = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    return blur


def print_output(text):
    print(text)
    print("----------******************************-------------")


def main_easy_ocr():
    # downloads packages, takes a while on the first run
    # reader = easyocr.Reader(['en', 'cs', 'es'])
    reader = easyocr.Reader(['en'])

    # read image
    img = cv2.imread('Images/Test.jpg')

    output = reader.readtext(img, detail=1)  # detail 0 for simple output, 1 for expanded

    # options
    # width_ths (float, default = 0.5) - Maximum horizontal distance to merge boxes.

    print('\n')
    print(output)


def main_tesseract():
    # configurations
    config = ('-l spa+ces --oem 1 --psm 3')

    # read image
    img = cv2.imread('Images/page1_v2.jpg')
    pimg = preprocess(img)

    # preprocess
    pimg = preprocess(img)

    text = pytesseract.image_to_string(pimg, config=config)

    # print results
    # text = text.split('\n')
    print(text)


def testing_tesseract():
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

    print("Tesseract output:")
    print_output(text0)
    # print_output(text1)
    # print_output(text2)


def testing_easy_ocr():
    reader = easyocr.Reader(['en'])

    # read image
    img0 = cv2.imread('Images/Test.jpg')

    output = reader.readtext(img0, detail=0)  # detail 0 for simple output, 1 for expanded

    # options
    # width_ths (float, default = 0.5) - Maximum horizontal distance to merge boxes.

    print("EasyOCR output:")
    print_output(output)


if __name__ == '__main__':
    # main_tesseract()
    # main_easy_ocr()

    # testing_tesseract()
    testing_easy_ocr()
