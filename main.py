import whisper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename
print(f'Loading "{filename}". This may take several seconds.')

model = whisper.load_model("base")
result = model.transcribe(filename)
print(result["text"])