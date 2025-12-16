# Columbus, Ohio Weather in Practice

## Project Name and Team Members

**Project Name:** Columbus, Ohio Weather in Practice  
**Team Member:** Yao Lin

## Project Overview

This project provides an analysis of the climatological data for Columbus, Ohio from July to November 2025. It focuses on understanding the temperature trends, precipitation patterns, and heating/cooling demands during the fall transition. The analysis is carried out using daily weather data, including temperature, precipitation, snow, and heating/cooling degree days (HDD/CDD). 

## Project Setup Instructions

### Step 1: Create a Virtual Environment

To isolate the project’s dependencies, create a virtual environment by following these steps:

1. **Install `virtualenv` if not already installed**:
    ```bash
    pip install virtualenv
    ```

2. **Create the virtual environment**:
    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

### Step 2: Install Dependencies

Once the virtual environment is activated, install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Scripts

There are two main Python scripts to run:

clean_data.py: This script loads the raw climatological data, merges the data for July to November 2025, and saves the cleaned data to a CSV file.

Run this script using:

python clean_data.py


daily_data.py: This script reads the cleaned data, performs analysis on daily temperature and precipitation data, and generates visualizations (temperature trends, precipitation distribution, HDD/CDD calculations). The output includes the saved plots in PNG format.

Run this script using:

python daily_data.py


