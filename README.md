# LTUAssistantPlus

LTUAssistantPlus is a voice-controlled AI assistant created specifically for use by LTU students.

This is a continuation of the [LTUAssistant][LTUAssistant] project.

## Setup

You will first need Python installed. This project has been tested with Python 3.6.8 64-bit on Windows 10.

On Windows, navigate into the cloned project directory and run:

```
python -m venv .venv
.venv\Scripts\activate
```

Get [PyTorch][PyTorch] installed as a dependency of the `stanfordnlp` package:

```
python -m pip install https://download.pytorch.org/whl/cpu/torch-1.0.1-cp36-cp36m-win_amd64.whl
```

Install the [`stanfordnlp`][stanfordnlp] (v0.2.0) package once this is done:

```
python -m pip install stanfordnlp
```

Install the [PyAudio][PyAudio] package:

```
python -m pip install pyaudio
```

Install the [SpeechRecognition][SpeechRecognition] (>=3.8.1) package:

```
python -m pip install SpeechRecognition
```

Install the [win10toast][win10toast] package:

```
python -m pip install win10toast
```

## Usage

After all package dependencies have been set up, run the following from the top-level directory (on Windows):

```
python .\LTUAssistantPlus\LTUAssistant.py
```

> **NOTE:**
>
> If this is the first time you are running the assistant, the neural network needed by the `stanfordnlp`
> package to run will be automatically downloaded. Be aware this download is about 235MB in size.
> On subsequent runs, the assistant should be ready right away.
>
> The assistant's data will be stored in the `~/.LTUAssistant` directory on your computer.

The assistant will greet you after the NLP pipeline initializes. Once you see the phrase
`Say something!` in the terminal, you may speak your command and wait for the assistant to
process it.

> **NOTE:**
>
> Currently, the assistant can only process one command per session. To have it execute
> another command, you need to restart the script.

## License

This project is made available under the MIT license. Please see the [LICENSE][license] file in the project root directory for details.

License notices for third-party software libraries this project uses are listed in the [THIRD_PARTY_NOTICES.txt][third-party notices] file for reference.

[license]: https://github.com/Xyaneon/LTUAssistantPlus/blob/master/LICENSE
[LTUAssistant]: https://github.com/Xyaneon/LTUAssistant
[PyAudio]: http://people.csail.mit.edu/hubert/pyaudio/
[PyTorch]: https://pytorch.org/
[SpeechRecognition]: https://pypi.org/project/SpeechRecognition/
[stanfordnlp]: https://stanfordnlp.github.io/stanfordnlp/
[third-party notices]: https://github.com/Xyaneon/LTUAssistantPlus/blob/master/THIRD_PARTY_NOTICES.txt
[win10toast]: https://github.com/jithurjacob/Windows-10-Toast-Notifications
