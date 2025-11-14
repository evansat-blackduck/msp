import os
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
from .transcript_parser import parse_transcript
from .pptx_generator import generate_pptx
from .salesforce_integration import attach_to_salesforce

app = FastAPI()

@app.post("/process_transcript")
async def process_transcript(
    transcript: UploadFile = File(...),
    template_pptx: UploadFile = File(...),
    opportunity_id: str = Form(...)
):
    # Save uploaded files
    transcript_path = f"/tmp/{transcript.filename}"
    template_path = f"/tmp/{template_pptx.filename}"
    
    with open(transcript_path, "wb") as buffer:
        buffer.write(await transcript.read())
    with open(template_path, "wb") as buffer:
        buffer.write(await template_pptx.read())

    # Process transcript
    with open(transcript_path, "r") as f:
        transcript_text = f.read()
    parsed_data = parse_transcript(transcript_text)

    # Generate PPTX
    output_pptx = NamedTemporaryFile(delete=False, suffix=".pptx")
    output_path = generate_pptx(template_path, output_pptx.name, parsed_data['attendees'], parsed_data['success_criteria'])

    # Attach to Salesforce
    sf_result = attach_to_salesforce(opportunity_id, output_path)

    if sf_result:
        return FileResponse(output_path, filename="processed_transcript.pptx")
    else:
        return {"error": "Failed to attach file to Salesforce opportunity"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)