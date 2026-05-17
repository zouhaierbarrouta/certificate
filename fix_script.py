import os
import re

path = r"c:\Users\Kian-PC\Desktop\zouhour certification\certificate.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new script
new_script = """    <script>
        async function printToPDF() {
            const btn = document.querySelector('.print-btn');
            const originalContent = btn.innerHTML;
            
            // 1. Update button state
            btn.innerHTML = '⏳ جاري المعالجة...';
            btn.disabled = true;
            btn.style.opacity = '0.7';
            btn.style.cursor = 'wait';

            const element = document.getElementById('certificateContent');
            const opt = {
                margin: 5,
                filename: 'شهادة_شكر_وتقدير.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2, useCORS: true },
                jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' }
            };

            try {
                // 2. Generate PDF
                await html2pdf().set(opt).from(element).save();
            } catch (error) {
                console.error('Error generating PDF:', error);
            } finally {
                // 3. Restore button state
                btn.innerHTML = originalContent;
                btn.disabled = false;
                btn.style.opacity = '1';
                btn.style.cursor = 'pointer';
            }
        }
    </script>"""

# Replace the broken script tag
# We look for the <script> tag after the certificate content
content = re.sub(r'    <script>.*?</script>', new_script, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Script updated successfully")
