from google.cloud import aiplatform
#from aiplatform.vertexai.language_models import TextGenerationModel

aiplatform.init(project="gen-benchwarmers", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
model = aiplatform
model = aiplatform.models.TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """White phrase that would describe what type of math problem it is and give additional description. Do not solve the question.

input: 3x + 4 = y
output: This is a linear equation with one variable. It can be solved by isolating the variable x on one side of the equation.


input: . Which of the following sets of vectors are bases for R
2
?
a). {(0, 1), (1, 1)}
b). {(1, 0), (0, 1), (1, 1)}
c). {(1, 0), (−1, 0}
d). {(1, 1), (1, −1)}
e). {((1, 1), (2, 2)}
f). {(1, 2)}

output: This is a question about linear algebra. It asks which of the following sets of vectors are bases for R2. A basis for a vector space is a set of vectors that span the space and are linearly independent.


input: Prove that every integer greater than 1 is a product of prime numbers.

output: This is a proof by induction. prove a statement about an arbitrary number n by first proving it is true when n is 1 and then assuming it is true for n=k and showing it is true for n=k+1


input: ∫cos^2xdx
output: This is a definite integral. It can be evaluated using the power rule for integration.


input: expand 
(2x−3)^4
output: This is a polynomial expansion problem. It can be solved using the binomial theorem.
""",
    **parameters
)
print(f"Response from Model: {response.text}")