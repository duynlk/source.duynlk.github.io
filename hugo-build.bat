hugo-toc.exe
set /p msg="Message for commit: "
@RD /S /Q ".\public"
hugo -D
git add .
git commit -m "%msg%"
git push
xcopy /s /y public ..\duyka-public
cd ..
cd duynlk.github.io
git add .
git commit -m "%msg%"
git push
pause