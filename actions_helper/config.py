from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GH_TOKEN: str
    storage_filename: str = "storage.pickle"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
