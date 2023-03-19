import pytest
from project_1 import *

# HTML
@pytest.mark.parametrize("link, expected_result_link, expected_result_text", [('https://pmpu.space', 'https://vk.com/sspmpu', 'Факультет прикладной математики — процессов управления/n')])
def testgetTextAndLinks(link, expected_result_link, expected_result_text):
    assert expected_result_link in getTextAndLinks(link)[0]
    assert expected_result_text in getTextAndLinks(link)[1]

# PDF
@pytest.mark.parametrize("filepath, save_im_to, expected_result", [('testPDF.pdf', 'test_im_folder', "Hi! How are you? What's up?\n\n\x0c")])
def testgetTextAndImagesFromPDF(filepath, save_im_to, expected_result):
    assert getTextAndImagesFromPDF(filepath, save_im_to) == expected_result

# Docx 
@pytest.mark.parametrize("path, expected_result", [('testDocx.docx', "Hi! How are you? What's up?")])
def testgetFromDocx(path, expected_result):
    assert getFromDocx(path)[0] == expected_result

s = """Привет! 
Как дела?


Что делаешь? Я тестирую Docx-документы! 

№;%::?@#$$%&&&*"""

# print(s)

@pytest.mark.parametrize("path, expected_result", [('testDocxRussian.docx', s)])
def testgetFromDocx(path, expected_result):
    print(getFromDocx(path)[0])
    assert getFromDocx(path)[0] == expected_result

