# AcademicJobToolkit

AcademicJobToolkit is a Python and LaTeX-based project designed to assist in preparing and organizing academic job application documents. It simplifies splitting a single PDF containing multiple sections (e.g., Cover Letter, Research Statement, Teaching Statement, Diversity Statement, and References) into separate PDFs for each section, ensuring a streamlined and efficient job application process.

![jobsearch_over](https://github.com/iamgmujtaba/AcademicJobToolkit/assets/33286377/27f0f39b-a60b-4f39-bedf-86437b17911b)

### Features
- LaTeX Project Structure: Organized template for compiling academic job application documents.
- PDF Splitting: Python script to split the compiled PDF into individual sections.
- Customizable: Easily modify the LaTeX templates and Python script to fit different job applications.


### Prerequisites
- Python 3.x
- PyPDF2 library
- LaTeX distribution (Overleaf recommended)

### Installation
- Clone the repository:

``` bash
git clone https://github.com/iamgmujtaba/AcademicJobToolkit.git
cd AcademicJobToolkit
```
- Install the required Python packages:

```bash
pip install PyPDF2
```

### Installation and Usage
- LaTeX Project: Edit the provided LaTeX section files to include your content.
- Python Script: Use the Python script to split the compiled PDF into separate files for each section.
- Compilation: Compile the LaTeX project using a LaTeX editor or Overleaf (highly recommended).


### Directory Structure

```
job-toolkit
│
├── main.tex
├── resume.sty
├── bibliography.bib
├── sections
│   ├── cover_letter.tex
│   ├── research_statement.tex
│   ├── teaching_statement.tex
│   ├── diversity_statement.tex
│   ├── references.tex
└── split_pdf.py
└── README.md
```

### File Descriptions
- `main.tex`: Main LaTeX file that combines all sections
- `resume.sty`: Custom style file for LaTeX
- `bibliography.bib`: BibTeX file for references
- `split_pdf.py`: Python script to split the compiled PDF


### Usage
1. Prepare your LaTeX project, which is compiled into a single PDF file containing all sections of your job application. The LaTeX project should be structured with \newpage between sections to ensure each section starts on a new page.

2. Save the compiled PDF in the project directory as CS_JobSearch.pdf (or any name you prefer).

3. Update the sections list in the Python script to match the structure of your PDF. Each section should have the name, starting page, and ending page.

4. Run the Python script to split the PDF into individual sections:

```bash
python split_pdf.py
```

5. The script will create a jobApp directory and save each section as a separate PDF file within this directory. After splitting, the original PDF file will be deleted.
![jobsearch_cmd](https://github.com/iamgmujtaba/AcademicJobToolkit/assets/33286377/f0bf9b06-cc86-40c0-bd8a-02b64941564a)

### Output
After running the script, your jobApp directory will contain files like:
- Cover_Letter.pdf
- Research_Statement.pdf
- Teaching_Statement.pdf
- Diversity_Statement.pdf
- References.pdf

### Troubleshooting
If you encounter any issues, please check the following:
- Ensure all LaTeX packages are installed
- Verify that PyPDF2 is correctly installed
- Check that the PDF file name in the Python script matches your compiled PDF

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Reporting Issues
If you encounter any bugs or have feature requests, please file an issue on the [GitHub issue tracker](https://github.com/iamgmujtaba/AcademicJobToolkit/issues).
