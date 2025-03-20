import ollama

class NexoltAI:
    def __init__(self , model_name='nexolt-1'):
        self.model_name = model_name

    def chat(self , prompt):
        response = ollama.chat(model=self.model_name , messages=[{"role": "user", "content": prompt}])
        return response['message']