# Transcript Processor

This application processes customer meeting transcripts, generates PowerPoint presentations, and attaches them to Salesforce opportunities.

## Features

- Parse meeting transcripts to extract attendees and success criteria
- Generate PowerPoint presentations using a template
- Attach generated presentations to Salesforce opportunities
- Containerized application for easy deployment

## Prerequisites

- Docker
- Salesforce account with API access

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd transcript_processor
   ```

2. Set up environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   SALESFORCE_USERNAME=your_username
   SALESFORCE_PASSWORD=your_password
   SALESFORCE_SECURITY_TOKEN=your_security_token
   ```

3. Build the Docker image:
   ```
   docker build -t transcript-processor .
   ```

4. Run the container:
   ```
   docker run -p 8000:8000 --env-file .env transcript-processor
   ```

The application will be available at `http://localhost:8000`.

## Usage

To process a transcript and generate a presentation:

1. Prepare your transcript file and PowerPoint template.
2. Send a POST request to `http://localhost:8000/process_transcript` with the following form data:
   - `transcript`: The transcript file
   - `template_pptx`: The PowerPoint template file
   - `opportunity_id`: The Salesforce opportunity ID

Example using curl:
```
curl -X POST http://localhost:8000/process_transcript \
  -F "transcript=@path/to/transcript.txt" \
  -F "template_pptx=@path/to/template.pptx" \
  -F "opportunity_id=your_opportunity_id"
```

The API will return the processed PowerPoint file if successful, or an error message if there was a problem.

## Development

To set up the development environment:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```
   uvicorn app.main:app --reload
   ```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.