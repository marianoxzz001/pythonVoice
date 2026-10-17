import speech_recognition as sr
import pyttsx3
import pygame
import os
from gtts import gTTS


# Inicializa o reconhecedor e a fala
r = sr.Recognizer()
engine = pyttsx3.init()



def falar(texto):
    # Cria o objeto de voz do Google em português
    tts = gTTS(text=texto, lang='pt', tld='com.br')
    
    # Salva o arquivo de áudio temporário
    arquivo_audio = "resposta.mp3"
    tts.save(arquivo_audio)
    
    # Inicializa o pygame mixer para tocar o áudio
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    
    # Aguarda o áudio terminar de tocar
    while pygame.mixer.music.get_busy():
        continue
        
    # Desliga o mixer para liberar o arquivo
    pygame.mixer.quit()
    
    # Remove o arquivo temporário (opcional)
    os.remove(arquivo_audio)

# Volume (vai de 0.0 a 1.0)
engine.setProperty('volume', 0.9)

# Configura a voz para português
voices = engine.getProperty('voices')
for voice in voices:
    if "brazil" in voice.name.lower() or "portugues" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Usa o microfone como fonte de áudio
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # calibra o ruído do ambiente
    print('Diga alguma coisa:')
    audio = r.listen(source)

try:
    # Reconhece o áudio usando o Google Web Speech em português
    comando = r.recognize_google(audio, language='pt-BR')
    print(f'Você disse: {comando}')

    # Fala o texto reconhecido (antes estava falando o "audio")
    engine.say(f"voce disse {comando}")
    falar("Olá! Esta é uma voz gerada pelo Google em Python.")
    engine.runAndWait()

    # Ação simples baseada no comando
    if 'abrir navegador' in comando.lower():
        print('Abrindo o navegador...')

except sr.UnknownValueError:
    print('Não foi possível entender o áudio.')
except sr.RequestError as e:
    print(f'Erro ao comunicar com o serviço de reconhecimento: {e}')