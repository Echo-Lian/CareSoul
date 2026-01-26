import os
import sys
import logging
from dotenv import load_dotenv

# Import the logic from your internal modules
from processor import load_and_chunk_docs
from database import sync_to_supabase

# 1. Setup Logging (Essential for production-grade software)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def main():
    # 2. Load environment variables
    load_dotenv()
    
    # Validation: Catch missing config early
    required_vars = ['SUPABASE_URL', 'SUPABASE_KEY', 'AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_ENDPOINT', 'AZURE_OPENAI_DEPLOYMENT_NAME', 'AZURE_OPENAI_API_VERSION']
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        logger.error(f"Missing environment variables: {', '.join(missing)}")
        return

    # 3. Define Paths
    # Ensure this directory exists and contains your clinical PDFs/TXTs
    DATA_DIR = "./data"
    
    if not os.path.exists(DATA_DIR):
        logger.error(f"Data directory '{DATA_DIR}' not found. Create it and add your PDFs.")
        return

    try:
        # 4. Phase 1: Load and Chunk
        logger.info("Starting document processing...")
        chunks = load_and_chunk_docs(DATA_DIR)
        
        if not chunks:
            logger.warning("No documents found or chunks created. Check your data folder.")
            return
            
        logger.info(f"Successfully created {len(chunks)} chunks with metadata.")

        # 5. Phase 1: Sync to Vector Database (pgvector)
        logger.info("Syncing to Supabase pgvector...")
        sync_to_supabase(
            chunks=chunks,
            supabase_url=os.getenv("SUPABASE_URL"),
            supabase_key=os.getenv("SUPABASE_KEY"),
            azure_openai_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_openai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_openai_deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            azure_openai_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
        
        logger.info("Pipeline execution completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred during the pipeline: {str(e)}")

if __name__ == "__main__":
    main()