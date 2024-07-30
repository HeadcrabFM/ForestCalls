@echo off
REM Set code page to UTF-8
chcp 65001 >nul


set repname = "FOREST CALLS CONSOLE TEXT RPG"
set branch = "master"


echo 				* * * * * * * *
echo 				*             *
echo 				*      R      *
echo 				*      A      *
echo 				*    A V E    *
echo 				*      E      *
echo 				*             *
echo 				* * * * * * * *
echo 					 2024
echo .
echo .
echo .
echo Сейчас будет произведено ОБНОВЛЕНИЕ
echo УДАЛЁННОГО РЕПОЗИТОРИЯ
echo					%repname%
echo НА ГИТХАБЕ.
echo (интеграция результатов работы в локальной папке
echo в систему контроля версий в облаке).
echo ------------------------------------------------------------------------
echo Пожалуйста, следуйте указаниям на экране и читайте вывод консоли.
echo Успешность обновления Гитхаба можно проверить в браузере.
echo Если что-то сломалось, пляши, хуле :D
echo ------------------------------------------------------------------------
echo 		gs@cosyma.pro			+79217916237				    
echo ------------------------------------------------------------------------

:: Запрос комментария для коммита
set /p comment="Комментарий:      "

echo ------------------------------------------------------------------------

:: Добавление всех изменений в индекс
git add .

:: Коммит с пользовательским сообщением
git commit -m "%comment%"

:: Пуш изменений в ветку '%branch%' на удаленный репозиторий 'origin'
git push -u origin %branch%

echo ------------------------------------------------------------------------

:: Подтверждение завершения
echo Скрипт завершил работу, файлы загружены в систему контроля версий.
echo пожалуйста, проверьте успешность через браузер, в случае неудачи
echo следуйте указаниям в консоли выше, либо обратитесь к админу

endlocal
pause