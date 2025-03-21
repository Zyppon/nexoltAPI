from transformers import LlamaForCausalLM , LlamaTokenizer
import torch

model_name = "meta-llama/Llama-3.3-70B-Instruct"
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name)


def fine_tune_model(model , tokenizer  , train_data):
    inputs = tokenizer(train_data , return_tensors="pt" , padding=True , truncation=True)
    labels = inputs.input_ids
    outputs = model(input_ids=inputs.input_ids, labels=labels)
    loss = outputs.loss
    return loss

def generate_response(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(input_ids=inputs.input_ids, max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

model.save_pretrained("./nexolt-1")
tokenizer.save_pretrained("./nexolt-1")