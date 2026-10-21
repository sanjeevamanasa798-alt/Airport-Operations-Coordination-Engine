from typing import TypedDict


class AirportState(TypedDict):
    workflow_id: str
    airport: str
    problem: str
    findings: list[str]
    plan: str
    status: str