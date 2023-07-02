from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    name: str = "microservice"
    env: str = "dev"
    debug: bool = False
