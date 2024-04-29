from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings_yaml import YamlBaseSettings

from utils.consts import BASE_DIR


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
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings().database

    app: AppSettings = AppSettings()

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
