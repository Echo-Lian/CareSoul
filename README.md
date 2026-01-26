# CareSoul

This application demonstrates a production-grade mental health AI application.

## Structure
project-root/
├── data/               # Raw PDFs/TXTs clinical guides
├── src/
│   ├── processor.py    # Logic for chunking and metadata
│   ├── database.py     # Supabase/pgvector connection
│   └── main.py         # The entry script to run the pipeline
├── .env                # API Keys
└── requirements.txt  # Python dependencies