import requests
import json
import pprint

key = "XtQRoKauzTS8sYKC"
userId = '5e154e57b4e9df33319d3293'
workspaceId = "5e154e58b4e9df33319d3294"


def get_projects():
    workspaceId = "5e154e58b4e9df33319d3294"
    response = requests.get(f"https://api.clockify.me/api/v1//workspaces/{workspaceId}/projects",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    }
    )
    return response.json()

def get_tasks(projectId):
    workspaceId = "5e154e58b4e9df33319d3294"
    response = requests.get(f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects/{projectId}/tasks",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    }
    )
    return response.json()

def start_task(taskId):
        workspaceId = "5e154e58b4e9df33319d3294"
    response = requests.get(f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects/{projectId}/tasks",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    }
    )
    return response.json()

pprint.pprint(get_tasks('5ed2eb3de240581b7e175f66'))