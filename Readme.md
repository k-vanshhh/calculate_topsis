
# TOPSIS Web Application

## Overview

The **TOPSIS Web Application** is a web-based platform built using Flask that implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method. TOPSIS is a multi-criteria decision analysis (MCDA) technique used to rank and select alternatives based on a set of criteria. This application allows users to upload data in CSV format, performs the TOPSIS calculation, and provides the results in an Excel file that can be downloaded.

### Features

- **CSV File Upload**: Users can upload a CSV file containing data for analysis.
- **TOPSIS Calculation**: The application performs the TOPSIS method on the provided data.
- **Excel Export**: After calculating the results, the app generates an Excel file with the ranking and score.
- **Easy to Use**: The user interface allows easy interaction with the application.

## Project Setup

### Prerequisites

Before running the application, you must have the following installed on your machine:

- **Python 3.x**: Make sure you have Python installed. You can check this by running `python --version` or `python3 --version` in the terminal.
- **pip**: Python's package installer to install dependencies.

### Installing Dependencies

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:
   First, clone the project repository to your local machine. Use the following command in the terminal:
   
   ```bash
   git clone https://github.com/k-vanshhh/topsis-cal-webpage
   ```

2. **Navigate to Project Directory**:
   Change your working directory to the project folder:
   
   ```bash
   cd topsis-cal-webpage
   ```

3. **Install Dependencies**:
   Install the required Python packages using `pip` by running:
   
   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary libraries, such as Flask, pandas, and other dependencies listed in `requirements.txt`.


## How to Run Locally

### Step-by-Step Guide

1. **Install Dependencies**:
   Ensure that all dependencies are installed:
   
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Flask Application**:
   Run the Flask application locally by executing the following command:
   
   ```bash
   python app.py
   ```

   By default, Flask will run on `http://127.0.0.1:5000/`.

3. **Access the Web Application**:
   Open a web browser and go to `http://127.0.0.1:5000/`. You should see the home page of the application, where you can upload the CSV file for analysis.

### Uploading Data

The web app expects a CSV file with the following structure:

- **Column 1**: `Fund Name` (or any identifier for each row/option)
- **Column 2 and onward**: The criteria for evaluating each option (e.g., P1, P2, P3, etc.)

Here is an example of what the CSV data might look like:

```csv
Fund Name,P1,P2,P3,P4,P5
Fund 1,0.8,0.7,0.6,0.9,0.5
Fund 2,0.7,0.8,0.6,0.8,0.6
Fund 3,0.6,0.6,0.8,0.7,0.7
```

### Running the TOPSIS Calculation

1. Upload the CSV file containing your data.
2. Select the criteria for weights and impacts, if applicable.
3. Click on the **Calculate** button to perform the TOPSIS analysis.
4. The app will process the data and generate a ranking for each option based on the TOPSIS method.
5. Download the results in an Excel format containing the calculated rankings and scores.

## Usage

1. Visit the web application at the provided URL.
2. Upload a CSV file with the required data (Fund names and criteria).
3. Select the relevant weights and impacts (if applicable).
4. Click **Calculate** to generate the TOPSIS results.
5. Download the results as an Excel file.

## Contributing

We welcome contributions! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

### How to Contribute

- **Report Issues**: If you find a bug or issue, please open an issue on the GitHub repository.
- **Enhancements**: Suggest features or improvements by opening a new issue or pull request.


## Acknowledgments

- **Flask**: A lightweight web framework for Python used to build the web application.
- **pandas**: A powerful data manipulation library used for handling and processing CSV data.
- **NumPy**: A package used for numerical computations, used in the implementation of TOPSIS.
- **TOPSIS Method**: A well-known multi-criteria decision analysis method for ranking and selecting alternatives.

---

Feel free to explore, improve, and contribute to this project!
