
# Import necessary functions and classes
from oait import translate
import assemblyai as aai

# Set up AssemblyAI
aai.settings.api_key = "apiKey"

def on_open(session_opened: aai.RealtimeSessionOpened):
    "This function is called when the connection has been established."
    print("Session ID:", session_opened.session_id)

def on_data(transcript: aai.RealtimeTranscript):
    "This function is called when a new transcript has been received."
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print("Final Transcript:", transcript.text)
        translation = translate(transcript.text, language="Russian")
        print("Translation:", translation)
    else:
        print("Interim Transcript:", transcript.text, end="\r")

def on_error(error: aai.RealtimeError):
    "This function is called when an error occurs."
    print("An error occurred:", error)

def on_close():
    "This function is called when the connection has been closed."
    print("Closing Session")

# Transcriber setup
transcriber = aai.RealtimeTranscriber(
    on_data=on_data,
    on_error=on_error,
    sample_rate=44_100,
    on_open=on_open, # optional
    on_close=on_close, # optional
)

# Main function to start the transcription and translation process
def main():
    # Start the connection
    transcriber.connect()

    # Open a microphone stream
    microphone_stream = aai.extras.MicrophoneStream()

    # Press CTRL+C to abort
    try:
        transcriber.stream(microphone_stream)
    except KeyboardInterrupt:
        pass

    transcriber.close()

if __name__ == "__main__":
    main()

