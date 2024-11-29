# AI Tutor

This project provides an application for automatic correction and analysis using AI model
The service takes an essay and a predefined question as input and returns detailed feedback in HTML format.

## Features
- Essay evaluation with AI-powered feedback
- Predefined writing prompts
- HTML-formatted response suitable for integration into applications
- Docker containerization for easy deployment

## Prerequisites
- Docker and Docker Compose installed
- Hugging Face API key

## Testing
For testing purposes, you can:

1. Clone the repository:
```bash
git clone (https://github.com/Pleias/BSF_AI_tutor.git)
cd BSF_AI_tutor
```
2. Run Docker Compose
```bash
docker-compose up --build
```
3. Open http://127.0.0.1:8090 in your browser
Try the interface to see example inputs and outputs

<img src="https://github.com/user-attachments/assets/a1aae489-ac0f-428f-ba3d-7ec228c939f7" width="400" alt="Input Interface"/>
</br>
<img src="https://github.com/user-attachments/assets/e6ae65e7-0229-42dc-abb1-0c29e4c70b9b" width="500" alt="Output Interface"/>

## Integration

Available endpoints:
1. GET '/' - renders test page with form
2. POST '/submit' - handles essay evaluation

## Integration Example
```python
import requests

# For essay evaluation
url = "http://127.0.0.1:8090/submit"
data = {
    "essayInput": "Your essay text here",
    "questionInput": "The predefined question"
}

# Make API call and get HTML response
response = requests.post(url, data=data)
html_feedback = response.text


