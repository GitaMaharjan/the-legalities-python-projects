import os  # Import the os module for interacting with the operating system
from PIL import Image  # Import Image class from PIL for image processing
from fpdf import FPDF  # Import FPDF class for creating PDF documents
from docx2pdf import convert  # Import convert function for converting Word documents to PDF

import os  # Import the os module for interacting with the operating system
from PIL import Image  # Import Image class from PIL for image processing
from fpdf import FPDF  # Import FPDF class for creating PDF documents
from docx2pdf import convert  # Import convert function for converting Word documents to PDF

def convert_images_to_pdf(input_directory, output_pdf_path):
    # Ensure the output directory exists
    output_directory = os.path.dirname(output_pdf_path)  # Extract the directory from the output path
    os.makedirs(output_directory, exist_ok=True)  # Create the directory if it does not exist

    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print("Error: Input directory does not exist.")  # Print error if directory doesn't exist
        return

    images = []  # List to hold images for PDF conversion
    # Iterate over files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_file_path = os.path.join(input_directory, filename)  # Create full file path
            try:
                img = Image.open(input_file_path)  # Open the image file
                if img.mode != 'RGB':  # Check if the image is in RGB mode
                    img = img.convert('RGB')  # Convert image to RGB if necessary
                images.append(img)  # Add image to the list
                print(f"Added '{filename}' to PDF list.")  # Print success message
            except (IOError, ValueError) as e:
                print(f"Error: Failed to add '{filename}': {e}")  # Print error if image can't be opened

    # Check if there are images to save
    if images:
        try:
            images[0].save(output_pdf_path, save_all=True, append_images=images[1:])  # Save images as PDF
            print(f"Converted images to PDF successfully: {output_pdf_path}")  # Print success message
        except Exception as e:
            print(f"Error: Failed to save PDF: {e}")  # Print error if PDF can't be saved
    else:
        print("Warning: No images found to convert.")  # Print warning if no images were found

def convert_text_to_pdf(input_directory, output_directory):
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print("Error: Input directory does not exist.")  # Print error if directory doesn't exist
        return

    os.makedirs(output_directory, exist_ok=True)  # Create output directory if it doesn't exist

    # Iterate over files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a text file
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_directory, filename)  # Create full file path
            output_file_path = os.path.join(output_directory, filename.replace(".txt", ".pdf"))  # Define output PDF path
            try:
                pdf = FPDF()  # Create a PDF object directly from FPDF
                pdf.add_page()  # Add a new page to the PDF
                pdf.set_font("Arial", size=12)  # Set font style and size for the PDF

                with open(input_file_path, 'r', encoding='utf-8') as file:  # Open the text file
                    for line in file:  # Iterate through each line in the file
                        pdf.multi_cell(0, 10, line)  # Write the line to the PDF

                pdf.output(output_file_path)  # Save the PDF to the output path
                print(f"Converted '{filename}' to PDF successfully.")  # Print success message
            except (IOError, ValueError) as e:
                print(f"Error: Failed to convert '{filename}': {e}")  # Print error if conversion fails
            except Exception as e:
                print(f"Error: Unexpected error while converting '{filename}': {e}")  # Print unexpected errors

def convert_word_to_pdf(input_directory, output_directory):
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print("Error: Input directory does not exist.")  # Print error if directory doesn't exist
        return
    
    os.makedirs(output_directory, exist_ok=True)  # Create output directory if it doesn't exist

    # Iterate over files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a Word document
        if filename.endswith(".docx"):
            input_file_path = os.path.join(input_directory, filename)  # Create full file path
            output_file_path = os.path.join(output_directory, filename.replace(".docx", ".pdf"))  # Define output PDF path
            print(f"Attempting to convert: {input_file_path}")  # Print the conversion attempt
            try:
                convert(input_file_path, output_file_path)  # Convert the Word file to PDF
                print(f"Converted '{filename}' to PDF successfully.")  # Print success message
            except FileNotFoundError as e:
                print(f"Error: File not found: {e}")  # Print error if the file is not found
            except Exception as e:
                print(f"Error: Failed to convert '{filename}': {e}")  # Print other errors

def main():
    input_directory = "Simple PDF Generator/input_files"  # Define input directory for files
    output_directory = "Simple PDF Generator/output_files"  # Define output directory for PDFs

    # Convert images to PDF
    convert_images_to_pdf(input_directory, os.path.join(output_directory, "images_output.pdf"))
    # Convert text files to PDF
    convert_text_to_pdf(input_directory, output_directory)
    # Convert Word documents to PDF
    convert_word_to_pdf(input_directory, output_directory)

if __name__ == "__main__":
    main()  # Run the main function
