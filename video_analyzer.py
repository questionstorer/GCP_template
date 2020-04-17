
import apache_beam as beam
from google.cloud import videointelligence
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.protobuf.json_format import MessageToJson
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
import json
import logging

logging.basicConfig(level=logging.INFO)

class VideoAnalyzer(beam.DoFn):
    def __init__(self):
        beam.DoFn.__init__(self)
        self.video_client = None
        self.features = None
        self.config = None
        self.video_context = None
    def parse_annotation(self, result):
        text = []
        alternatives = result["annotationResults"][0]["speechTranscriptions"]
        for alternative in alternatives:
            if "transcript" in alternative["alternatives"][0]:
                text.append(alternative["alternatives"][0]["transcript"])
        
        return "\n".join(text)
		
		
    def process(self, uri):
        if not self.video_client:
            self.video_client = videointelligence.VideoIntelligenceServiceClient()
            self.features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]
            self.config = videointelligence.types.SpeechTranscriptionConfig(
                language_code="en-US", enable_automatic_punctuation=True)
            self.video_context = videointelligence.types.VideoContext(
                speech_transcription_config=self.config)
        
            
        operation = self.video_client.annotate_video(
            uri, features=self.features, video_context=self.video_context)
        result = json.loads(MessageToJson(operation.result(timeout=600)))
		
        text = self.parse_annotation(result)
        return [(uri, text)]

class SentimentAnalyzer(beam.DoFn):
    def __init__(self):
        beam.DoFn.__init__(self)
        self.client = None
        self.type_ = None
        self.language = None
        self.encoding_type = None
		
    def process(self, input):
        uri, text = input
        if not self.client:
            self.client = language_v1.LanguageServiceClient()
            self.type_ = enums.Document.Type.PLAIN_TEXT
            self.language = "en"
            self.encoding_type = enums.EncodingType.UTF8
		
        document = {"content": text, "type": self.type_, "language": self.language}
        response = self.client.analyze_sentiment(document, encoding_type=self.			encoding_type)
		
        result = json.loads(MessageToJson(response))
		
        return [(uri, result["documentSentiment"]["score"])]

class prepare_write(beam.DoFn):
	def process(self, input):
		uri, result = input
		return uri + ";" + str(result)

def run(input_path, output_path, options=None):

    with beam.Pipeline(options=options) as p:
        _ = (p
			| 'get uris' >> beam.io.ReadFromText(input_path)
			| 'get transcription' >> beam.ParDo(VideoAnalyzer())
			| 'analyze sentiment' >> beam.ParDo(SentimentAnalyzer())
			| 'output metadata' >> beam.io.WriteToText(output_path))
	
	
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      '--input-path',
      required=True,
      help='path to video path list')

    parser.add_argument(
      '--output-path',
      required=True,
      help='Path to the exported video metadata')
	  
    args, pipeline_args = parser.parse_known_args()
    
    options = PipelineOptions(pipeline_args)


    run(args.input_path, args.output_path, options)
	