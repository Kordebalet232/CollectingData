import pytest
from project_1 import getFromDocx

# Docx 
@pytest.mark.parametrize("path, expected_result", [('testDocx.docx', "Hi! How are you? What's up?")])
def testgetFromDocx(path, expected_result):
    assert getFromDocx(path)[0] == expected_result

s = """Привет! 
Как дела?


Что делаешь? Я тестирую Docx-документы! 

№;%::?@#$$%&&&*"""

@pytest.mark.parametrize("path, expected_result", [('testDocxRussian.docx', s)])
def testgetFromDocx2(path, expected_result):
    print(getFromDocx(path)[0])
    assert getFromDocx(path)[0] == expected_result

@pytest.mark.parametrize("path, expected_result", [('empty.docx', "")])
def testgetFromDocx3(path, expected_result):
    print(getFromDocx(path)[0])
    assert getFromDocx(path)[0] == expected_result

table = """№

Колонка 1

Колонка 2

Колонка 3

Строка 1

1

2

3

Строка 2

4

5

6

Строка 3

7

8

9

Итого

12

15

18"""

@pytest.mark.parametrize("path, expected_result", [('testDocxTable.docx', table)])
def testgetFromDocx4(path, expected_result):
    print(getFromDocx(path)[0])
    assert str(getFromDocx(path)[0]) == expected_result