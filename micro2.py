import asyncio
import os
import edge_tts
import pygame

# Lista de excelentes vozes em português brasileiro para testar:
# "pt-BR-FranciscaNeural" (Feminina - Muito natural)
# "pt-BR-AntonioNeural"   (Masculina - Excelente)
# "pt-BR-ThalitaNeural"   (Feminina - Estilo assistente)


VOZ_SELECIONADA = "pt-BR-FranciscaNeural"
ARQUIVO_AUDIO = "audio_realista.mp3"

async def gerar_voz(texto):
    """Gera o arquivo de áudio usando a IA da Microsoft"""
    communicate = edge_tts.Communicate(texto, VOZ_SELECIONADA)
    await communicate.save(ARQUIVO_AUDIO)

def reproduzir_audio():
    """Reproduz o arquivo MP3 de forma limpa"""
    pygame.mixer.init()
    pygame.mixer.music.load(ARQUIVO_AUDIO)
    pygame.mixer.music.play()
    
    # Aguarda o áudio terminar de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.quit()
    
    # Remove o arquivo temporário após o uso
    if os.path.exists(ARQUIVO_AUDIO):
        os.remove(ARQUIVO_AUDIO)

def falar(texto):
    """Função principal que junta a geração e a reprodução"""
    print(f"Gerando áudio para: '{texto}'...")
    # Executa a função assíncrona de geração de voz
    asyncio.run(gerar_voz(texto))
    # Toca o áudio gerado
    reproduzir_audio()

# --- Testando o Sistema ---
if __name__ == "__main__":
    texto_exemplo = (
        "Olá! Esta voz é gerada por redes neurais artificiais. "
        "Como você pode perceber, a minha entonação, as pausas para respiração "
        "e o ritmo da fala parecem muito mais com os de um ser humano."
    )
    falar(texto_exemplo)
