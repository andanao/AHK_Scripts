#WinActivateForce
#singleinstance force
#Persistent
DetectHiddenWindows, On
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.

; Move mouse if idle
	; ================================================================
	;        Move mouse if idle
	; ================================================================
	; adjust the folowing 3 values to suit your circumstances
	; ================================================================

	inactivity_limit=300	; measured in seconds
	how_often_to_test=1	; measured in seconds
	show_tooltip=0       ; 1=show, anything else means hide

	; ================================================================

	inactivity_limit_ms:=inactivity_limit*1000
	how_often_to_test_ms:=how_often_to_test*1000

	settimer, check_active, %how_often_to_test_ms%

	mm_cnt=0
	return

	; ================================================================
	; test if the mouse and keyboard have been idle

	check_active:

	if show_tooltip=1
	tooltip, % A_TimeIdle "ms`rmoves " mm_cnt


	if A_TimeIdle > %inactivity_limit_ms%
	{
	mousemove,1,1,50, R	; down and right 1 pixel each time
	sleep, 100
	mousemove,-1,-1,50, R
	mm_cnt++	; tally number of times the mouse was artificially moved
	}

	return


	; these hotkeys are diagnostics, disable during normal use

	; Sesc::exitapp	
	; f10::reload