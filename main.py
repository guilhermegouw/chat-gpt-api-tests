import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-pro')

q1 = '''Can you review the accuracy of my answer?
subject: Python
question: Explain the difference between lists and tuples in Python.
answer: Lists are mutable, which means they can be altered after creation. They are defined with square brackets. Tuples, on the other hand, are immutable and are defined with parentheses.'''

q2 = '''Can you review the accuracy of my answer? Judge as if it were a Senior Python Developer interview.
subject: Python
question: What are decorators in Python?
answer: Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behavior of a function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
format: markdown
with code example: true'''

response = model.generate_content(q2)

with open('output.md', 'w') as f:
    f.write(response.text)