```
# Web Content to Word Document Project

This project uses Python to transfer all content (headings and paragraphs) from a website to a Word document.

## Requirements
----------------->
- Python 3.x
- pip
```
## Step 1: Create Project Directory

Create a directory for the project and navigate into it:

```sh
mkdir web_to_word
cd web_to_word
```

## Step 2: Create Virtual Environment

Create and activate a virtual environment:

- Windows:

  ```sh
  python -m venv venv
  .\venv\Scripts\activate
  ```

- MacOS/Linux:

  ```sh
  python -m venv venv
  source venv/bin/activate
  ```

## Step 3: Install Required Libraries

Install the necessary Python libraries:

```sh
pip install requests beautifulsoup4 python-docx
```

## Step 4: Write Python Code

## Step 5: Run the Code

Run the code using the terminal or command prompt:

```sh
python web_to_word.py
```
Enter the URL of the website: "https://example.com"
Enter the name of the Word file to be saved (e.g. output.docx): "output.docx"


Once this process is complete, a file named `website_content.docx` will be created in the `web_to_word` directory. This file will contain the headings and paragraphs from the specified website.

## Check the Results

Open the generated Word document to verify the content. Ensure that all the headings and paragraphs from the website have been correctly transferred to the document.

## Additional Features

If you want to include other types of content (images, lists, etc.), you can update the Python code accordingly.

