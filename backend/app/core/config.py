from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    client_id: str
    twitch_broadcaster_id: str
    twitch_access_token: str


settings = Settings()