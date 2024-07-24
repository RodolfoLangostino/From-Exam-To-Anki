import PyPDF2

def pdftotxt(pdf_file, skip_pages=2):
    with open(pdf_file, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        num_paginas = len(lector_pdf.pages)
        texto = ""
        for num_pagina in range(skip_pages, num_paginas):
            pagina = lector_pdf.pages[num_pagina]
            texto += pagina.extract_text() + "\n"
    print (f"The text has been extracted from {pdf_file}")
    #print (texto)
    return texto

# Example to use the function
# pdftotxt("tu_archivo.pdf", "salida.txt")