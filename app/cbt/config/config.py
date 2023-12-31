from pydantic import BaseModel, HttpUrl


class MetricsServerConfig(BaseModel):
    url: HttpUrl
    api_key: str


class Config(BaseModel):
    metrics_server_config: MetricsServerConfig
