rem CHAMA O SCRIPT QUE IRA POPULAR AS TAGS DOS ARQUVIVOS DE UMA PLAYLIST
rem BASEADO NUMA PLANILHA CHAMADA TAGS.XLS
rem A TAG SO EH MODIFICADA SE O ARQUIVO AINDA NAO TIVER ARTWORK
rem ESSE SCRIPT TEM UM PARAMETRO QUE DETERMINA SE DEVE MODIFICAR AS TAGS DE ARQUIVOS
rem QUE POSSUEM ART COVER (DELETE ART), ESSE PARAMETRO EH -N BY DEFAULT (NAO DELETAR)
rem CASO -Y SEJA USADA, A COVER TB EH DELETADA SE EXISTIR
cd D:\iTunes\Scripts
cscript Pop_Year_Tag.vbs -Y
pause
