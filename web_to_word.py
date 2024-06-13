import requests
from bs4 import BeautifulSoup
from docx import Document

def fetch_web_content(url):
    response = requests.get(url)
    response.raise_for_status()  # HTTP hatalarını kontrol et
    return response.content

def parse_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_text(soup):
    paragraphs = soup.find_all('p')
    text_content = [paragraph.get_text() for paragraph in paragraphs]
    return text_content

def save_to_word(text_content, file_name):
    doc = Document()
    for paragraph in text_content:
        doc.add_paragraph(paragraph)
    doc.save(file_name)

def main(url, file_name):
    html_content = fetch_web_content(url)
    soup = parse_content(html_content)
    text_content = extract_text(soup)
    save_to_word(text_content, file_name)
    print(f"Web sayfası içeriği başarıyla {file_name} dosyasına aktarıldı.")

if __name__ == "__main__":
    url = input("Web sayfası URL'sini girin: ")
    file_name = input("Kaydedilecek Word dosyasının adını girin (örn. output.docx): ")
    main(url, file_name)
