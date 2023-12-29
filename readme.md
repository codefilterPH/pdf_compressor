# PDF Compression Script

This Python script uses the PyMuPDF library to compress PDF files without changing their quality. It takes one or more input PDF files, compresses each one, and saves the compressed versions to the specified output paths.

## Installation

Before running the script, make sure to install the required library:

```bash
pip install PyMuPDF
```

# Usage
- Clone the repository or download the script.
- Open a terminal and navigate to the script's directory.
- Run the script by executing the following command:

```python compress_pdf.py```
**Note:** You can customize the input and output paths within the script.

The compressed PDF files will be saved to the specified output paths.

# Script Details
## Script File
compress_pdf.py: The main script file containing the PDF compression logic.
## Class
PDFCompressor: A class that encapsulates the PDF compression functionality.
# Usage in Main Block
The script can be customized in the __main__ block to specify input and output paths for multiple PDF files.
```
if __name__ == "__main__":
    # Specify the input and output paths
    input_paths = [
        "path/to/input_file1.pdf",
        "path/to/input_file2.pdf",
        # Add more input paths as needed
    ]
    output_paths = [
        "path/to/output_file1_compressed.pdf",
        "path/to/output_file2_compressed.pdf",
        # Add more output paths corresponding to the input files
    ]

    # Compress each PDF
    for input_path, output_path in zip(input_paths, output_paths):
        compressor = PDFCompressor(input_path, output_path)
        compressor.compress_pdf()
```