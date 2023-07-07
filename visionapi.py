import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision_v1.ImageAnnotatorClient()

def detectText(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])
    for text in texts:
        df = df._append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    return df['description'][0]

FILE_NAME = 'image2.png'
FOLDER_PATH = r'C:\Users\lethomps\code\python_venv\VisionAPI\images'
print(detectText(os.path.join(FOLDER_PATH, FILE_NAME)))

