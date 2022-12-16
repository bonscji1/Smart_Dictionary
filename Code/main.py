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

def testing_easy_ocr():
    reader = easyocr.Reader(['en'])

    # read image
    img0 = cv2.imread('Images/Test.jpg')

    output = reader.readtext(img0, detail=0)  # detail 0 for simple output, 1 for expanded

    # options
    # width_ths (float, default = 0.5) - Maximum horizontal distance to merge boxes.

    print("EasyOCR output:")
    print_output(output)


def test_easy_ocr(img, config):
    reader = easyocr.Reader(config)

    return reader.readtext(img, detail=0)



def main_easy_ocr():
    # downloads packages, takes a while on the first run
    reader = easyocr.Reader(['cs', 'es'])

    # read image
    img = cv2.imread('Images/page1.jpg')

    output = reader.readtext(img, detail=0)  # detail 0 for simple output, 1 for expanded

    # options
    # width_ths (float, default = 0.5) - Maximum horizontal distance to merge boxes.

    print("EasyOCR output:")
    print_output(output)


def main_tesseract():
    # configurations
    config = '-l spa+ces --oem 1 --psm 3'

    # read image
    img = cv2.imread('Images/page1.jpg')

    # preprocess
    pimg = preprocess(img)

    text = pytesseract.image_to_string(pimg, config=config)

    # print results
    print("Tesseract output:")
    print_output(text)


def test_tesseract(img, config):
    prep_img = preprocess(img)

    return pytesseract.image_to_string(prep_img, config=config)


def testing_tesseract():
    # configurations
    config = '-l eng --oem 1 --psm 3'

    # read image
    img0 = cv2.imread('Images/Test.jpg')
    img1 = cv2.imread('Images/test_1.png')
    img2 = cv2.imread('Images/test_2.png')
    img3 = cv2.imread('Images/page_test.jpg')

    # text0 = test_tesseract(img0, config)
    # text1 = test_tesseract(img1, config)
    # text2 = test_tesseract(img2, config)

    config = '-l spa+ces --oem 1 --psm 3'
    text3 = test_tesseract(img3, config)

    print("Tesseract output:")
    # print_output(text0)
    # print_output(text1)
    # print_output(text2)
    print_output(text3)



def comparative_testing():
    # set testing image
    img = cv2.imread('Images/Test.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['cs', 'es']




if __name__ == '__main__':
    main_tesseract()
    main_easy_ocr()

    # testing_tesseract()
    # testing_easy_ocr()
