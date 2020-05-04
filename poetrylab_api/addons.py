import requests

from .settings import ADDONS


def is_available(operation):
    """Checks wether the service for the operation is defined and listening"""
    if operation in ADDONS:
        health = ADDONS[operation]["health"]
        try:
            response = requests.request(health["method"], health["uri"])
        except Exception as err:
            return {
                "error": (f"Error retrieving health response from "
                          f"{health['uri']}: {str(err)}")
            }
        if response.status_code != health["code"]:
            availability = {
                "error": (f"Error retrieving health response from "
                          f"{health['uri']}. "
                          f"Expected status code {health['code']}, "
                          f"but got {response.status_code}"),
                "status": response.status_code,
                "expected": health["code"],
            }
        else:
            availability = {
                "success": "Health check OK"
            }
    else:
        availability = {
            "error": f"Operation '{operation}' not listed as addon."
        }
    return availability


def perform(operation, poem):
    """Performs the specified operation over poem and returns the result"""
    endpoint = ADDONS[operation]["endpoint"]
    data = {field["name"]: field["type"](poem) for field in endpoint["fields"]}
    try:
        response = requests.request(
            endpoint["method"], endpoint["uri"], data=data
        )
        response_json = response.json()
    except Exception as err:
        return {
            "error": (f"Error retrieving or decoding JSON response from "
                      f"{endpoint['uri']}: {str(err)}")
        }
    if "output" in endpoint:
        return response_json.get(endpoint["output"], response_json)
    else:
        return response_json
