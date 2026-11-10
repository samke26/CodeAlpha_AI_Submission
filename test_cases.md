# Test Cases — FAQ Chatbot

| Test | Input | Expected result |
|---|---|---|
| Exact match | "How do I reset my password?" | Password reset guidance |
| Similar wording | "I forgot my login password" | Closest password FAQ response, if similarity is sufficient |
| Assignment query | "How can I upload my assignment?" | Assignment submission guidance |
| Unrelated query | "What is the weather?" | Fallback response |
| Empty input | Submit no text | Chat input does not send an empty question |
