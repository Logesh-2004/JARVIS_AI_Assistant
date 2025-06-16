from core.speech_to_text import listen
from core.text_to_speech import speak
from core.jarvis_brain import get_response
#from core.wake_word import detect_wake_word
from core.command_parser import execute_command

print("🔵 JARVIS is warming up...")

while True:
    #if detect_wake_word():
        user_input = listen()
        print("You said:", user_input)

        response = get_response(user_input)
        print("Jarvis:", response)

        action_done = execute_command(user_input)
        speak(response)
