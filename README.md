# CareSoul

This application demonstrates a production-grade mental health AI application.

## Structure
```
project-root/
├── data/               # Raw PDFs/TXTs clinical guides
├── src/
│   ├── processor.py    # Logic for chunking and metadata
│   ├── database.py     # Supabase/pgvector connection
│   └── main.py         # The entry script to run the pipeline
├── .env                # API Keys
└── requirements.txt    # Python dependencies
```

## Features
### Clinical Grounding

The application avoids scraping blog posts, instead, it uses structured, evidence-based frameworks to demonstrate an understanding of the industry's high standards for accuracy, such as:
- **CBT Manuals**
- **WHO Guidelines**
- **Crisis Protocols**


### Chunking

Split documents into manageable chunks with metadata.
