from dataclasses import dataclass
from typing import Any


@dataclass
class AgentMessage:
    sender: str
    receiver: str
    task: str
    payload: Any