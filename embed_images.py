import base64
import os

def get_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 1. Update style.css
css_path = r'c:\Users\Kian-PC\Desktop\zouhour certification\style.css'
bg_path = r'c:\Users\Kian-PC\Desktop\zouhour certification\img\background.png'

if os.path.exists(bg_path):
    bg_base64 = get_base64(bg_path)
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Replace the url reference
    import re
    new_css = re.sub(r'url\([\'"]?img/background\.png[\'"]?\)', f'url("data:image/png;base64,{bg_base64}")', css_content)
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("style.css updated with base64 background.")

# 2. Update certificate.html
html_path = r'c:\Users\Kian-PC\Desktop\zouhour certification\certificate.html'
st_path = r'c:\Users\Kian-PC\Desktop\zouhour certification\img\student.png'

if os.path.exists(st_path):
    st_base64 = get_base64(st_path)
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Replace the img src reference
    new_html = re.sub(r'src="img/student\.png"', f'src="data:image/png;base64,{st_base64}"', html_content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("certificate.html updated with base64 student image.")
