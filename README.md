# Webage-scraping-Linkedin-headhunter

This repository contains a Python script that automates the process of scraping LinkedIn profiles, taking screenshots, and extracting relevant candidate information using OpenAI's GPT-4 model. The script is designed for headhunters who need to quickly gather and analyze information about potential candidates for CTO positions.

## Features

- Automates the process of opening LinkedIn profiles.
- Takes a screenshot of the LinkedIn profile page.
- Encodes the screenshot in base64 format.
- Uses OpenAI's GPT-4 model to extract key information from the screenshot.
- Outputs the extracted information in JSON format.

## Requirements

- Python 3.6+
- Selenium
- OpenAI API key
- dotenv

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Webage-scraping-Linkedin-headhunter.git
   cd Webage-scraping-Linkedin-headhunter

2. **Install the required python packages:**
    ```sh
    pip install -r requirements.txt

3. **Set up environment variables:**
    ```sh
    Create a .env file in the root directory of the project and add your OpenAI API key:
    OPENAI_API_KEY=your_openai_api_key

## Usage
Run the script:
```sh
run app.py
```
app.py: The main script file that contains the following functions:
- screenshot_linkedin_profile(profile_url): Opens the LinkedIn profile URL and takes a screenshot.
- encode_image(image_path): Encodes the screenshot to base64 format.
- extract_candidate_info(api_key, base64_image): Sends the base64 image to OpenAI's GPT-4 model and extracts candidate information.
- main(profile_url): Main function to orchestrate the scraping, encoding, and information extraction process.

## Example
```sh
Enter the LinkedIn profile URL: https://www.linkedin.com/in/example-profile/
{
  "name": "Example Name",
  "headline": "CTO at Example Company",
  "experience": [
    {
      "title": "Chief Technology Officer",
      "company": "Example Company",
      "duration": "3 years"
    },
    {
      "title": "Senior Developer",
      "company": "Another Company",
      "duration": "5 years"
    }
  ],
  "education": [
    {
      "degree": "BSc in Computer Science",
      "institution": "Example University",
      "year": "2010"
    }
  ]
}
```
