
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent import classify_message
from schemas import MessageRequest, ClassificationResponse, HealthResponse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LLM Support Agent API",
    description="AI-powered support ticket classification system",
    version="1.0.0"
)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Added Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "LLM Support Agent API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "LLM Support Agent"}

@app.post("/classify")
async def classify(request: MessageRequest):
    try:
        logger.info(f"Received classification request for message: {request.message[:50]}...")
        result = classify_message(request.message)
        
        if "error" in result:
            logger.error(f"Classification error: {result['error']}")
            raise HTTPException(status_code=400, detail=result["error"])
        
        logger.info("Classification completed successfully")
        return result
    except Exception as e:
        logger.error(f"Unexpected error in classify endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
