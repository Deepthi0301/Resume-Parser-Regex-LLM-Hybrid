# Resume Parser Using Regex, LLM, and Hybrid Approach

A Python-based resume parser that extracts important candidate information from PDF, DOCX, and ODT files using three approaches: Regular Expressions (Regex), a Large Language Model (LLM), and a Hybrid approach. The extracted information is saved in structured JSON format.

## Project Overview

Manually collecting candidate information from resumes can be time-consuming. This project automates the extraction process by identifying important details such as contact information, technical skills, education, work experience, projects, and certifications.

The project implements three different parsing approaches to explore rule-based extraction, AI-powered extraction, and a combination of both.

## Features

- Supports PDF, DOCX, and ODT resume formats.
- Extracts candidate names, email addresses, and phone numbers.
- Identifies technical skills using predefined patterns.
- Extracts education, work experience, projects, and certifications.
- Provides three parsing approaches: Regex, LLM, and Hybrid.
- Generates structured JSON output.
- Handles missing information and unsupported file formats.
- Uses a local language model through Ollama for AI-based extraction.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Regular Expressions (`re`) | Pattern-based information extraction |
| PyMuPDF (`fitz`) | Reading PDF files |
| python-docx | Reading Word documents |
| odfpy | Reading ODT files |
| Ollama | Running the language model locally |
| Llama 3.2 1B | AI-based resume information extraction |
| JSON | Storing extracted information |

## Project Structure

```text
Resume-Parser-Regex-LLM-Hybrid/
├── regex_parser.py
├── llm_parser.py
├── hybrid_parser.py
├── sample_resumes/
│   ├── sample_resume.pdf
│   ├── incomplete.docx
│   └── test.txt
├── output/
│   └── generated JSON files
├── README.md
└── .gitignore
```

The output files are generated when the parsers are executed. The exact filenames depend on the input resume and the script being used.

## Parsing Approaches

### 1. Regex-Based Parser

The Regex parser uses predefined rules and regular expressions to identify information in resume text.

**How it works:**
1. Extracts text from the input resume.
2. Searches for email addresses and phone numbers.
3. Identifies technical skills using a predefined skills list.
4. Extracts information under recognized resume section headings.
5. Saves the extracted information as JSON.

**Advantages:** Fast, straightforward, and suitable for recognizable text patterns.

**Limitation:** Depends on predefined patterns and may struggle with unfamiliar layouts or wording.

### 2. LLM-Based Parser

The LLM parser uses the Llama 3.2 1B model through Ollama to interpret resume content and organize it into structured fields.

**How it works:**
1. Extracts text from the resume.
2. Sends the text to the local language model with extraction instructions.
3. Requests structured JSON output.
4. Processes the model's response and uses fallback extraction for selected missing fields.
5. Saves the result as JSON.

**Advantages:** Can interpret context and organize information more flexibly than fixed rules.

**Limitation:** AI-generated results may be incomplete or inaccurate and should be checked.

### 3. Hybrid Parser

The Hybrid parser combines Regex and LLM extraction to use the strengths of both approaches.

**How it works:**
1. Extracts text from the resume.
2. Runs both the Regex and LLM parsers.
3. Prioritizes Regex results for email addresses and phone numbers.
4. Uses the LLM result for other configured fields when a usable value is available.
5. Falls back to Regex results when the LLM result is missing or empty.
6. Saves the combined information as JSON.

**Advantages:** Combines pattern-based extraction with AI-based interpretation.

**Limitation:** The final accuracy depends on the quality of both extraction methods and the selection rules.

## Information Extracted

The parser is designed to extract the following fields:

- Full Name
- Email Address
- Phone Number
- Technical Skills
- Educational Qualifications
- Work Experience
- Projects
- Certifications

Missing fields may be represented as `null`, empty strings, or empty lists, depending on the field and parser.

## Installation and Setup

### Prerequisites

- Python 3.11 or a compatible version
- Ollama installed on your computer
- The Llama 3.2 1B model for LLM and Hybrid parsing

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Resume-Parser-Regex-LLM-Hybrid.git
cd Resume-Parser-Regex-LLM-Hybrid
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install Python Dependencies

```bash
python -m pip install pymupdf python-docx odfpy
```

### 3. Set Up Ollama

Install Ollama from https://ollama.com/ and download the model:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama and the model are available before running the LLM or Hybrid parser.

## How to Run

Run the commands from the project directory.

### Regex Parser

```bash
python regex_parser.py sample_resumes/sample_resume.pdf
```

### LLM Parser

```bash
python llm_parser.py sample_resumes/sample_resume.pdf
```

### Hybrid Parser

```bash
python hybrid_parser.py sample_resumes/sample_resume.pdf
```

You can replace the sample PDF path with another supported resume file, such as:

```text
sample_resumes/incomplete.docx
```

The scripts print the extracted information and save JSON results in the output directory.

## Testing

The project was tested with:

- A complete sample PDF resume.
- An incomplete DOCX resume with some fields missing.
- An unsupported TXT file to verify format validation.
- All three parsing approaches to check extraction and JSON generation.

These tests verify the basic workflow for the tested files. Results may vary with different resume layouts and content.

## Error Handling

The project includes handling for common issues:

- Resume file not found.
- Unsupported file formats.
- Empty extracted text.
- Missing resume information.
- Unexpected parsing errors.

## Future Enhancements

- Improve extraction accuracy for different resume layouts.
- Expand technical skill recognition.
- Convert education and work experience into more detailed structured fields.
- Add batch processing for multiple resumes.
- Build a web interface for resume uploads.
- Store candidate details in a database.
- Add job-description matching and skill comparison.
- Evaluate extraction accuracy against manually verified results.

## Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and file handling.
- Regular expressions and text processing.
- Extracting text from different document formats.
- JSON serialization and structured data.
- Integrating a locally running language model.
- Prompt-based information extraction.
- Combining rule-based and AI-based methods.
- Testing, debugging, and error handling.

## Conclusion

This project demonstrates how resume information can be extracted using rule-based, AI-based, and hybrid approaches. It provides a foundation for further development into resume-processing and recruitment-support applications.

**Project Type:** Python | Natural Language Processing | Local LLM | Information Extraction
