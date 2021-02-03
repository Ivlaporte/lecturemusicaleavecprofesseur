from pdf2image import convert_from_path

pagLMAP = convert_from_path('LecturePAP1dN1.pdf', 1)

pagLMAP.save('LecturePAP1dN1.jpg', 'JPEG')