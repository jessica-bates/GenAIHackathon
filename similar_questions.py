import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="gen-benchwarmers", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 1
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """can you generate 3 questions similar to 3x+4=10 including answers
""",
    **parameters
)
print(f"Response from Model: {response.text}")