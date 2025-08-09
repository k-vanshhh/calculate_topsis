

# TOPSIS Web Application

## Overview

The **TOPSIS Web Application** is a web-based platform built using Flask that implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method. TOPSIS is a multi-criteria decision analysis (MCDA) technique used to rank and select alternatives based on a set of criteria. This application allows users to upload data in CSV format, performs the TOPSIS calculation, and provides the results in an Excel file that can be downloaded.

### Features

- **CSV File Upload**: Users can upload a CSV file containing data for analysis.
- **TOPSIS Calculation**: The application performs the TOPSIS method on the provided data.
- **Excel Export**: After calculating the results, the app generates an Excel file with the ranking and score.
- **Easy to Use**: The user interface allows easy interaction with the application.

---

## Screenshots

### 1. **Home Page**
This is the landing page where users can upload their CSV file, enter weights and impacts, and submit the form.

![Home Page](/screenshots/image.png)

---

### 2. **Results Page**
After processing the uploaded data, the application displays a confirmation message and provides an Excel file for download.

![Results Page](/screenshots/2.png)

---

## Project Setup

### Prerequisites

Before running the application, you must have the following installed on your machine:

- **Python 3.x**: Make sure you have Python installed. You can check this by running `python --version` or `python3 --version` in the terminal.
- **pip**: Python's package installer to install dependencies.

---

### Installing Dependencies

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/k-vanshhh/calculate_topsis
   ```

2. **Navigate to Project Directory**:
   ```bash
   cd calculate_topsis
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

### Running the Application

1. **Start the Flask Server**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open `http://127.0.0.1:5000/` in your browser to start using the TOPSIS web application.

---

## How to Contribute

We welcome contributions! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## Acknowledgments

- **Flask**: A lightweight web framework for Python used to build the web application.
- **pandas**: A powerful data manipulation library used for handling and processing CSV data.
- **NumPy**: A package used for numerical computations, used in the implementation of TOPSIS.
- **TOPSIS Method**: A well-known multi-criteria decision analysis method for ranking and selecting alternatives.
