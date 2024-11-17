from supabase import create_client, Client
from core.config import settings
from typing import Optional

class SupabaseClient:
    _instance: Optional[Client] = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._instance is None:
            try:
                cls._instance = create_client(
                    settings.SUPABASE_URL,
                    settings.SUPABASE_KEY
                )
            except Exception as e:
                raise ConnectionError(f"Failed to connect to Supabase: {str(e)}")
        return cls._instance

supabase = SupabaseClient.get_client()
