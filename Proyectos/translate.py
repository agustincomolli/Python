import openai

# Configura tu clave de API aquí
#openai.api_key = "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"
openai.api_key = "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"

def translate_text(text, target_language):
    response = openai.Completion.create(
        engine="davinci",  # Puedes ajustar el motor según las opciones disponibles
        prompt=text,
        max_tokens=50,  # Puedes ajustar este valor según tus necesidades
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def translate_srt_file(input_file, target_language):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    translated_lines = []

    for line in lines:
        if line.strip().isnumeric():
            translated_lines.append(line)  # Preserve line numbers
        else:
            translated_text = translate_text(line.strip(), target_language)
            translated_lines.append(translated_text)

    output_file = input_file.replace('.srt', f'_{target_language}.srt')
    with open(output_file, 'w') as file:
        file.writelines(translated_lines)

    print(f"Traducción completada. El archivo traducido se encuentra en: {output_file}")

if __name__ == "__main__":
    input_file = "archivo.srt"  # Cambia esto al nombre de tu archivo SRT
    target_language = "es"  # Cambia esto al idioma al que deseas traducir

    translate_srt_file(input_file, target_language)
