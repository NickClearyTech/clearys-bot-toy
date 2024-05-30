from typing import Optional, List
import os

from pydantic import BaseModel, HttpUrl


class GitHubConfiig(BaseModel):
    owner: Optional[str]
    repo: Optional[str]
    workflow_name: Optional[str]
    token: Optional[str] = os.getenv("GITHUB_TOKEN", None)


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
    taytay: MemeConfig


class LibreTranslateServerConfig(BaseModel):
    url: str
    default_language: str


class Config(BaseModel):
    libretranslate_server_config: LibreTranslateServerConfig
    discord_server_id: int
    all_memes_config: AllMemesConfig
    github: GitHubConfiig
