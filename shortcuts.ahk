#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.


^\:: Run, C:\Program Files\Sublime Text 3\subl.exe, "%A_ScriptDir%.shortcuts.ahk"
^+d::Run "C:\Users\Adrian\Downloads"


#g:: ; Google search selected Texts
	;	send, ^c
	;	Sleep, 100
	run http://www.google.com/search?q=%Clipboard%
return


; Press ~ to move up a folder in Explorer
	#IfWinActive, ahk_class CabinetWClass
	`::Send !{Up} 
	#IfWinActive
	return

::\\n::Adrian Danao-Schroeder
::\\e::adriandanao@gmail.com
::\\w::adriandanao.com
::\\p::301-318-6809
::\\in::https://www.linkedin.com/in/adrian-danao-schroeder-a85698155/
::\\umd::adanaosc@umd.edu
::\\uid::114097347
::\\ln::Danao-Schroeder
::\\cn::{U+8BB8}{U+9053}{U+8FDC} ; 许道远
::\\ae::Aerospace Engineering
::\\umcp::University of Maryland College Park
::\\1c1::13032869076




;		Addresses
	::\\cp::8705 36th Av.`nCollege Park, MD `n20740
	::\\ss::2308 Peggy Ln.`nSilver Spring, MD `n20910

;		Dates
	::\\jan::January
	::\\feb::February
	::\\mar::March
	::\\apr::April
	::\\jun::June
	::\\jul::July
	::\\aug::August
	::\\sep::September
	::\\oct::October
	::\\nov::November
	::\\dec::December
	::\\d::
		FormatTime, CurrentDateTime,, yyyy-MM-dd
		SendInput,%CurrentDateTime%
	return
	::--d::
		FormatTime, CurrentDateTime,, yyyy-MM-dd
		SendInput %CurrentDateTime%
	return

	::\\da::
	  FormatTime, CurrentDateTime,,MM/dd/yyyy
	  SendInput %CurrentDateTime%
	return

	::\\df::
	  FormatTime, CurrentDateTime,,MMMM dd, yyyy
	  SendInput %CurrentDateTime%
	return

	::\\m::
		FormatTime, CurrentDateTime,, yyyy-MM
		SendInput,%CurrentDateTime%
	return
	::--m::
		FormatTime, CurrentDateTime,, yyyy-MM
		SendInput %CurrentDateTime%
	return

; 		Common special Charachters 
	::\\nnc::{U+00D1}			; Ñ
	::\\nn::{U+00F1}			; ñ
	::\\ck::{U+2713}			; ✓

; 		Greek
	::\\alpha::{U+03B1}			; α - alpha
	::\\beta::{U+03B2}			; β - beta
	::\\gamma::{U+03B3}			; γ - gamma
	::\\delta::{U+03B4}			; δ - delta
	::\\epislon::{U+03B5}		; ε - epislon
	::\\zeta::{U+03B6}			; ζ - zeta
	::\\eta::{U+03B7}			; η - eta
	::\\theta::{U+03B8}			; θ - theta
	::\\iota::{U+03B9}			; ι - iota
	::\\kappa::{U+03BA}			; κ - kappa
	::\\lamda::{U+03BB}			; λ - lamda
	::\\mu::{U+03BC}			; μ - mu
	::\\nu::{U+03BD}			; ν - nu
	::\\xi::{U+03BE}			; ξ - xi
	::\\omicron::{U+03BF}		; ο - omicron
	::\\pi::{U+03C0}			; π - pi
	::\\rho::{U+03C1}			; ρ - rho
	::\\sigma::{U+03C3}			; σ - sigma
	::\\tau::{U+03C4}			; τ - tau
	::\\upsilon::{U+03C5}		; υ - upsilon
	::\\phi::{U+03C6}			; φ - phi
	::\\chi::{U+03C7}			; χ - chi
	::\\psi::{U+03C8}			; ψ - psi
	::\\omega::{U+03C9}			; ω - omega
	::\\epsilon::{U+03B5}		; ε - epsilon
	::\\Alphac::{U+0391}		; Α - ALPHA
	::\\Betac::{U+0392}			; Β - BETA
	::\\Gammac::{U+0393}		; Γ - GAMMA
	::\\Deltac::{U+0394}		; Δ - DELTA
	::\\Epsilonc::{U+0395}		; Ε - EPISLON
	::\\Zetac::{U+0396}			; Ζ - ZETA
	::\\Etac::{U+0397}			; Η - ETA
	::\\Thetac::{U+0398}		; Θ - THETA
	::\\Iotac::{U+0399}			; Ι - IOTA
	::\\Kappac::{U+039A}		; Κ - KAPPA
	::\\Lambdac::{U+039B}		; Λ - LAMDA
	::\\Muc::{U+039C}			; Μ - MU
	::\\Nuc::{U+039D}			; Ν - NU
	::\\Xic::{U+039E}			; Ξ - XI
	::\\Omicronc::{U+039F}		; Ο - OMICRON
	::\\Pic::{U+03A0}			; Π - PI
	::\\Rhoc::{U+03A1}			; Ρ - RHO
	::\\Sigmac::{U+03A3}		; Σ - SIGMA
	::\\Tauc::{U+03A4}			; Τ - TAU
	::\\Upsilonc::{U+03A5}		; Υ - UPSILON
	::\\Phic::{U+03A6}			; Φ - PHI
	::\\Chic::{U+03A7}			; Χ - CHI
	::\\Psic::{U+03A8}			; Ψ - PSI
	::\\Omegac::{U+03A9}		; Ω - OMEGA

; 		Math
	::\\pm::{U+00B1} 			; ( ± ) plus-minus
	::\\inf::{U+221E} 			; ( ∞ ) infinity
	::\\approx::{U+2248} 		; ( ≈ ) almost equal
	::\\ne::{U+2260} 			; ( ≠ ) not equal
	::\\def::{U+2261} 			; ( ≡ ) equivalent to
	::\\lte::{U+2264} 			; ( ≤ ) less than or equal
	::\\gte::{U+2265} 			; ( ≥ ) greater than or equal
	::\\sqrt::{U+221A} 			; ( √ ) square root
	::\\int::{U+222B} 			; ( ∫ ) integral
	::\\deg::{U+00BA} 			; ( º ) power zero ; degree
	::\\p1::{U+00B9} 			; ( ¹ ) power one ; linear
	::\\p2::{U+00B2} 			; ( ² ) power two ; squared
	::\\p3::{U+00B3} 			; ( ³ ) power three ; cubed
	::\\12::{U+00BD}        	; ( ½ )

;		Common Acronyms			
	::\\prc::People's Republic of China
	::\\gmd::Guomingdang
	::\\ccp::Chinese Communist Party
	::\\us::United States
	::\\usa::United States of America


