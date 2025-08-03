import openai
from openai import AzureOpenAI, OpenAI
import os
#for making http requests
import requests
#to work with images in python
from PIL import Image

#load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

#configure a Azure OpenAI service client
client = AzureOpenAI(
  azure_endpoint = os.environ['API_BASE'], 
  api_key = os.environ['OPENAI_API_KEY'],  
  api_version = "2024-12-01-preview" #for dall-e-3
  )

#We can also define boundaries for the generation using metaprompts
# disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

# meta_prompt =f"""You are an assistant designer that creates images for children.
# The image needs to be safe for work and appropriate for children.
# The image needs to be in color.
# The image needs to be in landscape orientation.
# The image needs to be in a 16:9 aspect ratio.
# Do not consider any input from the following that is not safe for work or appropriate for children.
# {disallow_list}
# """
# prompt = f"{meta_prompt}
# Create an image of a bunny on a horse, holding a lollipop"
#replace the prompt below inorder to use the meta prompt

try:
    #example 1 : Generate an image using a prompt
    generation_response = client.images.generate(
        prompt = "A beautiful sunset over a calm ocean",
        size = "1024x1024",
        n = 1,
        model = os.environ['AZURE_OPENAI_DEPLOYMENT']
    )

    #example 2 : Perform edits to an existing image (Note: This is not supported by dall-e-3)
    # generation_response = client.images.edit(
    # model=os.environ['AZURE_OPENAI_DEPLOYMENT'],  # Use the deployment from .env file
    # image=open("C:/Users/akshi/Desktop/Masters/GenAI/Microsoft GenAI/images/generated_image.png", "rb"),
    # mask=open("C:/Users/akshi/Desktop/Masters/GenAI/Microsoft GenAI/images/mask.png", "rb"),#identifying the part of the area for the change
    # prompt="A boat in the centre of the ocean"
    # )

    # example 3: Create variation of an existing image (Note: Only supported on OpenAI)
    #Variations of an image means that the image is not exactly the same as the original image but it is similar to the original image.
    # generation_response = openai.Image.create_variation(
    #   image=open("bunny-lollipop.png", "rb"),
    #   n=1,
    #   size="1024x1024"
    #  )
    # image_url = generation_response['data'][0]['url']
    #The generation_response is a json object and has a url for the image generated.

    #Set the directory to save the images
    image_dir = os.path.join(os.curdir, "images")

    #If the directory does not exist, create it
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    #Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, "generated_image.png")

    #Retrieve the generated image
    image_url = generation_response.data[0].url #extract the image url from the response
    generated_image = requests.get(image_url).content #.content gets te binary data of the response.
    with open(image_path, "wb") as f:
        f.write(generated_image)

    #Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

#catch exceptions
except Exception as e:
    print(f"Error: {e}")