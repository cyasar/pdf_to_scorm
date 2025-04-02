import os
import zipfile

# SCORM yapılandırma dosyası (imsmanifest.xml)
imsmanifest_template = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="PDF_SCORM_Package" version="1.0"
    xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
    xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 
    ims_cp_rootv1p1p2.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 
    adlcp_rootv1p2.xsd">
    
    <organizations default="ORG">
        <organization identifier="ORG">
            <title>PDF SCORM Package</title>
            <item identifier="ITEM1" identifierref="RES1">
                <title>PDF Document</title>
            </item>
        </organization>
    </organizations>

    <resources>
        <resource identifier="RES1" type="webcontent" href="index.html">
            <file href="index.html"/>
            <file href="document.pdf"/>
        </resource>
    </resources>
</manifest>
"""

# HTML dosyası (PDF görüntüleyici)
html_template = """<!DOCTYPE html>
<html>
<head>
    <title>PDF SCORM Viewer</title>
</head>
<body>
    <embed src="document.pdf" type="application/pdf" width="100%" height="600px" />
</body>
</html>
"""

def create_scorm_package(pdf_path, output_zip):
    """PDF dosyasını SCORM paketi haline getirir."""
    
    if not os.path.exists(pdf_path):
        print("PDF dosyası bulunamadı!")
        return
    
    scorm_dir = "scorm_package"
    os.makedirs(scorm_dir, exist_ok=True)
    
    # PDF'yi kopyala
    pdf_filename = os.path.basename(pdf_path)
    pdf_dest = os.path.join(scorm_dir, pdf_filename)
    os.system(f"cp '{pdf_path}' '{pdf_dest}'")
    
    # HTML dosyası oluştur
    with open(os.path.join(scorm_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_template.replace("document.pdf", pdf_filename))
    
    # imsmanifest.xml dosyası oluştur
    with open(os.path.join(scorm_dir, "imsmanifest.xml"), "w", encoding="utf-8") as f:
        f.write(imsmanifest_template)
    
    # SCORM paketini ZIP olarak oluştur
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(scorm_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, scorm_dir))
    
    print(f"SCORM paketi başarıyla oluşturuldu: {output_zip}")

# Kullanım
create_scorm_package("example.pdf", "scorm_package.zip")
