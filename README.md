# LTUAssistantPlus

[![Python](https://github.com/Xyaneon/LTUAssistantPlus/actions/workflows/python.yaml/badge.svg)](https://github.com/Xyaneon/LTUAssistantPlus/actions/workflows/python.yaml)

LTUAssistantPlus is a voice-controlled AI assistant created specifically for use by LTU students.

This is a continuation of the [LTUAssistant][LTUAssistant] project, with a
modernized code base and added FAQ functionality.

## Setup

### Dependencies

LTUAssistantPlus has direct dependencies on the following packages:
- [beautifulsoup4][beautifulsoup4]
- [Neo4j][Neo4j]
- [PyAudio][PyAudio]
- [spaCy][spaCy]
- [SpeechRecognition][SpeechRecognition]
- [win10toast][win10toast]

See the `requirements.txt` file for a complete listing of needed pip packages.

### Installation

**Note: These instructions are all given for Windows.**

This project needs additional setup for Neo4j, run as the local database. You
will need the following prerequisites for it:

- [Chocolatey][Chocolatey] (an application package manager for Windows)
- A Java 1.8 runtime environment (JRE)

Once the above are installed on your machine, run the following command in an
elevated PowerShell prompt to install Neo4j Community Edition (based on
[this blog post][Neo4j via Chocolatey]):

```PS
choco install neo4j-community -version 3.5.1
```

After this, you will also need the project's direct dependencies. For instance,
you will need Python installed. This project has been tested with Python 3.6.8
64-bit on Windows 10.

In a command prompt, navigate into the cloned project directory and run:

```PS
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Usage

Navigate to the Neo4j installation directory (if you used the Chocolatey
command above, this is likely
`C:\tools\neo4j-community\neo4j-community-3.5.1`).

Before you start the server for the first time, you need to set the password.
Run the following command (you only ever need to do this once):

```PS
bin/neo4j-admin set-initial-password password
```

Also, for running Neo4j locally, you may have to change the following property
in your `neo4j.conf` file in the `conf` subfolder of the installation
directory to disable HTTPS (we only need HTTP and Bolt here):

```
dbms.connector.https.enabled=false
```

Then start the server:

```PS
bin\neo4j console
```

The above will allow the assistant to connect to the database using the Bolt
driver endpoint on port 7678, with username `neo4j` and password `password`.

In another command prompt, navigate to the project's top-level directory, then
run:

```PS
python .\LTUAssistantPlus\LTUAssistant.py
```

The assistant will greet you after the NLP pipeline initializes. Once you see
the phrase `Say something!` in the terminal, you may speak your command and
wait for the assistant to process it.

**Notes:**
- Currently, the assistant can only process one command per session. To have
  it execute another command, you need to restart the script.
- The assistant's data will be stored in the `~/.LTUAssistant` directory on
  your computer.

### Sample commands

LTUAssistantPlus organizes what it can do into multiple skills, each of which
is dedicated to handling one particular task. Here are some things you can
say to the assistant to try out its capabilities.

#### Add schedule events

- "Schedule an event."
- "Plan an event."
- "Remind me about an event."

#### Change the assistant's voice

- "Use a male voice."
- "Use a female voice."

#### Change the name the assistant calls you by

- "Call me Bob."

#### Open an LTU website

- "Go to BannerWeb."
- "Open Gmail."

#### Find the building and floor of a room on campus

- "Find room S108."

#### Compose an email

- "Send an email."
- "Compose an email to example@example.com."

#### Tell the current date

- "Tell me the date."
- "What is the current date?"

#### Remind the user which events are scheduled for today

- "What is my schedule?"

#### Tell the current time

- "Tell me the time."
- "What is the current time?"

## Testing

This project includes some unit tests. To run all tests, navigate into the
`LTUAssistantPlus` directory under the project root, then run this command:

```PS
python -m unittest discover -v
```

## License

This project is made available under the MIT license. Please see the
[LICENSE][license] file in the project root directory for details.

License notices for third-party software libraries this project uses are
listed in the [THIRD_PARTY_NOTICES.txt][third-party notices] file for
reference.

## About

This was a project by Christopher Horton and Mengyi Chen for Lawrence
Technological University's Collaborative Research Project 2 course during the
Fall 2019 semester. It was done under the supervision and guidance of Dr.
Paula Lauren.

[beautifulsoup4]: https://pypi.org/project/beautifulsoup4/
[Chocolatey]: https://chocolatey.org/
[license]: https://github.com/Xyaneon/LTUAssistantPlus/blob/master/LICENSE
[LTUAssistant]: https://github.com/Xyaneon/LTUAssistant
[Neo4j]: https://pypi.org/project/neo4j/
[Neo4j via Chocolatey]: https://neo4j.com/blog/chocolatey-neo4j-windows/
[PyAudio]: http://people.csail.mit.edu/hubert/pyaudio/
[spaCy]: https://spacy.io/
[SpeechRecognition]: https://pypi.org/project/SpeechRecognition/
[third-party notices]: https://github.com/Xyaneon/LTUAssistantPlus/blob/master/THIRD_PARTY_NOTICES.txt
[win10toast]: https://github.com/jithurjacob/Windows-10-Toast-Notifications
