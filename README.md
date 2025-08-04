# Image Generation Application Using Azure AI

A simple application showcasing how to generate images using Dall-E model. 

## 📚 Overview
This repository contains :
- .py file with example codes:
   - to generate images by passing prompts to the Dall-E model.
   - defining boundaries for image generation using metaprompts.
   - performing edits to an existing image (not supported by Dall-E)
   - creating variation of an existing image using OpenAI
- .env_example file (for environment variables)
- requirements.txt file (with required packages)

## 🚀 Azure Resource Setup
Note: Active Azure subscription is required.
**1. Create a Azure OpenAI Resource**
- Go to Azure Portal : https://portal.azure.com
- Search **Azure OpenAI** in search bar.
- Click **Create**.
- Choose the **Subscription**
- Create or Select an existing **Resource Group**.
- Choose one of the supported **Regions** (e.g. East US)
- Give a Unique name for the resource.
- Review the details and Create the resource.

**2. Deploy a Model**
Once the resource is created:
- Open the created the resource.
- Click on **Explore and Deploy**.
- Create a new deployment and choose either base model or fine-tuned model.
- Select a model:
        - Model : Choose o3-mini or gpt-4 (choose model according to your application)
        - Deployment name : e.g., text-gen-model.
        - Version : Choose default or latest.

**3. Get Endpoints and Keys**
- In the resource’s left menu, click Keys and Endpoint.
- Copy the following:
   - Endpoint (e.g., https://your-resource-name.openai.azure.com/)
   - API Key 1 or API Key 2.


## 🛠 Installation & Setup
**1. Clone the repository**
```bash 
git clone https://github.com/Your-Profile/Your-Repository-Name.git
cd Your-Repository-Name
```

**2. Install dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


**3. Set Up Environment Variables (Refer .env_example)**
- Create a .env file 
```bash
OPENAI_API_KEY='Your-api-key'
OPENAI_API_TYPE='azure'
OPENAI_API_VERSION='2023-05-15'
API_BASE='Your-base-url'
AZURE_OPENAI_DEPLOYMENT='dall-e-3'
```




    


