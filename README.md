# Speech to Text

Simple speech to text interpreter using [Whisper].

Winston Churchill audio provided by the [Internet Archive]. These audio files are in ```./samples```.

***Important!*** [Whisper] needs [ffmpeg] package.

## Setup

### Create Python Virtual Environment

``` sh
python3 -m venv .myenv
```

### Install [Whisper]

``` sh
pip install -U openai-whisper
```

OR

``` sh
pip install -r requirements.txt
```

## Run

Syntax: ```python main.py <filename>```

``` sh
python main.py ./samples/churchill-first-month-of-the-war.mp3
```

``` sh
python main.py ./samples/churchill-threat-of-nazi.mp3
```

[ffmpeg]: https://www.ffmpeg.org/
[Whisper]: https://github.com/openai/whisper
[Internet Archive]: https://archive.org/details/Winston_Churchill/