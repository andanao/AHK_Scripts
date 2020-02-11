#WinActivateForce
DetectHiddenWindows, On
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.


~Volume_Down::	SoundSet, -8 Return
~Volume_Up::	SoundSet, +8 Return

CapsLock::Ctrl

::;;e::adrian.danao.schroeder@ses.com
::;;n::Adrian Danao-Schroeder
::;;u::adanaos
::;;p::202-924-7073


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

