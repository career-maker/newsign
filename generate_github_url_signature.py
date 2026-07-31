import os
from pathlib import Path

# GitHub raw content URLs
GITHUB_RAW_URL = "https://raw.githubusercontent.com/career-maker/newsign/master"

image_urls = {
    'Logo-7.svg': f'{GITHUB_RAW_URL}/Logo-7.svg',
    'watermark.png': f'{GITHUB_RAW_URL}/watermark.png',
    'logo-wca.png': f'{GITHUB_RAW_URL}/logo-wca.png',
    'logo-jctrans.png': f'{GITHUB_RAW_URL}/logo-jctrans.png',
    'logo-gla.png': f'{GITHUB_RAW_URL}/logo-gla.png',
    'logo-mundu.png': f'{GITHUB_RAW_URL}/logo-mundu.png',
    'logo-icv.jpeg': f'{GITHUB_RAW_URL}/logo-icv.jpeg',
    'logo-iso.png': f'{GITHUB_RAW_URL}/logo-iso.png',
    'logo-nafl.png': f'{GITHUB_RAW_URL}/logo-nafl.png',
    'logo-fiata.svg': f'{GITHUB_RAW_URL}/logo-fiata.svg',
}

# Read the original index.html
with open(Path(__file__).parent / 'index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace image sources with GitHub URLs
for filename, url in image_urls.items():
    html = html.replace(f'src="{filename}"', f'src="{url}"')

# Write the GitHub URL version
output_path = Path(__file__).parent / 'outlook_signature_github_urls.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Generated {output_path}')
print(f'Uses GitHub raw URLs for reliable Outlook compatibility')
