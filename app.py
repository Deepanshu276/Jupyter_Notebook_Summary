import os
from tqdm import tqdm
from openai import OpenAI
import asyncio
key=""
#key=os.getenv('')
client=OpenAI(api_key=key)
#client=OpenAI(key)
async def generate_response_of_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content

def generate_response_of_image(prompt, image):
    response=client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[

        {
        "role":"system",
        "content":f"Images/{image}"
        },
        {
        "role":"user",
        "content": prompt,
        }
        ],
    )
    return response.choices[0].message.content
    
def understand_image(image):
    prompt = '''The given image is extracted from jupyter notebook. It is either an image or a type of visualisation. 
    If visualization: 
        1. Identify the type of visualization
        2. If labels or legends are present then using them, extract important and accurate insights with numerical figures or percentages from the visualization if there are any.
    If image/flow chart:
        1. If it has text within it, then accurately read it.
        2. If it doesn't have any text in it, then describe the image in detail.
    
    Instructions:
    1. Make sure above conditions are met.
    2. Do not include anything else in your response.
    3. Be concise, crisp and concrete.
    '''
    prompt = '''
            The provided image is sourced from a Jupyter notebook. It could represent either a visualization or an image/flow chart. Here's what to do in each case:

            If it's a visualization:
            1. Determine the type of visualization.
            2. If labels or legends are available, use them to extract pertinent insights, including numerical data or percentages.

            If it's an image/flow chart:
            1. If there's text embedded in the image, ensure accurate transcription.
            2. If no text is present, provide a detailed description of the image.

            Instructions:
            1. Ensure adherence to the specified conditions.
            2. Limit your response to the given instructions.
            3. Maintain clarity and brevity.

            '''
    return generate_response_of_image(prompt, image)

def main_function():
    about_images = '''Below mentioned are the descriptions of the images/visualizations present in the jupyter notebook:\n'''

    img_path = os.listdir('Images')
 
    image_insights = understand_image(img_path)
    about_images = []
    j=1
    for i in tqdm(img_path):
        prompt = '''Analyse the image and give insights about it. 
        Image: {}'''
        print("------image_insights-------- ",i,", ")
        image_insights = understand_image(i)
        about_images.append(f'image {j}'  + ' ' + str(image_insights) )

        print("------aboubt-------- ", about_images)
        j+=1
    prompt = f'''The following consists description of images/visualizations/flow charts and the code in python that was taken from a
        Jupyter notebook. If visualization then from the IMAGE DESCRIPTIONS match it's code with CODE.
        Understand the contents of the jupyter notebook as shared below and explain it in detail (step by step) along with insights from IMAGE DESCRIPTIONS(if any)

    IMAGE DESCRIPTIONS: {about_images}
    

    CODE:\n{open('output.txt','r', encoding='UTF-8').read()} '''

    a=asyncio.run(generate_response_of_text(prompt))
    return a

