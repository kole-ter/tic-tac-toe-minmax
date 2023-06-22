<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<!--
 /* Font Definitions */
 @font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:"Segoe UI";
	panose-1:2 11 5 2 4 2 4 2 2 3;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0cm;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{margin-top:0cm;
	margin-right:0cm;
	margin-bottom:0cm;
	margin-left:36.0pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;}
p.MsoListParagraphCxSpFirst, li.MsoListParagraphCxSpFirst, div.MsoListParagraphCxSpFirst
	{margin-top:0cm;
	margin-right:0cm;
	margin-bottom:0cm;
	margin-left:36.0pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;}
p.MsoListParagraphCxSpMiddle, li.MsoListParagraphCxSpMiddle, div.MsoListParagraphCxSpMiddle
	{margin-top:0cm;
	margin-right:0cm;
	margin-bottom:0cm;
	margin-left:36.0pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;}
p.MsoListParagraphCxSpLast, li.MsoListParagraphCxSpLast, div.MsoListParagraphCxSpLast
	{margin-top:0cm;
	margin-right:0cm;
	margin-bottom:0cm;
	margin-left:36.0pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;}
.MsoChpDefault
	{font-family:"Calibri",sans-serif;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:72.0pt 72.0pt 72.0pt 72.0pt;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 ol
	{margin-bottom:0cm;}
ul
	{margin-bottom:0cm;}
-->

</head>

<body lang=en-CZ style='word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal><b><span lang=EN-GB style='font-size:24.0pt'>TIC TAC TOE
MINIMAX</span></b></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-GB>Implementation of minimax strategy for tic
tac toe 3x3.</span></p>

<p class=MsoNormal><span lang=EN-GB>Player 1 </span><span lang=EN-GB
style='font-family:Symbol'>=</span><span lang=EN-GB> X</span></p>

<p class=MsoNormal><span lang=EN-GB>Player 2 </span><span lang=EN-GB
style='font-family:Symbol'>=</span><span lang=EN-GB> O</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN-GB style='font-size:16.0pt'>Game Modes</span></b></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoListParagraphCxSpFirst style='text-indent:-18.0pt'><span
lang=EN-GB style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>Player vs. AI (Default setting)</span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'><span
lang=EN-GB style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>Player vs. Random generator</span></p>

<p class=MsoListParagraphCxSpLast style='text-indent:-18.0pt'><span lang=EN-GB
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>Player vs. Player (pvp)</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN-GB style='font-size:16.0pt'>Game
Instructions</span></b></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoListParagraphCxSpFirst style='text-indent:-18.0pt'><span
lang=EN-GB style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>press 'g' to change gamemode (pvp or ai)</span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'><span
lang=EN-GB style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>press '0' to change ai level to 0 (random)</span></p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'><span
lang=EN-GB style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>press '1' to change ai level to 1 (impossible)</span></p>

<p class=MsoListParagraphCxSpLast style='text-indent:-18.0pt'><span lang=EN-GB
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span lang=EN-GB>press 'r' to restart the game</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN-GB style='font-size:16.0pt'>Minimax
Algorithm</span></b></p>

<p class=MsoNormal><span lang=EN-GB>&nbsp;</span></p>

<p class=MsoNormal><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif'>The
minimax algorithm is a decision-making algorithm used in two-player games, such
as tic-tac-toe, checkers, chess and go</span><span lang=CS style='font-size:
10.5pt;font-family:"Segoe UI",sans-serif'>. It is</span><span style='font-size:
10.5pt;font-family:"Segoe UI",sans-serif'> a recursive algorithm that evaluates
all possible moves and outcomes within the game</span><span lang=CS
style='font-size:10.5pt;font-family:"Segoe UI",sans-serif'> state tree, and selects
the next best possible move for the AI.</span></p>

<p class=MsoNormal>&nbsp;</p>

</div>

</body>

</html>
