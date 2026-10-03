from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSetting(BaseSettings):

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )


dbSetting = DatabaseSetting()
