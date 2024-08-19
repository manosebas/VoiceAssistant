from RealtimeSTT import AudioToTextRecorder
import assist
# import tools

if __name__ == '__main__':

                                                #tiny, base, small, medium, o large
    recorder = AudioToTextRecorder(spinner=False, model="base", language="en", post_speech_silence_duration =0.1, silero_sensitivity = 0.4)
    hot_words = ["Manolo"]
    skip_hot_word_check = False

    print("Im listening...")

    while True:
        current_text = recorder.text()
        print(current_text)

        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
                    
                    if current_text:
                        print("User: " + current_text)
                        recorder.stop()

                        response = assist.ask_question_memory(current_text)
                        print(response)
                        speak = assist.TTS(response)

                        recorder.start()
                        #continua la conversacion 
                        skip_hot_word_check = True if "?" in response else False

                        # if len(response.split('#')) > 1:
                        #     command = response.split('#')[1]
                        #     tools.parse_command(command)