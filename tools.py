import requests
from agents import function_tool

API_BASE = (
    "https://store-admin-farooq.vercel.app/api/"
    "f887dc57-d660-43d5-8fcf-afd6748cf9d9/billboards"
)


@function_tool
def fetch_all_billboards() -> dict:
    try:
        response = requests.get(API_BASE)
        response.raise_for_status()
        return {"billboards": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@function_tool
def fetch_billboard_by_id(billboard_id: str) -> dict:
    try:
        url = f"{API_BASE}/{billboard_id}"
        response = requests.get(url)
        response.raise_for_status()
        return {"billboard": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@function_tool
def create_billboard(label: str, imageUrl: str) -> dict:
    """
    Creates a new billboard.
    """
    try:
        data = {"label": label, "imageUrl": imageUrl}
        response = requests.post(API_BASE, json=data)
        response.raise_for_status()
        return {"success": True, "billboard": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@function_tool
def update_billboard(billboard_id: str, label: str, imageUrl: str) -> dict:
    """
    Updates an existing billboard.
    """
    try:
        url = f"{API_BASE}/{billboard_id}"
        data = {"label": label, "imageUrl": imageUrl}
        response = requests.patch(url, json=data)
        response.raise_for_status()
        return {"success": True, "billboard": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@function_tool
def delete_billboard(billboard_id: str) -> dict:
    """
    Deletes a billboard by ID.
    """
    try:
        url = f"{API_BASE}/{billboard_id}"
        response = requests.delete(url)
        response.raise_for_status()
        return {"success": True}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
