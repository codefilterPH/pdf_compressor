import os
import sys
import PyMuPDF

class PDFCompressor:
    """
    A class for compressing PDF files without changing the quality.

    Attributes:
        input_path (str): The path to the input PDF file.
        output_path (str): The path to save the compressed PDF file.

    Methods:
        compress_pdf(): Compresses the PDF and saves the compressed version.
    """

    def __init__(self, in_path, out_path):
        """
        Initializes a PDFCompressor object.

        Parameters:
            in_path (str): The path to the input PDF file.
            out_path (str): The path to save the compressed PDF file.
        """
        self.input_path = in_path
        self.output_path = out_path

    def compress_pdf(self):
        """
        Compresses the PDF and saves the compressed version.
        """
        # Check if the input file exists
        if not os.path.isfile(self.input_path):
            print(f"Error: Input file '{self.input_path}' not found.")
            sys.exit(1)

        # Open the PDF file
        pdf_document = PyMuPDF.open(self.input_path)

        # Create a PDF writer
        pdf_writer = PyMuPDF.open()

        # Iterate through each page and copy it to the new PDF
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            pix = page.get_pixmap()

            # Create a new page with the same size
            new_page = pdf_writer.new_page(width=pix.width, height=pix.height)

            # Draw the pixmap on the new page
            new_page.insert_image((0, 0), pixmap=pix)

        # Save the compressed PDF to the specified output path
        pdf_writer.save(self.output_path)
        pdf_writer.close()

        print(f"Compression successful. Compressed PDF saved to '{self.output_path}'.")


if __name__ == "__main__":
    # Specify the input and output paths
    input_paths = [
        "upload/dependent_father.pdf",
        "upload/dependent_mother.pdf",
    ]
    output_paths = [
        "output/dependent_father_compressed.pdf",
        "output/dependent_mother_compressed.pdf"
    ]

    # Compress each PDF
    for input_path, output_path in zip(input_paths, output_paths):
        compressor = PDFCompressor(input_path, output_path)
        compressor.compress_pdf()
