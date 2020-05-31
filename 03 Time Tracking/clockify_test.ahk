key = "XtQRoKauzTS8sYKC"

oWhr := ComObjCreate("WinHttp.WinHttpRequest.5.1")
oWhr.Open("GET", "/workspaces/{workspaceId}/clients", false)
oWhr.SetRequestHeader("Content-Type", "application/json")
oWhr.SetRequestHeader("Authorization", "Bearer 80b44ea9c302237f9178a137d9e86deb-20083fb12d9579469f24afa80816066b")
oWhr.Send()
MsgBox, % oWhr.ResponseText