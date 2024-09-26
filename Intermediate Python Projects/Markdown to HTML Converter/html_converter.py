# 25.  Markdown to HTML Converter   
#     *Description*: Write a program that converts simple Markdown syntax into HTML.  
#     *Skills*: File handling, string manipulation, regular expressions.

import re

class MarkdownConverter:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text
    
    def convert_headers(self):
        # Convert Markdown headers to HTML
        self.markdown_text = re.sub(r'^(#{1,6})\s*(.+)', self.header_replacer, self.markdown_text, flags=re.MULTILINE)
    
    def header_replacer(self, match):
        level = len(match.group(1))  # Determine header level based on number of '#' characters
        return f"<h{level}>{match.group(2)}</h{level}>"
    
    def convert_bold(self):
        # Convert bold text
        self.markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', self.markdown_text)
        self.markdown_text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', self.markdown_text)
    
    def convert_italic(self):
        # Convert italic text
        self.markdown_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', self.markdown_text)
        self.markdown_text = re.sub(r'_(.+?)_', r'<em>\1</em>', self.markdown_text)
    
    def convert_links(self):
        # Convert links
        self.markdown_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', self.markdown_text)
    
    def convert_images(self):
        # Convert images
        self.markdown_text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', self.markdown_text)
    
    def convert_lists(self):
        # Convert unordered lists
        self.markdown_text = re.sub(r'^\s*-\s*(.+)', r'<li>\1</li>', self.markdown_text, flags=re.MULTILINE)
        self.markdown_text = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', self.markdown_text, flags=re.DOTALL)

        # Convert ordered lists
        self.markdown_text = re.sub(r'^\s*\d+\.\s*(.+)', r'<li>\1</li>', self.markdown_text, flags=re.MULTILINE)
        self.markdown_text = re.sub(r'(<li>.*?</li>)', r'<ol>\1</ol>', self.markdown_text, flags=re.DOTALL)

    def convert(self):
        self.convert_headers()
        self.convert_bold()
        self.convert_italic()
        self.convert_links()
        self.convert_images()
        self.convert_lists()
        return self.markdown_text

def main():
    # Read Markdown input from a file
    input_file = 'Markdown to HTML Converter/markdown.md'
    output_file = 'Markdown to HTML Converter/output.html'
    
    try:
        with open(input_file, 'r') as file:
            markdown_text = file.read()

        # Create an instance of MarkdownConverter
        converter = MarkdownConverter(markdown_text)
        
        # Convert Markdown to HTML
        html_output = converter.convert()
        
        # Write the HTML output to a file
        with open(output_file, 'w') as file:
            file.write(html_output)
        
        print(f"Markdown has been converted to HTML and saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
