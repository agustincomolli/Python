import openai

API_KEY = "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"

openai.api_key = API_KEY
task_description = "Traducir subtítulos de inglés a español:"
with open("./subtítulo.vtt", mode="r", encoding="UTF-8") as file:
    to_translate = file.read()

prompt = task_description+"\n" + to_translate

#The API call
#respone will contain the generated translation
response = openai.Completion.create(
  model="text-curie-001",
  prompt=prompt,
  temperature=0.3,
  max_tokens=2048,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
 
#Print the JSON response from GPT-3
print(response)