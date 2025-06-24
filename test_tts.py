from TTS.api import TTS

# Obtener la lista de modelos disponibles
tts = TTS()

# Seleccionar el modelo en español
model_name = "tts_models/es/css10/vits"

# Inicializar el modelo
tts = TTS(model_name)

# Texto a convertir en voz
texto = "¡Hola! Este es un ejemplo de síntesis de voz con Coqui TTS."

# Generar y guardar el audio
tts.tts_to_file(text=texto, file_path="output.wav") 