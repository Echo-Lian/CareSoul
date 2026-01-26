from supabase.client import create_client
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_openai import AzureOpenAIEmbeddings # Import the Azure-specific class

def sync_to_supabase(chunks, supabase_url, supabase_key, azure_conf):
    # Initialize Azure OpenAI Embeddings
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=azure_conf["deployment_name"],
        openai_api_version=azure_conf["api_version"],
        azure_endpoint=azure_conf["endpoint"],
        api_key=azure_conf["api_key"],
    )
    
    supabase = create_client(supabase_url, supabase_key)
    
    vector_store = SupabaseVectorStore.from_documents(
        chunks,
        embeddings,
        client=supabase,
        table_name="documents",
        query_name="match_documents",
    )
    print(f"Successfully synced {len(chunks)} chunks to Supabase via Azure.")