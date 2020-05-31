import requests
import json
import pprint
from datetime import datetime 
import calendar

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
    response = requests.post(f"https://api.clockify.me/api/v1//workspaces/{workspaceId}/time-entries",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    },
    json = {
        # "id": taskId,
        # "start": str(datetime.timestamp(now)),
        "start": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description": "Testing with python",
        "projectId": "5ed2eaf88092f06db020247f",
        "taskId": taskId,
        # "taskId": '5ed2eb3de240581b7e175f66',
        # "tagIds": [
        #     "string"
        # ]
        
    }
    )
    return response.json()

def stop_task():
    workspaceId = "5e154e58b4e9df33319d3294"
    response = requests.put(f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries/endStarted",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    },
    json = {
        # "body": "StopTimeEntryRequest",
        # "id": "5ed4372b05734533ebef3313",
        # "message":"test",
        "end": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    },
    )
    return response.json()


def get_running_entry():
    workspaceId = "5e154e58b4e9df33319d3294"
    response = requests.post(f"https://api.clockify.me/api/v1//workspaces/{workspaceId}/time-entries",
    headers = {
        "X-Api-Key": "XtQRoKauzTS8sYKC",
        "content-type": "application/json"
    },
    json = {
        # "id": taskId,
        # "start": str(datetime.timestamp(now)),
        "start": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description": "Testing with python",
        "projectId": "5ed2eaf88092f06db020247f",
        "taskId": taskId,
        # "taskId": '5ed2eb3de240581b7e175f66',
        # "tagIds": [
        #     "string"
        # ]
        
    }
    return response.json()
    
pprint.pprint(stop_task())
# pprint.pprint(start_task('5ed2eb3de240581b7e175f66'))