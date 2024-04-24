from typing import Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings_yaml import YamlBaseSettings


class Database(BaseModel):
    host: Optional[str] = "localhost"
    port: Optional[int] = 5432
    user: Optional[str] = "postgres"
    password: Optional[str] = "postgres"
    name: Optional[str] = "postgres"


class AppSettings(YamlBaseSettings):
    host: Optional[str] = "localhost"
    port: Optional[int] = 8001

    class Config:
        yaml_file="config.yaml"


class DbSettings(YamlBaseSettings):
    database: Database

    class Config:
        yaml_file="config.yaml"


class AuthJWT(BaseModel):
    pass


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings().database

    app: AppSettings = AppSettings()

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
