# Test Cases — Language Translation Tool

| Test | Input | Expected result |
|---|---|---|
| Empty input | Leave text area blank and press Translate | A warning asks for text |
| English to Zulu | "Good morning" | A translated result is displayed when service is available |
| Auto detect | Select Auto detect and enter a sentence | The service attempts to detect the source language |
| Same language | Select English as source and target | App asks user to choose different languages |
| No internet | Disconnect internet and translate | A clear error message is displayed |
