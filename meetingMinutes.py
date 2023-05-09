import os
import argparse
import openai
import logging

logging.basicConfig(level=logging.INFO)

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(audio_file_path, output_file_path):
    logging.info(f"Transcribing audio file: {audio_file_path}")
    with open(audio_file_path, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
    with open(output_file_path, "w") as f:
        logging.info(f"Saving transcript to file: {output_file_path}")
        f.write(transcript.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file_path", type=str, help="Path to the audio file")
    parser.add_argument("output_file_path", type=str, help="Path to the output file")
    args = parser.parse_args()

    transcribe_audio(args.audio_file_path, args.output_file_path)
