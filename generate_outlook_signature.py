import os
import base64
from pathlib import Path

# Map of file paths to their MIME types
image_files = {
    'Logo-7.svg': ('image/svg+xml', 'logo'),
    'watermark.png': ('image/png', 'watermark'),
    'logo-wca.png': ('image/png', 'logo_wca'),
    'logo-jctrans.png': ('image/png', 'logo_jctrans'),
    'logo-gla.png': ('image/png', 'logo_gla'),
    'logo-mundu.png': ('image/png', 'logo_mundu'),
    'logo-icv.jpeg': ('image/jpeg', 'logo_icv'),
    'logo-iso.png': ('image/png', 'logo_iso'),
    'logo-nafl.png': ('image/png', 'logo_nafl'),
    'logo-fiata.svg': ('image/svg+xml', 'logo_fiata'),
}

# Read and encode images
encoded_images = {}
for filename, (mime_type, key) in image_files.items():
    filepath = Path(__file__).parent / filename
    if filepath.exists():
        with open(filepath, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            encoded_images[key] = f'data:{mime_type};base64,{data}'
        print(f'+ Encoded {filename}')
    else:
        print(f'- Missing {filename}')

# Read the original HTML
with open(Path(__file__).parent / 'index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace image sources
replacements = {
    'src="Logo-7.svg"': f'src="{encoded_images.get("logo", "")}"',
    'src="watermark.png"': f'src="{encoded_images.get("watermark", "")}"',
    'src="logo-wca.png"': f'src="{encoded_images.get("logo_wca", "")}"',
    'src="logo-jctrans.png"': f'src="{encoded_images.get("logo_jctrans", "")}"',
    'src="logo-gla.png"': f'src="{encoded_images.get("logo_gla", "")}"',
    'src="logo-mundu.png"': f'src="{encoded_images.get("logo_mundu", "")}"',
    'src="logo-icv.jpeg"': f'src="{encoded_images.get("logo_icv", "")}"',
    'src="logo-iso.png"': f'src="{encoded_images.get("logo_iso", "")}"',
    'src="logo-nafl.png"': f'src="{encoded_images.get("logo_nafl", "")}"',
    'src="logo-fiata.svg"': f'src="{encoded_images.get("logo_fiata", "")}"',
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Write the Outlook-compatible version
output_path = Path(__file__).parent / 'outlook_signature.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\n+ Generated {output_path}')
