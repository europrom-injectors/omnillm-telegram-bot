# See: https://github.com/coleam00/ottomator-agents/blob/main/pydantic-github-agent/studio-integration-version/github_agent_endpoint.py
from .endpoint import agent_endpoint
from .deps import Dependencies

__all__ = ["agent_endpoint", "Dependencies"]
