#WinActivateForce
DetectHiddenWindows, On

; getSpotifyHwnd() {
; 	WinGet, spotifyHwnd, ID, ahk_exe spotify.exe
; 	; We need the app's third top level window, so get next twice.
; 	spotifyHwnd := DllCall("GetWindow", "uint", spotifyHwnd, "uint", 2)
; 	spotifyHwnd := DllCall("GetWindow", "uint", spotifyHwnd, "uint", 2)
; 	SetFormat, IntegerFast, hex
; 	Return spotifyHwnd
; }

; ; Send a key to Spotify.
; spotifyKey(key) {
; 	spotifyHwnd := getSpotifyHwnd()
; 	; Chromium ignores keys when it isn't focused.
; 	; Focus the document window without bringing the app to the foreground.
; 	ControlFocus, Chrome_RenderWidgetHostHWND1, ahk_id %spotifyHwnd%
; 	ControlSend, , %key%, ahk_id %spotifyHwnd%
; 	Return
; }

; spotifyHwnd := getSpotifyHwnd()

; f2:: 	
; 	SendInput, {Volume_Down}
; 	SoundSet, -8
; Return
; f3:: 	
; 	SendInput, {Volume_Up}
; 	SoundSet, +8

; Return
; f4:: 	SendInput, {Media_Prev}
; f6:: 	SendInput, {Media_Play_Pause}	
; f7:: 	SendInput, {Media_Next}

; F13::
; {	
; 	currHwnd := WinExist("A")
; 	spotifyHwnd := getSpotifyHwnd()
; 	if (currHwnd=spotifyHwnd)
; 	{
; 		Winactivate, ahk_id %prevHwnd%
; 		Return
; 	}
; 	Else
; 	{
; 		prevHwnd := currHwnd
; 		WinActivate, ahk_id %spotifyHwnd%
; 		Return
; 	}
; }