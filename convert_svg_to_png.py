#!/usr/bin/env python3
import os
import base64
from pathlib import Path

# For SVG to PNG conversion, we'll use a simple approach:
# Read SVG files and embed them, then create a version with alternative approach

# Read the original SVG files as base64
def encode_file(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Get image files
logo_svg_b64 = encode_file('Logo-7.svg')
fiata_svg_b64 = encode_file('logo-fiata.svg')
watermark_png_b64 = encode_file('watermark.png')
wca_b64 = encode_file('logo-wca.png')
jctrans_b64 = encode_file('logo-jctrans.png')
gla_b64 = encode_file('logo-gla.png')
mundu_b64 = encode_file('logo-mundu.png')
icv_b64 = encode_file('logo-icv.jpeg')
iso_b64 = encode_file('logo-iso.png')
nafl_b64 = encode_file('logo-nafl.png')

# Create Outlook-compatible version with embedded PNG/JPEG logos (no SVG)
# Skip SVG logos for Outlook compatibility
html = f'''<div style="font-family: 'Segoe UI', Arial, sans-serif; color: #2a3550; max-width: 500px;">

<div style="margin-bottom: 16px;">
  <div style="font-size: 16px; font-weight: bold; color: #14315c; margin-bottom: 2px;">Sahal Musthafa V</div>
  <div style="font-size: 10px; font-weight: bold; color: #1c5594; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px;">Pricing &amp; Sales Coordinator</div>
  <img src="data:image/png;base64,{watermark_png_b64}" alt="" style="height: 30px; width: auto; margin: 4px 0;">
</div>

<div style="border-top: 2px solid #14315c; border-bottom: 1px solid #e6ebf3; padding: 12px 0; margin-bottom: 12px; font-size: 11.5px;">
  <div style="font-weight: bold; color: #14315c; margin-bottom: 3px;">Sprint Logistic Services LLC</div>
  <div style="color: #75849e; font-size: 11px; line-height: 1.6;">
    P O Box 90631, Suite-308,310,312, Belhoul Group Building,<br>
    Entrance 4, 3rd Floor, Near Dubai Cargo Village,<br>
    Al Garhoud, Dubai, UAE
  </div>
</div>

<div style="font-size: 11px; line-height: 1.8;">
  <div><span style="font-weight: bold; color: #14315c;">P</span> &nbsp;Tel: <a href="tel:+97142399448" style="color: #2a3550; text-decoration: none;">+971-4-2399448</a> &nbsp;|&nbsp; Fax: +971-4-2399447</div>
  <div><span style="font-weight: bold; color: #14315c;">M</span> &nbsp;<a href="tel:+971545130911" style="color: #14315c; text-decoration: none; font-weight: bold;">+971 54 513 0911</a></div>
  <div><span style="font-weight: bold; color: #14315c;">E</span> &nbsp;<a href="mailto:sahal@sprintlogi.com" style="color: #1c5594; text-decoration: none;">sahal@sprintlogi.com</a></div>
  <div><span style="font-weight: bold; color: #14315c;">W</span> &nbsp;<a href="https://www.sprintlogisticservices.com" style="color: #1c5594; text-decoration: none;">www.sprintlogisticservices.com</a></div>
</div>

<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #eef1f8; text-align: center;">
  <img src="data:image/png;base64,{wca_b64}" alt="WCA" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/png;base64,{jctrans_b64}" alt="JCtrans" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/png;base64,{gla_b64}" alt="GLA" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/png;base64,{mundu_b64}" alt="Mundu" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/jpeg;base64,{icv_b64}" alt="ICV" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/png;base64,{iso_b64}" alt="ISO" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
  <img src="data:image/png;base64,{nafl_b64}" alt="NAFL" style="height: 24px; width: auto; margin: 2px 3px; vertical-align: middle;">
</div>

<div style="border-top: 1px solid #eef1f8; padding-top: 8px; margin-top: 12px; font-size: 8px; color: #9aa6bb; font-style: italic; line-height: 1.5; text-align: center;">
  Sprint Logistic Services LLC is a member of NAFL, Dubai and all business is carried out subject to NAFL standard Trading Conditions.
</div>

</div>'''

with open('outlook_signature_embedded.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Generated outlook_signature_embedded.html')
print(f'All PNG/JPEG images embedded (skipped SVG logos for Outlook compatibility)')
print(f'File size: {len(html)} bytes')
