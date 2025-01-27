## Project Overview

This project involves processing historical quiz data, fetching data from APIs, and performing various data cleaning, transformation, and analysis tasks. The data is then presented through interactive visualizations and served via a Flask API. The API allows users to upload quiz data and receive analysis results, including performance metrics and suggestions for revision based on incorrect answers.

## Approach Description

1. **Data Collection:**
   - Data is fetched from multiple API URLs, and each response is saved as a JSON file.
   - The data is then processed by converting it into a structured format (CSV or Excel).
   
2. **Data Preprocessing:**
   - Historical data is cleaned, null values are handled, and categorical, numerical, and date columns are segregated for easier analysis.
   - Duplicate entries are removed, and column names are standardized.
   
3. **Historical Data Analysis:**
   - The quiz data is grouped by quiz ID or topic, and various metrics such as total questions, correct answers, and incorrect answers are calculated.
   - Anomalies and trends are visualized in bar charts for better insight into quiz performance.

4. **Flask API:**
   - A Flask-based API serves the processed data and allows for interaction, including uploading student quiz data for further processing.
   - The API provides a recommendation system to guide students on questions to revise based on their performance.

5. **Visualization:**
   - Matplotlib is used to generate various performance visualizations based on quiz data.

---

## Setup Instructions

### Prerequisites
Ensure the following dependencies are installed on your system:

1. **Python 3.x**
2. **Pip** (Python package installer)
3. **Docker** (if running inside a container)
4. **Flask**: `pip install flask`
5. **pandas**: `pip install pandas`
6. **matplotlib**: `pip install matplotlib`
7. **requests**: `pip install requests`

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo-url.git
cd your-repo-directory
```
### 2. Install Dependencies
If you haven’t installed the dependencies already, run:
```bash
pip install -r requirements.txt
```
### 3. Running the Flask Application
To run the Flask application locally, use the following command:

```bash
python app.py
```
The Flask app will run on `http://127.0.0.1:5000/`.

### 4. Testing the API
After starting the Flask application, you can test it using tools like curl, Postman, or directly through your browser.
Below is the curl command that you can run in command promt.
```bash
curl -X POST -F "student_data=@student_data.json" http://localhost:5000/upload-student-data
```
This will upload a JSON file containing student data for analysis and give recommendations on where to improve

## Conclusion
This project demonstrates a complete pipeline for handling, analyzing, and serving quiz data. The Flask API provides a simple yet effective way to upload data and receive recommendations, making it useful for both educators and students.
