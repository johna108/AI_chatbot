# AI Chatbot with Speech and Image Recognition

A sophisticated chatbot application that combines natural language processing, speech recognition, and image recognition capabilities. Built with Python and Streamlit, this application offers an interactive interface for text chat, voice input, and image analysis.

## Features

- **Text-based Chat**: 
  - Powered by OpenAI's GPT model for intelligent conversations
  - Automatic spell correction for user inputs
  - Chat history tracking in sidebar
- **Speech Recognition**: 
  - Voice input support using Google's Speech Recognition
  - Real-time audio processing
  - Error handling for unclear audio
- **Image Recognition**: 
  - Advanced image analysis using Imagga API
  - Theme-based classification system
  - Natural language description generation
  - Confidence threshold filtering (default: 50%)
- **Intelligent Processing**:
  - Context-aware image descriptions
  - Environment and theme detection
  - Multi-object recognition and relationship analysis
- **Modern UI**: 
  - Clean and responsive interface built with Streamlit
  - Real-time updates
  - Mobile-friendly design

## System Requirements

- Python 3.7+
- Working microphone for speech recognition
- Stable internet connection
- Operating System: Windows/macOS/Linux
- Minimum 4GB RAM recommended
- Webcam (optional, for image capture)

## Prerequisites

### API Keys Required:
1. **OpenAI API Key**
   - Sign up at https://openai.com/api
   - Free tier available with usage limits
   - Pricing based on token usage

2. **Imagga API Key and Secret**
   - Register at https://imagga.com/auth/signup
   - Free tier: 1000 requests/month
   - Additional tiers available for higher usage

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd AI_chatbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:

For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your-openai-api-key"
$env:IMAGGA_API_KEY="your-imagga-api-key"
$env:IMAGGA_API_SECRET="your-imagga-api-secret"
```

For Linux/macOS:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export IMAGGA_API_KEY="your-imagga-api-key"
export IMAGGA_API_SECRET="your-imagga-api-secret"
```

Alternatively, create a `.env` file:
```
OPENAI_API_KEY=your-openai-api-key
IMAGGA_API_KEY=your-imagga-api-key
IMAGGA_API_SECRET=your-imagga-api-secret
```

## Usage

1. Start the application:
```bash
streamlit run chatbot.py
```

2. Access the web interface through your browser (typically http://localhost:8501)

3. Features Usage:
   - **Text Chat**: Type your message in the input box
   - **Voice Input**: Click the 🎤 button and speak clearly
   - **Image Analysis**: Upload images in JPG/JPEG/PNG format
   - **Chat History**: View previous conversations in the sidebar

## Technical Details

### Components

1. **Chat Interface**
   - Uses OpenAI's GPT model (text-davinci-003)
   - Maximum response length: 100 tokens
   - Includes error handling for API failures

2. **Speech Recognition**
   - Uses Google's Speech-to-Text service
   - Requires clear audio input
   - Supports multiple languages (based on system settings)

3. **Image Recognition**
   - Theme-based classification system:
     - Person: people, human, man, woman
     - Nature: sky, tree, flower, landscape
     - Technology: computer, phone, screen, device
     - Animals: animal, dog, cat, wildlife
   - Environment detection: indoor, outdoor, city, landscape
   - Confidence threshold filtering (customizable)
   - Natural language description generation

4. **Text Processing**
   - Automatic spell correction using TextBlob
   - Context-aware sentence generation
   - Multi-theme detection and analysis

## Configuration Options

- `confidence_threshold`: Adjust image recognition confidence (default: 50%)
- Custom themes can be added to `common_themes` dictionary
- Environment tags can be modified in `environment_tags` list

## API Usage and Limits

### OpenAI API
- Free tier: Limited tokens with usage caps
- Paid tier: Based on token usage
- Rate limits apply based on tier

### Imagga API
- Free tier: 1000 requests/month
- Response time: ~1-2 seconds
- Image size limits apply

### Google Speech Recognition
- Free tier available
- Usage limits apply
- Internet connection required

## Error Handling

The application includes comprehensive error handling for:
- Speech recognition failures
- API communication issues
- Invalid inputs
- Network connectivity problems
- File format issues
- Authentication errors

## Security Notes

- API keys are stored as environment variables
- Secure base64 encoding for API authentication
- No sensitive data storage in the application
- Temporary file handling for uploads
- No data persistence between sessions

## Limitations

- Requires active internet connection
- API rate limits may apply
- Speech recognition accuracy depends on:
  - Audio quality
  - Background noise
  - Microphone quality
  - Accent and pronunciation
- Image recognition limited to:
  - Supported file formats (JPG/JPEG/PNG)
  - File size limits
  - Imagga API capabilities
- Chat responses limited to 100 tokens

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a Pull Request

## License

Free to Contribute

## Support

For issues and feature requests, please use the GitHub issue tracker.
