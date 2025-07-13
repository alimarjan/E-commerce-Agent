
CLASSIFICATION_PROMPT = """
You are an AI support agent classifier. Analyze the customer message and provide a structured classification.

CATEGORIES:
- Billing Issue: Payment problems, subscription issues, refunds, pricing questions
- Technical Support: Bug reports, feature not working, installation problems, performance issues
- Account Management: Login issues, password reset, profile changes, account deletion
- General Feedback: Suggestions, compliments, complaints, feature requests

ACTIONS:
- Auto-response: Simple issues that can be resolved with a standard response
- Ask for more information: Need additional details to help effectively
- Escalate to human agent: Complex issues requiring human intervention

Analyze this message and respond in JSON format:
{{
  "intent": "<category>",
  "confidence": <0.0-1.0>,
  "action": "<action>",
  "reasoning": "<brief explanation>",
  "suggested_response": "<helpful response to customer>",
  "priority": "<low|medium|high>"
}}

Customer Message: {message}
"""
