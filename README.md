# financial-summary- version 1


## Overview

This project is a web-based AI system that **analyzes bank statements in PDF format** and generates a **structured financial summary** using AI agents. It extracts key financial insights such as:

- Opening and closing balances

- Top income and spend transactions

- Bank charges

  

## Core Components

  

### 1. PDF Upload (Flask API)

- Provides a REST API endpoint (`/summary`) to upload PDF bank statements.

  

### 2. PDF Parsing & Table Extraction

- Uses `Camelot` to extract tables from PDFs.

- Dynamically selects the parsing mode (`lattice` or `stream`).

- Handles unsupported/scanned PDFs gracefully.

  

### 3. Information Extraction (AI Agent System)

- Utilizes **CrewAI** to run specialized agents:

-  **Extractor Agent**: Identifies relevant financial data.

-  **Summarizer Agent**: Organizes the data into meaningful insights.

-  **Proofreader Agent**: Ensures summary accuracy and clarity.

  

### 4. Summary Output

- Returns structured JSON:


  

### 5. Tech stack


- Backend: Flask

- PDF Parsing: Camelot

  

- AI Agents: CrewAI

  

- LLM: OpenAI

  

- Utilities: Tempfile, Pathlib, Logging


### Sample output
{
    "summary": [
        "Opening Balance: -1,00,97,171.54, Date: 02-01-2020",
        "Closing Balance: -99,53,818.04, Date: 31-01-2020",
        "Top 5 Income Transactions:",
        "1. Amount: 3,00,000.00, Source: NEFT NAVA BHARAT PRESS, Date: 02-01-2020",
        "2. Amount: 28,168.00, Source: NEFT EXPRESS GRAPHICS, Date: 02-01-2020",
        "3. Amount: 15,000.00, Source: NEFT DESIGN TEC, Date: 02-01-2020",
        "4. Amount: 3,90,000.00, Source: CC-32 R.D., Date: 02-01-2020",
        "5. Amount: 16,308.00, Source: ACH Bajaj Finanac, Date: 02-01-2020",
        "Top 5 Spend Transactions:",
        "1. Amount: 16,308.00, Category: ACH Bajaj Finanac, Date: 02-01-2020",
        "2. Amount: 3,90,000.00, Category: CC-32 R.D., Date: 02-01-2020",
        "3. Amount: 1,00,000.00, Category: NEFT NAVA BHARAT PRESS, Date: 02-01-2020",
        "4. Amount: 91,009.00, Category: INDIAINFOLINE, Date: 07-01-2020",
        "5. Amount: 1,56,940.00, Category: ALPAP INTERNATIONAL, Date: 07-01-2020",
        "Bank Charges:",
        "1. Type: ATM Fee, Amount: 16,308.00, Date: 02-01-2020",
        "2. Type: NEFT Charge, Amount: 74,352.00, Date: 06-01-2020",
        "3. Type: CGST, Amount: 0.45, Date: 06-01-2020",
        "4. Type: SGST, Amount: 0.45, Date: 06-01-2020",
        "5. Type: Other Fee, Amount: 5.00, Date: 06-01-2020"
    ]
}


### Plan for version 2
- improve accuracy
- try out local llm(ollama)
- reduce response time (version 1 - 1m 35 sec)
- implement vectorisation 
- make an ui using streamlit