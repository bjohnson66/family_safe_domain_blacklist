import re
from bs4 import BeautifulSoup

def extract_domains(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    domain_pattern = re.compile(r'https?://([a-zA-Z0-9.-]+)')

    domains = set()
    for tag in soup.find_all(['a', 'link', 'script']):
        if 'href' in tag.attrs:
            href = tag['href']
            matches = domain_pattern.findall(href)
            if matches:
                domains.update(matches)

    return domains

def save_domains_to_file(domains, output_file):
    with open(output_file, 'w') as file:
        for domain in domains:
            file.write(domain + '\n')

def main():
    input_html_file = 'list_page.html'
    output_text_file = 'output_domains.txt'

    with open(input_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    extracted_domains = extract_domains(html_content)
    save_domains_to_file(extracted_domains, output_text_file)

if __name__ == "__main__":
    main()
