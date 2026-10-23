# Expense Tracker Assistant

A Python-based expense tracker that allows users to manage their income and expenses manually or with the help of an AI assistant.

## Features

- **Manual Transaction Entry:** Add income and expense transactions manually.
- **AI-Powered Transaction Entry:** Describe a transaction in natural language and let the AI extract its details.
- **LLM Tool Calling:** Extract structured transaction data using an LLM tool-calling mechanism.
- **Data Validation:** Validate transaction types, categories, titles, amounts, and dates before saving.
- **JSON Persistence:** Store transactions in a local JSON file and load them when the application starts.
- **Financial Summary:** Calculate total income, total expenses, and the current balance.
- **Error Handling:** Handle errors during AI requests and unexpected tool responses.

## Technologies Used

- Python
- REST APIs
- LLM Tool Calling
- JSON
- `requests`
- `python-dotenv`

## Project Structure

```text
expense-tracker/
├── main.py
├── llm_client.py
├── .env
├── .gitignore
├── README.md
└── transactions.json
```

- `main.py`: Handles the main application logic, transaction management, validation, and financial summaries.
- `llm_client.py`: Communicates with the AI API and processes tool calls.
- `.env`: Stores the API key locally.
- `.gitignore`: Specifies files that should not be tracked by Git.
- `README.md`: Documents the project.
