import google.generativeai as genai

class Gemini:
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

    def generateAbstract(self, input_file, output_file):
        # Read the content of the file
        with open(input_file, 'r') as file:
            file_content = file.read()

        # Use the content of the file in the model.generate_content function
        response = self.model.generate_content(f'Faça um resumo a partir dessa transição: {file_content}')

        # Save the response.text in a file
        with open(output_file, 'w') as file:
            file.write(response.text)