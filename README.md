# AI Tutor

This project provides an application for automatic correction and analysis using AI model
The service takes an essay and a predefined question as input and returns detailed feedback in HTML format.

## Features
- Essay evaluation with AI-powered feedback
- HTML-formatted response suitable for integration into applications
- Docker containerization

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
2. Write you hugging face key into .env file
```bash
HF_TOKEN=your_hugging_face_key_here
```
3. Run Docker Compose
```bash
docker-compose up --build
```
4. Open http://127.0.0.1:8090 in your browser
Try the interface to see example inputs and outputs

<img src="https://github.com/user-attachments/assets/a1aae489-ac0f-428f-ba3d-7ec228c939f7" width="400" alt="Input Interface"/>
</br>
<img src="https://github.com/user-attachments/assets/18809330-647b-4fbb-8660-02674ab922f8" width="400" alt="Output Interface"/>


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
    "essayInput": "User input text",
    "questionInput": "Question for the writing exercise"
}

# Make API call and get HTML response
response = requests.post(url, data=data)
html_feedback = response.text


