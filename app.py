import streamlit as st
from webdriver_setup import get_driver
from login import login_to_linkedIn
from scrape_profile import scrape_linkedin_profiles
import json


def process_file(file_contents, driver):
    linkedin_urls = file_contents.splitlines()

    all_profiles_data = []

    for url in linkedin_urls:
        profile_data = scrape_linkedin_profiles(driver, url)
        all_profiles_data.append(profile_data)

    return all_profiles_data


def main():
    st.title("LinkedIn Web Scraping")
    process = 0
    st.sidebar.header("Enter your LinkedIn Credentials")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Create a button to login
    if st.button("Login"):
        # Display a loading spinner
        spinner = st.empty()
        spinner.text("Logging in...")

        # Attempt to log in
        driver = get_driver()
        if login_to_linkedIn(driver, username, password):
            spinner.text("Login successful!")

            # Enable the scraping button
            if st.button("Process JSON") and process == 0:
                process = 1
                spinner.text("Fetching data...")

                # Process and download JSON
                all_profiles_data = process_file(file_contents, driver)
                output_file_path = "output.json"

                with open(output_file_path, "w") as json_file:
                    json.dump(all_profiles_data, json_file, indent=2)

                spinner.text("Data fetched successfully!")
                process = 0

                # Provide download button for the JSON file
                download_button = st.download_button(
                    label="Download JSON",
                    data=open(output_file_path, "rb").read(),
                    key="download_button",
                    file_name="output.json",
                    mime="application/json",
                )

                st.markdown("Click the button above to download the processed JSON file.")

            # Quit the driver after scraping
            driver.quit()


if __name__ == "__main__":
    main()
