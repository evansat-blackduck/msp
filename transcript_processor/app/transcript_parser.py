import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt', quiet=True)

class TranscriptParser:
    def __init__(self, transcript):
        self.transcript = transcript
        self.attendees = []
        self.success_criteria = []

    def parse(self):
        self._extract_attendees()
        self._extract_success_criteria()
        return {
            'attendees': self.attendees,
            'success_criteria': self.success_criteria
        }

    def _extract_attendees(self):
        attendee_pattern = r'(?:Attendees|Participants):\s*((?:[\w\s]+(?:,\s*)?)+)'
        match = re.search(attendee_pattern, self.transcript, re.IGNORECASE)
        if match:
            attendees_str = match.group(1)
            self.attendees = [attendee.strip() for attendee in attendees_str.split(',')]

    def _extract_success_criteria(self):
        sentences = sent_tokenize(self.transcript)
        for sentence in sentences:
            if 'success criteria' in sentence.lower():
                self.success_criteria.append(sentence.strip())

def parse_transcript(transcript_text):
    parser = TranscriptParser(transcript_text)
    return parser.parse()