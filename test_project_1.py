import pytest
from project_1 import *

# HTML
@pytest.mark.parametrize("link, expected_result", [('https://google.com', 2), ("https://ya.ru", 2)])
def testgetTextAndLinks(link, expected_result):
    assert len(getTextAndLinks(link)) == expected_result

# PDF
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('test.pdf', 'test_im_folder', "Hi! How are you? What's up?\n\n\x0c")])
def testgetTextAndImagesFromPDF(filepath, save_im_to, expected_result):
    assert getTextAndImagesFromPDF(filepath, save_im_to) == expected_result

# Docx 
@pytest.mark.parametrize("path, expected_result", [('testDocx.docx', "Hi! How are you? What's up?")])
def testgetFromDocx(path, expected_result):
    assert getFromDocx(path)[0] == expected_result