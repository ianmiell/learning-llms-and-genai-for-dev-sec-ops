from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI

import os
llm = AzureChatOpenAI(
    deployment_name=os.environ['AZURE_VISION_DEPLOYMENT'],  #  alias `azure_deployment`
    model_name="gpt-4-vision-preview",
    api_key=os.environ['AZURE_OPENAI_API_KEY'],
    azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'],
    max_tokens=2000,
    temperature=0
)

import base64

# Convert the image to base64 format
with open("data/hotdog.jpg", "rb") as f:
    encoded_image = base64.b64encode(f.read())

content = [
    {
        "type": "text",
        "text": "What's in this image?",
    },
    {
        "type": "image_url",
        "image_url": {
            "url": "data:image/jpeg;base64," + encoded_image.decode("utf-8"),
        },
    },
]

from langchain.schema import HumanMessage

msg = HumanMessage(content=content)
print(llm.invoke([msg]))


with open("data/screenshot.jpg", "rb") as f:
    encoded_image = base64.b64encode(f.read())

content = [
    {
        "type": "text",
        "text": "What are all the areas that I can click ? And list them in a table together with a name, a description, and their x,y coordinates on the page",
    },
    {
        "type": "image_url",
        "image_url": {
            "url": "data:image/jpeg;base64," + encoded_image.decode("utf-8"),
        },
    },
]

msg = HumanMessage(content=content)
print(llm.invoke([msg]).content)


