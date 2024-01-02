from typing import Optional, List
import os

from pydantic import BaseModel, HttpUrl


class MetricsServerConfig(BaseModel):
    """
    Configuration for the metrics server
    """

    url: HttpUrl
    api_key: Optional[str] = os.getenv("METRICS_API_KEY", None)


class MemeConfig(BaseModel):
    """
    Represents the users, servers, and channels for which a particular meme will apply to
    """

    users: Optional[List[int]] = None
    servers: Optional[List[int]] = None
    channels: Optional[List[int]] = None


class AllMemesConfig(BaseModel):
    prophet_has_spoken: MemeConfig
    emacs_quotes: MemeConfig
    guix_quotes: MemeConfig
    devops_quotes: MemeConfig
    jenkins: MemeConfig
    caustic: MemeConfig
    chris: MemeConfig


class Config(BaseModel):
    metrics_server_config: MetricsServerConfig
    discord_server_id: int
    all_memes_config: AllMemesConfig
