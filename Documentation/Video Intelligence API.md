# Video Intelligence API

## Usage

Features: 

- label analysis: detect and extract information about entities shown in video.

- shot changes: Detect scene changes in video

- detect and track objects: Detect and track objects, how many, where they are within the frame (bounding box), and when they show up (timestamp).

- detect and extract text: Detect and extract text using OCR, know where it is within the frame (bounding box), and when it shows up (timestamp).

- Moderate content: Detect explicit content(adult, violent, etc.) within images.

- Analyze streaming and stored video

- Automate video transcription for closed captioning and subtitles: Transcribe speech to text with punctuation. Refine results with alternatives provided for transcribed words or phrases. Censor profanities. Transcribe up to two audio tracks from multitrack video files. Currently supports English.

Supported Video format

The Video Intelligence API supports common video formats, including `.MOV`, `.MPEG4`, `.MP4`, `.AVI`, and the formats decodable by [ffmpeg](https://ffmpeg.org/) such as `FLV`, `MKV`.

Beta Features:

- Stream video: Label detection, Shot change detection, Explicit content detection, Explicit content detection, Object tracking. 

- Live Stream video: Live Label Detection, Live Shot Change Detection, Live Explicit Content Detection, Live Object Detection and Tracking

### Code example

*Python*

```python
from google.cloud import videointelligence
from google.protobuf.json_format import MessageToJson

video_client = videointelligence.VideoIntelligenceServiceClient()
# get features for label detection
features = [videointelligence.enums.Feature.LABEL_DETECTION]

operation = video_client.annotate_video(input_uri=input_uri, features=features)

print("\nProcessing video for label detection.")
result = operation.result(timeout=3600)
annotation_result = result.annotation_results[0]

# parse result as a JSON file
response = MessageToJson(annotation_result)

return response
```

### Response example

```json
{
  "@type":         "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
  "annotationResults": [
    {
      "inputUri": "/test_34336/video",
      "segment": {
          "inputUri": "/test_34336/video",
          "segment": {
              "segmentLabelAnnotations":[
                  "categoryEntities": [
                    {
                      "description": "animal",
                      "entityId": "/m/0jbk",
                      "languageCode": "en-US"
                    }
                  ],
                  "entity": {
                    "description": "bird",
                    "entityId": "/m/015p6",
                    "languageCode": "en-US"
                  },
                  "segments": [
                    {
                      "confidence": 0.66169775,
                      "segment": {
                        "endTimeOffset": "200.366833s",
                        "startTimeOffset": "0s"
                      }
                    }
                  ]
              ],
              "shotLabelAnnotations": [
               {
                  "categoryEntities": [
                    {
                      "description": "geographical feature",
                      "entityId": "/m/043rvww",
                      "languageCode": "en-US"
                    }
                  ],
                  "entity": {
                    "description": "polar ice cap",
                    "entityId": "/m/048nfp",
                    "languageCode": "en-US"
                  },
                  "segments": [
                    {
                      "confidence": 0.53277606,
                      "segment": {
                        "endTimeOffset": "88.463375s",
                        "startTimeOffset": "87.378958s"
                      }
                    }
                  ]
                }
              ]
          }
      }
  ]
}
```

## 

## Deployment

There are many ways to deploy an application using video intelligence. One can run the code in compute engine, app engine or publish it as a cloud function. However one crucial step before one can use video intelligence API is the authentication. Video intelligence API does NOT support authenticating via user account. 

When API is called from a compute engine or app engine, service account asscoiated to these instances will be automatically used to call the API so no further setup has to be done. If one is using Cloud function to call the API, then the service account can be set in creating the Cloud function and no further setup is needed.

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

## Logging

## Billing

*Stored video annotation*

| Feature                    | First 1000 minutes | Minutes 1000+                                          |
| -------------------------- | ------------------ | ------------------------------------------------------ |
| Label detection            | Free               | $0.10 / minute                                         |
| Shot detection             | Free               | $0.05 / minute, or free with Label detection           |
| Explicit content detection | Free               | $0.10 / minute                                         |
| Speech transcription       | Free               | $0.048 / minute (charges for en-US transcription only) |
| Object tracking            | Free               | $0.15 / minute                                         |
| Text detection             | Free               | $0.15 / minute                                         |
| Logo recognition           | Free               | $0.15 / minute                                         |
| Celebrity recognition      | Free               | $0.10 / minute                                         |

*Streaming video annotation*

| Feature                    | First 1000 minutes | Minutes 1000+  |
| -------------------------- | ------------------ | -------------- |
| Label detection            | Free               | $0.12 / minute |
| Shot detection             | Free               | $0.07 / minute |
| Explicit content detection | Free               | $0.12 / minute |
| Object Tracking            | Free               | $0.17 / minute |

## Use cases

- Use video intelligence API as a Cloud Function

- Use video intelligence API to process video in Compute Engine or App Engine

- Analyze Accenture uploaded to MediaExchange and analyze video labels to enable better label classification for search engine.

- 
