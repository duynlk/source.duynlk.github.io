:loop
set /p filename="New file: "
set filename = %filename%
set "cmd=posts\"
set "ext=.md"
hugo new %cmd%%filename%%ext%
goto loop
:exitloop
pause