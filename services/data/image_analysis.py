import base64
import os
from openai import OpenAI
from services.data.page_extraction import extract_random_pages_as_images, get_mode
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# Function to encode the image


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def image_analysis(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert at analysing images, and classifying them as lattice if the tables have welldefined and visible border else stream. only output with one word lattice or stream",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )

    if "lattice" in response.choices[0].message.content:
        return "lattice"
    else:
        return "stream"


def analyse_pdf(pdf_path: str):

    output_path = Path(f'outputs/pdf_images')
    output_path.mkdir(parents=True, exist_ok=True)

    extract_random_pages_as_images(pdf_path, output_path, num_pages=5)

    image_types = []

    for filename in output_path.glob('*'):
        image_types.append(image_analysis(str(filename)))

    return get_mode(image_types)[0]
