from TTS.api import TTS

# Inicializar el modelo VITS en español
tts = TTS(model_name="tts_models/es/css10/vits")

# Texto para probar la síntesis de voz
testo = "Hoy me levanté con mucho dolor abdominal, creo que me fisuré una costilla"

# Generar audio
tts.tts_to_file(
    text=testo,
    file_path="output_espanol_vits.wav"
)

print("¡Audio generado como output_espanol_vits.wav!") 