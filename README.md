# AI Content Generator

An individual AI productivity project that generates different types of content using structured prompts.

## Features

- Blog post generation
- Social media generation
- Professional email generation
- Cover letter generation
- Study note generation
- Tone and length controls
- Target audience input
- Copy-to-clipboard
- Prompt optimization demonstration
- Prompt library

## Current version

Version 1 includes a local demo generator so the application can be tested without an API key.

## Run locally

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Prompt optimization

The project compares a basic prompt with a structured prompt containing role, task, audience, tone, format and constraints.

## Future improvement

Connect the `/generate` endpoint to an AI provider and add prompt version tracking so the project can demonstrate measurable prompt improvement.
