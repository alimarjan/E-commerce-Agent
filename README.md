# 🤖 LLM Support Agent
<img width="1424" height="706" alt="image" src="https://github.com/user-attachments/assets/e240fbee-99c2-4f9e-b018-495d5506d1d2" />
````markdown
````markdown
````markdown
````markdown
# Intelligent E-commerce Order Processing Agent

## Assignment Overview

This project fulfills the assignment requirements to create an autonomous agent that automates problems in the e-commerce domain, with **LLM-driven control flow** making all critical decisions throughout the application lifecycle.

**Assignment Requirements Met:**
- ✅ **Agent of Choice**: E-commerce Order Processing Agent
- ✅ **Field of Choice**: E-commerce/Retail Operations
- ✅ **LLM-Controlled Flow**: All decision-making handled by GPT-4
- ✅ **Production Ready**: Full-stack application with proper architecture
- ✅ **GitHub Repository**: Complete codebase with documentation

## 🎯 Problem Domain: E-commerce Order Processing

**Real-World Problem Solved:**
E-commerce businesses struggle with manual order processing, leading to delays, errors, and poor customer experience. This agent automates the entire order lifecycle using AI-driven decision making.

**Key Challenges Addressed:**
- Manual order validation (time-consuming, error-prone)
- Fraud detection requiring pattern recognition
- Inventory management decisions
- Customer communication personalization
- Business process optimization

## 🧠 LLM-Driven Control Flow

**The LLM (GPT-4) controls ALL decision-making processes:**

### 1. Order Processing Decisions
```python
# LLM decides: approve, review, reject, or escalate
decision = await llm_service.analyze_order(order_data)
if decision.action == "approve":
   ` await process_payment()
eli`f decision.action == "review":
   ` await flag_for_manual_review(decision.reason)

````



### 2. Fraud Detection Logic

```python
# LLM analyzes patterns and makes fraud assessments

fraud_analysis = await llm_service.detect_fraud(order, customer_history)

risk_level = fraud_analysis.risk_score
```


### 3. Inventory Management


```python
# LLM decides reorder quantities and timing

inventory_decision = await llm_service.analyze_inventory(stock_levels, trends)
if inventory_decision.should_reorder:
    await place_supplier_order(inventory_decision.quantity)


```

### 4. Customer Communication


```python
# LLM generates personalized messages
message = await llm_service.generate_customer_message(context, customer_profile)

javascript
await send_communication(customer.email, message)
```

### 5. Business Analytics

javascript
```python
# LLM provides insights and recommendations
insights = await llm_service.analyze_business_metrics(sales_data, trends)
recommendations = insights.optimization_suggestions

```javascript


## javascript🏗️ Production-Ready Architecture

### Backend (FastAPI + Python)

```javascript
app/

├──javascript agent/
│   └── core.py              # Main LLM-driven orchestrator
├── services/

│ __└── llm_servic__.py      # OpenAI GPT-4 integration
├─__models/__
│ __└── schemas.py    __     # Pydantic data models
____
├─____javascript utils/
____│   └── helpers.py           # Utility functions
└─__main.py       __         # FastAPI application
____
``____
____
##__Frontend (React + __peScript)
__
__
``__avas__ipt
cl__nt/__
├─__src/__
____
│ __├── components__         # Reusable UI components

│ __├── pag__/              # Application pages
│ __└── services/     __    # API integration
└─__package.json__

``____
____
##__Production Fea__res
____
- __Error Handling__: Comprehensive exception management

- __Logging__: Structured logging with rotation
- __Environment Config__: Secure environment variable management
- __API Documenta
tion__: Auto-generated OpenAPI/Swagger docs
- __CORS__: Proper cross-origin resource sharing

- __Health Checks__: System monitoring endpoints
- __Docker Support__: Containerized deployment
- __Testing__: Unit and integration test suite


## 🚀 Quick Start

### Prerequisites

- Python 3.11+

- Node.js 18+
- OpenAI API Key

### Installation

```bash
# Clone repository
git clone https://github.com/alimarjan/E-commerce-Agent.git
cd E-commerce-Agent


# __tup envi__nment
cp__en__v.example .env
# __d your OPENAI_API__EY to .env file
____
# Run application (automated setup)
chmod +x start.sh
./start.sh
```

____
###__anual Setup__
____
``___sh___
# __ckend setup__
py__on -m venv venv__

so___e ven__bin/__tivate
____pip install -r requirements.txt
____
____# Frontend setup
cd client


npm__nstal__
cd ____
____
# ___rt bac___d
cd__pp__
uv__orn main:app --re__ad --host 0.0.0.0 --port 8000 &

_______# S__rt frontend__cd __ient__npm__un dev__    _______ ## __ Application__RLs
_______
- ___ronten___: http://localhost:5173
- __Backend API__: http://localhost:8000
- __API Documentati
on__:
 http://localhost:8000/docs
- ___ealth__heck__: http://localhos ____ ## __ LLM Dec__ion Examples ____ ### Order Processing Flow   1. __Input__: New order received 2. __LLM Analysis__: Evaluates customer, products, payment, shipping
3. __Decision__: Approve/Review/Reject with reasoning
4. __Action__: Automated processing based on LLM decision

### Fraud Detection Flow


1. __Input__: Order + customer hist 2. __LLM Analysis__: Pattern recogn 3. __Decision__: Risk score and recommended 4. __Action__: Block/Allow/Flag for revie  ### Inventory Management Flow  1. __Input__: Current stock levels + sales trends + seasonality 2. __LLM Analysis__: Demand forecasting and optimization
3. __Decision__: Reorder recommendations with quantities
4. __Ac
tion__: Automated supplier communications

## 🔧 API Endpoints


| Endpoint | Method | Description | |----------|--------|-------------| | `/` | GET | Application info and status | | `/health` | GET | System health check | | `/api/orders/process` | POST | Process new order (LLM-driven) | | `/api/orders/{id}/status` | GET | Get order status | | `/api/inventory/check` | POST | Inventory analysis (LLM-driven) | | `/api/analytics/dashboard` | GET | Business insights (LLM-generated) | | `/api/communication/send` | POST | Send customer message (LLM-generated) |

## 🧪 Testing the Age

nt

### Test Order Processingt"s/localhost:8000/health
```

## 📈 Production Deployment
ki### Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=False
```


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
