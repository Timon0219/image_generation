import os
from gradio_client import Client

async def image_generator(prompt: str):
    client = Client("ADOPLE/Text_To_Image")
    image = client.predict(
    prompt,
    api_name="/text_to_image"
    )
    return image