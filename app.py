from selenium import webdriver
from openai import OpenAI
import base64 
from dotenv import load_dotenv
import os 

# load secret api key defined in environment variable
load_dotenv()

# initialize the chrome webdriver
driver = webdriver.Chrome()

#open the webpage
driver.get('https://www.linkedin.com/in/bigyan-bhatta-48493a230/')

# taking screenshot of the webpage
driver.save_screenshot('linkedin-profile.png')

driver.quit()

client = OpenAI()
def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
base64_image = encode_image('linkedin-profile.png')

response = client.chat.completions.create(
    model = 'gpt-4o',
    messages= [
        {
            'role': "system",
            "content": [
                {
                    "type": "text",

                        'text': """
                        You are a headhunter for a CTO position.
                        Please extract the most important facts about the candidate.

                        Respond in JSON format.
                    """
                }    
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64, {base64_image}"
                    }
                }
            ]
        },
        {
            "role": 'assistant',
            "content": [
                {
                    "type": "text",
                    "text": "Here are some observations and recommendations to enhance conversation rates on this webpage: \n\n"
                }
            ]
        }
    ],
    temperature= 1, 
    max_tokens= 256, 
    top_p= 1,
    frequency_penalty= 0,
    presence_penalty= 0
)

print(response.choices[0].message.content)