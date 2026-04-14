
# AI Agent

## Overview
This project is an AI Agent application built with Python.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AIAgent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Setup

1. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

2. Add your configuration variables to `.env`:
```
GEMINI_API_KEY=your_api_key_here
```

3. The application will automatically load variables from `.env` using `python-dotenv`

**Note:** Never commit `.env` to version control. Add it to `.gitignore`.

## Usage

```bash
python main.py
```

## Contributing

See CONTRIBUTING.md for guidelines.
