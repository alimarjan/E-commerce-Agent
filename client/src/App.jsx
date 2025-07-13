import { useState } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!message.trim()) {
      setError('Please enter a message')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://localhost:8000/classify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message.trim() }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Failed to classify message')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleClear = () => {
    setMessage('')
    setResult(null)
    setError(null)
  }

  const parseClassification = (classification) => {
    try {
      return JSON.parse(classification)
    } catch {
      // Fallback for non-JSON responses
      return { raw: classification }
    }
  }

  const getPriorityColor = (priority) => {
    switch (priority?.toLowerCase()) {
      case 'high': return 'priority-high'
      case 'medium': return 'priority-medium'
      case 'low': return 'priority-low'
      default: return 'priority-default'
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🤖 LLM Support Agent</h1>
        <p>AI-powered customer support message classification</p>
      </header>

      <main className="app-main">
        <form onSubmit={handleSubmit} className="message-form">
          <div className="form-group">
            <label htmlFor="message">Customer Message:</label>
            <textarea
              id="message"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Enter a customer support message to classify..."
              rows={4}
              disabled={loading}
            />
          </div>
          
          <div className="form-actions">
            <button type="submit" disabled={loading || !message.trim()}>
              {loading ? 'Classifying...' : 'Classify Message'}
            </button>
            <button type="button" onClick={handleClear} disabled={loading}>
              Clear
            </button>
          </div>
        </form>

        {error && (
          <div className="error-message">
            <h3>❌ Error</h3>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="result-container">
            <h3>📊 Classification Result</h3>
            
            <div className="result-grid">
              <div className="result-card">
                <h4>Original Message</h4>
                <p className="original-message">{result.input}</p>
              </div>

              {result.classification && (() => {
                const parsed = parseClassification(result.classification)
                
                if (parsed.raw) {
                  return (
                    <div className="result-card">
                      <h4>Classification</h4>
                      <pre className="raw-classification">{parsed.raw}</pre>
                    </div>
                  )
                }

                return (
                  <>
                    <div className="result-card">
                      <h4>Intent & Action</h4>
                      <div className="intent-info">
                        <span className="intent-badge">{parsed.intent}</span>
                        <span className={`priority-badge ${getPriorityColor(parsed.priority)}`}>
                          {parsed.priority || 'medium'} priority
                        </span>
                      </div>
                      <p><strong>Action:</strong> {parsed.action}</p>
                      <p><strong>Confidence:</strong> {(parsed.confidence * 100).toFixed(1)}%</p>
                    </div>

                    <div className="result-card">
                      <h4>Analysis</h4>
                      <p><strong>Reasoning:</strong> {parsed.reasoning}</p>
                    </div>

                    <div className="result-card suggested-response">
                      <h4>Suggested Response</h4>
                      <p>{parsed.suggested_response}</p>
                    </div>
                  </>
                )
              })()}
            </div>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>Powered by OpenAI GPT-4 • Built with React & FastAPI</p>
      </footer>
    </div>
  )
}

export default App
