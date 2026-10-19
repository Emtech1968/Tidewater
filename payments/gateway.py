"""Chooses the gateway for a payment from config/routing.yaml."""
import yaml
from payments import paygate_a, paygate_b

ROUTING = yaml.safe_load(open("config/routing.yaml"))


def gateway_for(region: str, method: str):
    name = ROUTING.get(region, {}).get(method) or ROUTING["default"][method]
    if name == "paygate-a":
        return paygate_a
    if name == "paygate-b":
        return paygate_b
    raise ValueError(f"unknown gateway {name}")
