$cwd = "c:\Users\Kian-PC\Desktop\zouhour certification"

$studentBytes = [System.IO.File]::ReadAllBytes("$cwd\img\student.png")
$studentB64 = [System.Convert]::ToBase64String($studentBytes)

$bgBytes = [System.IO.File]::ReadAllBytes("$cwd\img\background.png")
$bgB64 = [System.Convert]::ToBase64String($bgBytes)

$htmlPath = "$cwd\index.html"
$htmlContent = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)
# We replace the previous base64 or path with the new base64
# To be safe, we can regex replace the src and url values
$htmlContent = $htmlContent -replace 'src="[^"]+"', "src=""data:image/png;base64,$studentB64"""

[System.IO.File]::WriteAllText($htmlPath, $htmlContent, [System.Text.Encoding]::UTF8)

$cssPath = "$cwd\style.css"
$cssContent = [System.IO.File]::ReadAllText($cssPath, [System.Text.Encoding]::UTF8)
$cssContent = $cssContent -replace "url\('[^']+'\)", "url('data:image/png;base64,$bgB64')"
[System.IO.File]::WriteAllText($cssPath, $cssContent, [System.Text.Encoding]::UTF8)

Write-Host "Done"
