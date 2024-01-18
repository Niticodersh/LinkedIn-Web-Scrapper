# LinkedIn Web Scraping with Streamlit

This project demonstrates web scraping of LinkedIn profiles using Streamlit. Users can input LinkedIn credentials, upload a text file containing LinkedIn profile URLs, and get a downloadable JSON file with scraped profile data.

## Profile Data Includes:

1. **Profile Picture URL:** URL of the user's profile picture.

2. **Name:** The name of the LinkedIn user.

3. **Connections:** The number of connections the user has.

4. **Summary/About:** A brief summary or description provided by the user about themselves.

5. **Education:** Details about the user's educational background, including the institution, degree, and time period.

6. **Skills:** A list of skills associated with the user.

These details may vary depending on the structure of the LinkedIn profiles and the specific information available on each profile. The web scraping script extracts these elements from the HTML source of the LinkedIn profiles.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (>=3.6)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Niticodersh/LinkedIn-Web-Scrapper.git

    ```

2. **Change into the project directory:**

    ```bash
    cd LinkedIn-Web-Scrapper
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download and install ChromeDriver. Ensure the path to ChromeDriver is in your system's PATH.**

## Usage

- Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

- Open your browser and go to the provided URL (usually http://localhost:8501).

- Enter your LinkedIn credentials in the sidebar.

- Upload a text file containing LinkedIn profile URLs.

- Click the "Process JSON" button to initiate scraping.

- Download the processed JSON file.

## File Structure

- `webdriver_setup.py`: Module for setting up Selenium WebDriver.
- `login.py`: Module for logging in to LinkedIn.
- `scrape_profile.py`: Module for scraping LinkedIn profile data.
- `app.py`: Main Streamlit app.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
