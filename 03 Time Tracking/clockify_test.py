import requests

key = "XtQRoKauzTS8sYKC"

workspaceId = "5e154e58b4e9df33319d3294"

# response = requests.get(f"/workspaces/{workspaceId}/projects")
response = requests.get(f"https://api.clockify.me/api/v1/user",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC"
    }
)
print(response)