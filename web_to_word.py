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
    print(f"The web page content has been successfully exported to {file_name}.")

if __name__ == "__main__":
    url = input("Enter the URL of the website -> (https://example.com): ")
    file_name = input("Enter the name of the Word file to be saved -> (e.g. output.docx): ")
    main(url, file_name)
