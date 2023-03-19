import pytest
from project_1 import getTextAndImagesFromPDF, extract_pages, get_image
from pdfminer.image import ImageWriter

# PDF with text
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('testPDF.pdf', 'test_im_folder', "Hi! How are you? What's up?\n\n\x0c")])
def testgetTextAndImagesFromPDF(filepath, save_im_to, expected_result):
    assert getTextAndImagesFromPDF(filepath, save_im_to) == expected_result

# PDF without text
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('testPDFPic.pdf', 'test_im_folder', "\x0c")])
def testgetTextAndImagesFromPDF2(filepath, save_im_to, expected_result):
    assert getTextAndImagesFromPDF(filepath, save_im_to) == expected_result

# PDF with image
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('testPDFPic.pdf', 'test_im_folder', "testImage.jpeg")])
def testgetTextAndImagesFromPDF3(filepath, save_im_to, expected_result):
    with open(expected_result, "rb") as imageFile:
        f = imageFile.read()

        pages = list(extract_pages(filepath))
        for page in pages:
            images = list(filter(bool, map(get_image, page)))
            for image in images:
                iw = ImageWriter(save_im_to)
                newImageName = iw.export_image(image)
                with open(save_im_to + '/' + newImageName, "rb") as imageFile2:
                    f2 = imageFile2.read()
                    assert f == f2
                
s = """Привет! 
Как дела?


Что делаешь? Я тестирую Docx-документы! 

№;%::?@#$$%&&&*"""


# PDF with russian text
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('testPDFRussian.pdf', 'test_im_folder', s)])
def testgetTextAndImagesFromPDF4(filepath, save_im_to, expected_result):
    assert getTextAndImagesFromPDF(filepath, save_im_to) == expected_result