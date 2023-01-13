import os
import requests
from bs4 import BeautifulSoup

url = 'https://ln.hako.vn/truyen/8534-my-plain-looking-fiancee-is-secretly-sweet-with-me/c75491-minh-hoa'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text from the website
# text = soup.get_text()
content = soup.select_one("#chapter-content")
text = content.get_text()


# Create a new text file and write the text to the file
with open('content.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Find all the img elements
img_elements = soup.find_all('img')

# Create a new folder to store the images
if not os.path.exists('images'):
    os.makedirs('images')

# Download each image
for i, img in enumerate(img_elements):
    img_url = img.get('src')
    img_data = requests.get(img_url).content

    # Write the image data to a file
    with open('images/img{}.jpg'.format(i), 'wb') as handler:
        handler.write(img_data)
