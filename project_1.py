import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
import pdfminer
from pdfminer.image import ImageWriter
from pdfminer.high_level import extract_pages


def getTextAndLinks(link):   #HTML
    req = requests.get(link)
    soup_ing = str(BeautifulSoup(req.content, 'lxml'))
    soup_ing = soup_ing.encode() 
    with open("test.html", "wb") as file: 
        file.write(soup_ing)
    html_file = ("test.html")
    html_file = open(html_file, encoding='UTF-8').read()
    soup = BeautifulSoup(html_file, 'lxml')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href')) 
    text = soup.get_text(separator="/n")
    return links, text

# # links, text = getTextAndLinks("https://mail.ru/")
# # print(links)
# # print(text)

def get_image(layout_object):
    if isinstance(layout_object, pdfminer.layout.LTImage):
        return layout_object
    if isinstance(layout_object, pdfminer.layout.LTContainer):
        for child in layout_object:
            return get_image(child)
    else:
        return None

def save_images_from_page(page: pdfminer.layout.LTPage, save_path):
    images = list(filter(bool, map(get_image, page)))
    iw = ImageWriter(save_path)
    for image in images:
        iw.export_image(image)

def getTextAndImagesFromPDF(filepath, save_im_to):  #PDF
    text = extract_text(filepath)
    pages = list(extract_pages(filepath))
    for page in pages:
        save_images_from_page(page, save_im_to)
    return text

text = getTextAndImagesFromPDF("test.pdf", "test_floder")
print(text)