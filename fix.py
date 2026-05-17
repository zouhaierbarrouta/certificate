import base64
import os

cwd = r'c:\Users\Kian-PC\Desktop\zouhour certification'

def to_base64(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

student_b64 = to_base64(os.path.join(cwd, 'images', 'student.png'))
bg_b64 = to_base64(os.path.join(cwd, 'images', 'background.png'))

html_path = os.path.join(cwd, 'certificate.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('"images/student.png"', f'"data:image/png;base64,{student_b64}"')
html = html.replace('.save().from(element).save()', '.from(element).save()')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = os.path.join(cwd, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("'images/background.png'", f"'data:image/png;base64,{bg_b64}'")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('Done')
