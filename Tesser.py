import pytesseract as Tess
Tess.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path
import os

PathIMG = input('Введите путь к файлу:\n')

if Path(PathIMG).suffix == '.pdf':
	pages = convert_from_path(PathIMG, 100, poppler_path = r'poppler-0.68.0\bin')
	counter = 1
	for page in pages:
		page.save(f'Title{counter}.png')
		PDF = Tess.image_to_pdf_or_hocr(f'Title{counter}.png', extension = 'pdf', lang = 'rus')
		with open('ScanFromPDF.pdf', 'w+b') as f:
			f.write(PDF)
			f.close()
		os.remove(f'Title{counter}.png')
		counter += 1
else:
	PDF = Tess.image_to_pdf_or_hocr(PathIMG, extension = 'pdf', lang = 'rus')
	with open('scan.pdf', 'w+b') as f:
		f.write(PDF)
		f.close()