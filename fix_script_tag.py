file_path = r'c:\Users\Kian-PC\Desktop\zouhour certification\certificate.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace line 9 (index 8)
lines[8] = '    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>\n'

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Line 9 replaced with html2pdf library link.")
