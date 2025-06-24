from TTS.api import TTS

# Inicializar el modelo Tacotron2 en español
tts = TTS(model_name="tts_models/es/mai/tacotron2-DDC")

# Texto para probar la síntesis de voz
texto = "Hola, este es un ejemplo de síntesis de voz en español usando el modelo Tacotron2. ¿Cómo suena mi acento argentino?"

# Generar audio
tts.tts_to_file(
    text=texto,
    file_path="output_tacotron.wav"
) 