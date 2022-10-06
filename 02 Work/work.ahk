#WinActivateForce
DetectHiddenWindows, On
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.


~Volume_Down::	SoundSet, -8 Return
~Volume_Up::	SoundSet, +8 Return

CapsLock::Ctrl


::;;d::
	FormatTime, CurrentDateTime,, yyyy-MM-dd
	SendInput,%CurrentDateTime%
return

::;;dl::
	FormatTime, CurrentDateTime,, yyyy-MM-dd HH:mm:ss
	SendInput %CurrentDateTime%
return

::;;da::
	FormatTime, CurrentDateTime,,MM/dd/yyyy
	SendInput %CurrentDateTime%
return

::;;df::
	FormatTime, CurrentDateTime,,MMMM dd, yyyy
	SendInput %CurrentDateTime%
return

