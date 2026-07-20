# Resume Screening and Candidate Ranking System

This is a Python project made for my machine learning mini-project submission. It takes candidate resumes, cleans the text using NLP steps, and matches them against job requirements to rank who fits best. It runs as a local web app in the browser.

## Project Structure
* `nlp_cleaner.py` - Contains the text cleaning code (lowercasing, removing punctuation, and stemming).
* `train_model.py` - Reads the main dataset file, extracts the text features, and saves them.
* `app.py` - The Streamlit code that creates the frontend web app interface.
* `vocab.txt` - Text file containing the words learned from the training data.
* `classes.txt` - Text file containing the job category list.

## App Interface Preview
Here is how the system looks and works when running in the browser:

![Main Web Interface](screenshot1.png)

*Note: You can replace 'screenshot1.png' with your actual web app image file name.*

## How to Set Up and Run This Project

### 1. Install Libraries
Open your terminal and run this command to install the required Python packages:
```bash
pip install pandas nltk scikit-learn streamlit
```

### 2. Generate Text Parameters
Run the training script once to read the data rows and create the text vocabulary files:
```bash
python train_model.py
```

### 3. Start the Web App
Run this command to fire up the Streamlit server and automatically open the website in your browser:
```bash
python -m streamlit run app.py
```
