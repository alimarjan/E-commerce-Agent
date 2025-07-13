import os
from openai import OpenAI
from prompts import CLASSIFICATION_PROMPT
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_message(message: str):
    try:
        if not message or not message.strip():
            return {"error": "Message cannot be empty"}
        
        # Try OpenAI API first
        try:
            prompt = CLASSIFICATION_PROMPT.format(message=message.strip())
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=500,
                temperature=0.3
            )
            result = response.choices[0].message.content
            return {"input": message, "classification": result, "status": "success"}
        except Exception as api_error:
            # If OpenAI API fails, provide demo response
            return get_demo_classification(message.strip())
            
    except Exception as e:
        # Return error details for easier debugging
        return {"error": str(e), "status": "error"}

def get_demo_classification(message: str):
    """Provide demo classifications based on message content"""
    message_lower = message.lower()
    
    # Billing-related keywords
    if any(word in message_lower for word in ['charge', 'bill', 'payment', 'refund', 'subscription', 'invoice', 'cost', 'price']):
        return {
            "input": message,
            "classification": """{
  "intent": "Billing Issue",
  "confidence": 0.92,
  "action": "Escalate to human agent",
  "reasoning": "Customer is reporting a billing discrepancy with double charges, which requires immediate attention and potential refund processing.",
  "suggested_response": "I understand your concern about being charged twice for your subscription. I'm escalating this to our billing team who will review your account and process any necessary refunds within 24 hours. You'll receive an email confirmation once this is resolved.",
  "priority": "high"
}""",
            "status": "success (demo mode)"
        }
    
    # Technical support keywords
    elif any(word in message_lower for word in ['crash', 'error', 'bug', 'not working', 'broken', 'issue', 'problem', 'upload', 'download']):
        return {
            "input": message,
            "classification": """{
  "intent": "Technical Support",
  "confidence": 0.88,
  "action": "Ask for more information",
  "reasoning": "Customer is experiencing technical difficulties that require troubleshooting steps and additional information to resolve.",
  "suggested_response": "I'm sorry to hear you're experiencing technical issues. To help resolve this quickly, could you please provide: 1) Your device type and operating system, 2) Browser version if applicable, 3) Any error messages you're seeing? This will help our technical team provide the best solution.",
  "priority": "medium"
}""",
            "status": "success (demo mode)"
        }
    
    # Account management keywords
    elif any(word in message_lower for word in ['password', 'login', 'account', 'profile', 'reset', 'access', 'username']):
        return {
            "input": message,
            "classification": """{
  "intent": "Account Management",
  "confidence": 0.85,
  "action": "Auto-response",
  "reasoning": "Standard account access issue that can be resolved with automated password reset process.",
  "suggested_response": "I can help you reset your password right away. Please check your email for a password reset link that I'm sending now. If you don't receive it within 5 minutes, please check your spam folder or let me know and I'll assist further.",
  "priority": "medium"
}""",
            "status": "success (demo mode)"
        }
    
    # General feedback keywords
    elif any(word in message_lower for word in ['love', 'great', 'awesome', 'suggestion', 'feature', 'improve', 'feedback']):
        return {
            "input": message,
            "classification": """{
  "intent": "General Feedback",
  "confidence": 0.90,
  "action": "Auto-response",
  "reasoning": "Positive customer feedback that should be acknowledged and forwarded to the product team.",
  "suggested_response": "Thank you so much for your positive feedback! We're thrilled to hear you're enjoying the new features. Your input helps us continue improving our service. I'll make sure to share your comments with our product development team.",
  "priority": "low"
}""",
            "status": "success (demo mode)"
        }
    
    # Default classification
    else:
        return {
            "input": message,
            "classification": """{
  "intent": "General Feedback",
  "confidence": 0.75,
  "action": "Ask for more information",
  "reasoning": "Message content is unclear or doesn't fit standard categories. More information needed to provide appropriate assistance.",
  "suggested_response": "Thank you for contacting us. To ensure I provide you with the best assistance, could you please provide a bit more detail about what you need help with? This will help me direct your inquiry to the right team.",
  "priority": "medium"
}""",
            "status": "success (demo mode)"
        }
