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


def comparative_print(test_name, text_tes, text_eocr):
    print(test_name + '\n')
    print("Tesseract output:")
    print_output(text_tes)
    print("EasyOCR output:")
    print_output(text_eocr)


def comparative_testing():
    # set testing image 1
    img = cv2.imread('Images/Test.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['en']

    #ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    #print output
    comparative_print("Default testing image", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 2 -> second testing image
    img = cv2.imread('Images/test_1.png')

    # set testing configurations
    config_tes = '-l eng --oem 1 --psm 3'
    config_eocr = ['en']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("Default testing image 2", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 2 -> second testing image with added language
    img = cv2.imread('Images/test_1.png')

    # set testing configurations
    config_tes = '-l spa+eng --oem 1 --psm 3'
    config_eocr = ['en', 'es']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("Default testing image 2 with 2 languages", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 3 -> testing for procedurally smaller text
    img = cv2.imread('Images/test_2.png')

    # set testing configurations
    config_tes = '-l eng --oem 1 --psm 3'
    config_eocr = ['en']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("Procedurally smaller text", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 4 -> small try on real data blurry
    img = cv2.imread('Images/page_test.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['cs', 'es']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("small real data blurry", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 5 -> small try on real data v2
    img = cv2.imread('Images/page_test_2.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['cs', 'es']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("small real data", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 5 -> small try on real data v2, sigle language
    img = cv2.imread('Images/page_test_2.jpg')

    # set testing configurations
    config_tes = '-l ces --oem 1 --psm 3'
    config_eocr = ['cs']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("small real data only 1 language", text_tes, text_eocr)

    # ******************************************************************
    # set testing image 6 -> real data
    img = cv2.imread('Images/page1.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['cs', 'es']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("Real data", text_tes, text_eocr)

    # ******************************************************************

    # set testing image 7 -> real data v2
    img = cv2.imread('Images/page1_v2.jpg')

    # set testing configurations
    config_tes = '-l spa+ces --oem 1 --psm 3'
    config_eocr = ['cs', 'es']

    # ocr
    text_tes = test_tesseract(img, config_tes)
    text_eocr = test_easy_ocr(img, config_eocr)

    # print output
    comparative_print("Real data adjusted for smaller image size", text_tes, text_eocr)



if __name__ == '__main__':
    # main_tesseract()
    # main_easy_ocr()

    # testing_tesseract()
    # testing_easy_ocr()

    comparative_testing()
