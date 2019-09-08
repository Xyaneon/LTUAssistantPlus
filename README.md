# LTUAssistantPlus

LTUAssistantPlus is a voice-controlled AI assistant created specifically for use by LTU students.

## Setup

You will first need Python installed. This project has been tested with Python 3.7.4 64-bit on Windows 10.

On Windows, navigate into the cloned project directory and run:

```
python -m venv .venv
```

Get [PyTorch][PyTorch] installed as a dependency of the `stanfordnlp` package:

```
python -m pip install https://download.pytorch.org/whl/cpu/torch-1.0.1-cp37-cp37m-win_amd64.whl
```

Install the [`stanfordnlp`][stanfordnlp] (v0.2.0) package once this is done:

```
python -m pip install stanfordnlp
```

Install the [SpeechRecognition][SpeechRecognition] (>=3.8.1) package:

```
python -m pip install SpeechRecognition
```

Install the [win10toast][win10toast] package:

```
python -m pip install win10toast
```

[PyTorch]: https://pytorch.org/
[SpeechRecognition]: https://pypi.org/project/SpeechRecognition/
[stanfordnlp]: https://stanfordnlp.github.io/stanfordnlp/
[win10toast]: https://github.com/jithurjacob/Windows-10-Toast-Notifications