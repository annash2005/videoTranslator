import asyncio
import websockets
from oait import translate
import assemblyai as aai

aai.settings.api_key = "1d7ab367e7e143ea8114beef8c02fddc"

async def on_data(websocket, path):
    async for message in websocket:
        if isinstance(message, bytes):
            transcript = aai.RealtimeTranscript(text=message.decode('utf-8'))
            if isinstance(transcript, aai.RealtimeFinalTranscript):
                print("Final Transcript:", transcript.text)
                translation = translate(transcript.text, language="Russian")
                print("Translation:", translation)
                await websocket.send(translation)
            else:
                print("Interim Transcript:", transcript.text, end="\r")

async def main():
    async with websockets.serve(on_data, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
