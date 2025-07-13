# 🤖 LLM Support Agent

An AI-powered customer support message classification system built with FastAPI and React. This application automatically categorizes customer support messages and suggests appropriate actions using OpenAI's GPT-4.

## ✨ Features

- **Intelligent Classification**: Automatically categorizes messages into:
  - Billing Issues
  - Technical Support
  - Account Management
  - General Feedback

- **Smart Actions**: Suggests next steps:
  - Auto-response for simple queries
  - Request more information
  - Escalate to human agent

- **Rich Analysis**: Provides:
  - Confidence scores
  - Priority levels
  - Reasoning behind classification
  - Suggested customer responses

- **Modern UI**: Clean, responsive React interface
- **Real-time Processing**: Fast API responses with loading states
- **Error Handling**: Comprehensive error management and user feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API Key

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd llm_support_agent_with_ui
```

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Easy Start (Recommended)

Use the provided startup script:

```bash
./start.sh
```

This script will:
- Create a Python virtual environment
- Install all dependencies
- Start both backend and frontend servers
- Open the application in your browser

### 4. Manual Setup (Alternative)

#### Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
# In a new terminal
cd client
npm install
npm run dev
```

## 🌐 Access Points

- **Frontend Application**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📖 Usage

1. **Enter Message**: Type or paste a customer support message in the text area
2. **Classify**: Click "Classify Message" to analyze the message
3. **Review Results**: View the detailed classification including:
   - Intent category
   - Confidence score
   - Priority level
   - Suggested action
   - Reasoning
   - Recommended response

### Example Messages to Try

**Billing Issue:**
```
I was charged twice for my subscription this month. Can you help me get a refund?
```

**Technical Support:**
```
The app keeps crashing when I try to upload files. I've tried restarting but it doesn't work.
```

**Account Management:**
```
I forgot my password and the reset email isn't coming through. Can you help?
```

**General Feedback:**
```
I love the new features you added! The interface is much more intuitive now.
```

## 🏗️ Architecture

### Backend (FastAPI)
- **`app/main.py`**: FastAPI application with CORS and endpoints
- **`app/agent.py`**: OpenAI integration and message classification logic
- **`app/prompts.py`**: AI prompts and classification instructions
- **`app/schemas.py`**: Pydantic models for request/response validation

### Frontend (React + Vite)
- **`client/src/App.jsx`**: Main React component with form and results display
- **`client/src/App.css`**: Responsive styling with modern design
- **`client/src/index.css`**: Global styles and CSS variables

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### API Configuration

The backend runs on port 8000 by default. To change:

```bash
uvicorn main:app --port YOUR_PORT
```

Update the frontend API URL in `client/src/App.jsx`:

```javascript
const response = await fetch('http://localhost:YOUR_PORT/classify', {
```

## 🛠️ Development

### Backend Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
cd app
uvicorn main:app --reload

# Run tests (if you add them)
pytest
```

### Frontend Development

```bash
cd client

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📊 API Reference

### POST /classify

Classify a customer support message.

**Request:**
```json
{
  "message": "string (1-2000 characters)"
}
```

**Response:**
```json
{
  "input": "original message",
  "classification": "JSON string with analysis",
  "status": "success"
}
```

**Classification JSON Structure:**
```json
{
  "intent": "Billing Issue | Technical Support | Account Management | General Feedback",
  "confidence": 0.95,
  "action": "Auto-response | Ask for more information | Escalate to human agent",
  "reasoning": "Brief explanation of classification",
  "suggested_response": "Helpful response to customer",
  "priority": "low | medium | high"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "LLM Support Agent"
}
```

## 🚨 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   - Ensure your API key is correctly set in `.env`
   - Verify the key has sufficient credits

2. **CORS Errors**
   - Check that frontend and backend ports match the CORS configuration
   - Default ports: Frontend (5173), Backend (8000)

3. **Module Import Errors**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

4. **Frontend Build Issues**
   - Delete `node_modules` and run `npm install`
   - Check Node.js version (16+ required)

### Logs and Debugging

- Backend logs appear in the terminal running uvicorn
- Frontend logs appear in browser developer console
- API documentation available at `/docs` endpoint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- FastAPI for the excellent web framework
- React and Vite for the frontend tools
