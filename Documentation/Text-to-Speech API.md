# Text-to-Speech API

## Table of Content

1. Usage

2. Billing

3. Code example

4. Deployment

5. Debugging

6. Use Case

## Usage

- Converts text or Speech Synthesis Markup Language (SSML) input into audio data

- Creates audio that sounds like a person talking using WaveNet.

## Billing

| Feature                       | Free                      | Paid usage                        |
| ----------------------------- | ------------------------- | --------------------------------- |
| Standard (non-WaveNet) voices | 0 to 4 million characters | $4.00 USD / 1 million characters  |
| WaveNet voices                | 0 to 1 million characters | $16.00 USD / 1 million characters |

## Code example

*Python package installation*

```shell
pip install --upgrade google-cloud-texttospeech
```

*Create audio from text*

```python
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

text = "近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独力支持，做了许多大事。哪知老境却如此颓唐！他触目伤怀，自然情不能自已。情郁于中，自然要发之于外；家庭琐屑便往往触他之怒。他待我渐渐不同往日。但最近两年不见，他终于忘却我的不好，只是惦记着我，惦记着他的儿子。我北来后，他写了一信给我，信中说道：“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不便，大约大去之期不远矣。”我读到此处，在晶莹的泪光中，又看见那肥胖的、青布棉袍黑布马褂的背影。唉！我不知何时再能与他相见！"

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text=text)

# Build the voice request, select the language code and specify a voice listed in https://cloud.google.com/text-to-speech/docs/voices
voice = texttospeech.types.VoiceSelectionParams(
    language_code='zh',
    name='cmn-CN-Wavenet-C')

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('背影.mp3', 'wb') as out:

    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "背影.mp3"')
```

## Deployment





## Debugging

One can debug the written code that calls the video API in Cloud SDK or Cloud interactive shell. In this case, proper authentication must be applied before video API becomes accessible.

*Authentication via a service account*

A service account is required to call the video intelligence API. Note that a user account cannot be used to call the API.

If the API is called from inside GCP in deployment time, then the authentication is automatically setup via service account assoicated to various services.

However, if one is calling the API using Cloud SDK, for example, in developing or debugging time, he has to set up the authentication manually.

To authenticate via a service account in Cloud SDK, one can use the service account key file. [Document](%5Bhttps://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python%5D(https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python) here covers the following points necessary to authenticate a service account via the key file

- Create service account and get the service account key file

- Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the key file

- Call the api using packages in Cloud SDK



## Use cases

- Use video intelligence API as a Cloud Function

- Use video intelligence API to process video in Compute Engine or App Engine

- Analyze Accenture uploaded to MediaExchange and analyze video labels to enable better label classification for search engine.
