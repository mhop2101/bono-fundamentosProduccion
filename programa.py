import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def insert_image_in_pdf(image_path, margins, dimensions, output_pdf):

    margin_left, margin_right, margin_top, margin_bottom = margins
    page_width, page_height = dimensions

    c = canvas.Canvas(output_pdf, pagesize=(page_width, page_height))

    img = Image.open(image_path)

    image_width = page_width - margin_left - margin_right
    image_height = page_height - margin_top - margin_bottom

    c.drawImage(image_path, margin_left, margin_bottom, width=image_width, height=image_height)

    c.save()

def main():
    parser = argparse.ArgumentParser(description="Inserta una imagen en un PDF con márgenes y dimensiones específicas.")
    parser.add_argument('margin_left', type=int, help='Margen izquierdo')
    parser.add_argument('margin_right', type=int, help='Margen derecho')
    parser.add_argument('margin_top', type=int, help='Margen superior')
    parser.add_argument('margin_bottom', type=int, help='Margen inferior')
    parser.add_argument('image_path', type=str, help='Ruta de la imagen')
    parser.add_argument('output_pdf', type=str, help='Ruta del PDF de salida')
    parser.add_argument('--width', type=int, default=600, help='Ancho del PDF (por defecto: 600)')
    parser.add_argument('--height', type=int, default=800, help='Alto del PDF (por defecto: 800)')

    args = parser.parse_args()

    margins = (args.margin_left, args.margin_right, args.margin_top, args.margin_bottom)
    dimensions = (args.width, args.height)

    insert_image_in_pdf(args.image_path, margins, dimensions, args.output_pdf)

if __name__ == "__main__":
    main()
