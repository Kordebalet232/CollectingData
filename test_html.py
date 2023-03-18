import pytest
from project_1 import getTextAndLinks

# HTML
@pytest.mark.parametrize("link, expected_result_link, expected_result_text", [('https://pmpu.space', 'https://vk.com/sspmpu', 'Факультет прикладной математики — процессов управления/n')])
def testgetTextAndLinks(link, expected_result_link, expected_result_text):
    assert expected_result_link in getTextAndLinks(link)[0]
    assert expected_result_text in getTextAndLinks(link)[1]