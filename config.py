from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Class for storing app settings.
    """

    SECRET_KEY: str

    class Config:
        """
        Configuration class for settings.
        """

        env_file = ".env"
        case_sensitive = True

settings = Settings()
