#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2018 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2018 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2018 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski
    PyUnTar based on iUnTar ver. 4.7 by Kazuki Przyborowski & Josep Sanz Campderros

    $FileInfo: gm2kenc.py - Last Update: 1/22/2018 Ver. 1.0.0 RC 1 - Author: cooldude2k $
'''

def str_replace(search, replace, subject, count=-1):
 outstring = subject;
 if(isinstance(search, str) and isinstance(replace, str)):
  outstring = outstring.replace(search, replace, count);
 if((isinstance(search, list) and isinstance(replace, list)) or (isinstance(search, tuple) and isinstance(replace, tuple))):
  for subsearch, subreplace in zip(search, replace):
   outstring = outstring.replace(subsearch, subreplace, count);
 return outstring;

def GM2k_Decrypt(matches):
 Change04 = ["%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change03 = ["#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change02 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change01 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change1 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", "#00"];
 Change4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change3 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change12 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change11 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change14 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change13 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change16 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change15 = ["#(04)", "#(14)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change18 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change17 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change20 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change19 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 Change6 = ["Th", "Wh", "En", "Go", "Ti", "Re", "In", "Un", "Fi", "Tr", "De", "We", "Ho", "No"];
 Change5 = ["#33", "#53", "#34", "#54", "#35", "#55", "#36", "#56", "#37", "#57", "#38", "#58", "#39", "#59"];
 Change8 = ["th", "wh", "en", "go", "ti", "re", "in", "un", "fi", "tr", "de", "we", "ho", "no"];
 Change7 = ["#73", "#93", "#74", "#94", "#75", "#95", "#76", "#96", "#77", "#97", "#78", "#98", "#79", "#99"];
 Change10 = ["Bo", "bo", "Ro", "ro", "Ki", "ki", "Co", "co", "Ja", "ja", "Ch", "ch", "Do", "do", "Du", "du", "Yo", "yo"];
 Change9 = ["#01", "#11", "#02", "#12", "#03", "#13", "#04", "#14", "#05", "#15", "#06", "#16", "#07", "#17", "#08", "#18", "#09", "#19"];
 Change22 = ["ba", "Ba", "da", "DA", "sa", "Sa", "pr", "Pr", "se", "Se"];
 Change21 = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"];
 Change24 = ["Ck", "ck", "Ne", "ne", "N�", "n�", "L�", "l�", "Lo", "lo", "Fo", "fo", "Su", "su", "Dis", "dis", "Us", "us", "Zy", "zy", "Si", "si", "Po", "po", "Mo", "mo", "GM", "gm", "CD", "cd"];
 Change23 = ["#{0}", "#{00}", "#{10}", "#{1}", "#{01}", "#{11}", "#{2}", "#{02}", "#{12}", "#{3}", "#{03}", "#{13}", "#{4}", "#{04}", "#{14}", "#{5}", "#{05}", "#{15}", "#{6}", "#{06}", "#{16}", "#{7}", "#{07}", "#{17}", "#{8}", "#{08}", "#{18}", "#{9}", "#{09}", "#{19}"];
 Change26 = ["Wo", "wo", "Jc", "jc", "Ge", "ge", "Ze", "ze", "Ph", "ph", "On", "on", "Te", "te", "If", "if", "IF", "IL", "Ps", "ps", "Il", "il", "Wi", "wi", "Li", "li", "La", "la", "Cr", "cr", "Ar", "ar", "Rs", "rs", "Pl", "pl", "Ab", "ab", "Ic", "ic"];
 Change25 = ["#{20}", "#{40}", "#{21}", "#{41}", "#{22}", "#{42}", "#{23}", "#{43}", "#{24}", "#{44}", "#{25}", "#{45}", "#{26}", "#{46}", "#{27}", "#{47}", "#{28}", "#{48}", "#{29}", "#{49}", "#{30}", "#{50}", "#{31}", "#{51}", "#{32}", "#{52}", "#{33}", "#{53}", "#{34}", "#{54}", "#{35}", "#{55}", "#{36}", "#{56}", "#{37}", "#{57}", "#{38}", "#{58}", "#{39}", "#{59}"];
 Change28 = ["Al", "al", "Ha", "ha", "Be", "be", "Ta", "ta", "Ga", "ga", "Gr", "gr", "Mu", "mu", "Nu", "nu", "Pi", "pi", "Zo", "zo", "Am", "am", "Sk", "sk", "Jo", "jo", "Rk", "rk", "Bu", "bu", "Ve", "ve", "Mp", "mp", "Ma", "ma", "Vi", "vi", "&#", "$"];
 Change27 = ["#{60}", "#{80}", "#{61}", "#{81}", "#{62}", "#{82}", "#{63}", "#{83}", "#{64}", "#{84}", "#{65}", "#{85}", "#{66}", "#{86}", "#{67}", "#{87}", "#{68}", "#{88}", "#{69}", "#{89}", "#{70}", "#{90}", "#{71}", "#{91}", "#{72}", "#{92}", "#{73}", "#{93}", "#{74}", "#{94}", "#{75}", "#{95}", "#{76}", "#{96}", "#{78}", "#{98}", "#{79}", "#{99}", "$", "�"];
 matches = str_replace(Change03, Change04, matches);
 matches = str_replace(Change01, Change02, matches);
 matches = str_replace(Change9, Change10, matches);
 matches = str_replace(Change5, Change6, matches);
 matches = str_replace(Change7, Change8, matches);
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 matches = str_replace(Change21, Change22, matches);
 matches = str_replace(Change23, Change24, matches);
 matches = str_replace(Change25, Change26, matches);
 matches = str_replace(Change27, Change28, matches);
 return matches;

def GM2k_Encrypt1(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 Change5 = ["Th", "Wh", "En", "Go", "Ti", "Re", "In", "Un", "Fi", "Tr", "De", "We", "Ho", "No"];
 Change6 = ["#33", "#53", "#34", "#54", "#35", "#55", "#36", "#56", "#37", "#57", "#38", "#58", "#39", "#59"];
 Change7 = ["th", "wh", "en", "go", "ti", "re", "in", "un", "fi", "tr", "de", "we", "ho", "no"];
 Change8 = ["#73", "#93", "#74", "#94", "#75", "#95", "#76", "#96", "#77", "#97", "#78", "#98", "#79", "#99"];
 Change9 = ["Bo", "bo", "Ro", "ro", "Ki", "ki", "Co", "co", "Ja", "ja", "Ch", "ch", "Do", "do", "Du", "du", "Yo", "yo"];
 Change10 = ["#01", "#11", "#02", "#12", "#03", "#13", "#04", "#14", "#05", "#15", "#06", "#16", "#07", "#17", "#08", "#18", "#09", "#19"];
 Change21 = ["ba", "Ba", "da", "DA", "sa", "Sa", "pr", "Pr", "se", "Se"];
 Change22 = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"];
 Change23 = ["Ck", "ck", "Ne", "ne", "N�", "n�", "L�", "l�", "Lo", "lo", "Fo", "fo", "Su", "su", "Dis", "dis", "Us", "us", "Zy", "zy", "Si", "si", "Po", "po", "Mo", "mo", "GM", "gm", "CD", "cd"];
 Change24 = ["#{0}", "#{00}", "#{10}", "#{1}", "#{01}", "#{11}", "#{2}", "#{02}", "#{12}", "#{3}", "#{03}", "#{13}", "#{4}", "#{04}", "#{14}", "#{5}", "#{05}", "#{15}", "#{6}", "#{06}", "#{16}", "#{7}", "#{07}", "#{17}", "#{8}", "#{08}", "#{18}", "#{9}", "#{09}", "#{19}"];
 Change25 = ["Wo", "wo", "Jc", "jc", "Ge", "ge", "Ze", "ze", "Ph", "ph", "On", "on", "Te", "te", "If", "if", "IF", "IL", "Ps", "ps", "Il", "il", "Wi", "wi", "Li", "li", "La", "la", "Cr", "cr", "Ar", "ar", "Rs", "rs", "Pl", "pl", "Ab", "ab", "Ic", "ic"];
 Change26 = ["#{20}", "#{40}", "#{21}", "#{41}", "#{22}", "#{42}", "#{23}", "#{43}", "#{24}", "#{44}", "#{25}", "#{45}", "#{26}", "#{46}", "#{27}", "#{47}", "#{28}", "#{48}", "#{29}", "#{49}", "#{30}", "#{50}", "#{31}", "#{51}", "#{32}", "#{52}", "#{33}", "#{53}", "#{34}", "#{54}", "#{35}", "#{55}", "#{36}", "#{56}", "#{37}", "#{57}", "#{38}", "#{58}", "#{39}", "#{59}"];
 Change27 = ["Al", "al", "Ha", "ha", "Be", "be", "Ta", "ta", "Ga", "ga", "Gr", "gr", "Mu", "mu", "Nu", "nu", "Pi", "pi", "Zo", "zo", "Am", "am", "Sk", "sk", "Jo", "jo", "Rk", "rk", "Bu", "bu", "Ve", "ve", "Mp", "mp", "Ma", "ma", "Vi", "vi"];
 Change28 = ["#{60}", "#{80}", "#{61}", "#{81}", "#{62}", "#{82}", "#{63}", "#{83}", "#{64}", "#{84}", "#{65}", "#{85}", "#{66}", "#{86}", "#{67}", "#{87}", "#{68}", "#{88}", "#{69}", "#{89}", "#{70}", "#{90}", "#{71}", "#{91}", "#{72}", "#{92}", "#{73}", "#{93}", "#{74}", "#{94}", "#{75}", "#{95}", "#{76}", "#{96}", "#{78}", "#{98}", "#{79}", "#{99}"];
 matches = str_replace(Change03, Change04, matches);
 matches = str_replace(Change01, Change02, matches);
 matches = str_replace(Change9, Change10, matches);
 matches = str_replace(Change21, Change22, matches);
 matches = str_replace(Change23, Change24, matches);
 matches = str_replace(Change25, Change26, matches);
 matches = str_replace(Change27, Change28, matches);
 matches = str_replace(Change5, Change6, matches);
 matches = str_replace(Change7, Change8, matches);
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 return matches;

def GM2k_Encrypt1Old(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 matches = str_replace(Change03, Change04, matches);
 matches = str_replace(Change01, Change02, matches);
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 return matches;

def GM2k_Encrypt2(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 Change5 = ["Th", "Wh", "En", "Go", "Ti", "Re", "In", "Un", "Fi", "Tr", "De", "We", "Ho", "No"];
 Change6 = ["#33", "#53", "#34", "#54", "#35", "#55", "#36", "#56", "#37", "#57", "#38", "#58", "#39", "#59"];
 Change7 = ["th", "wh", "en", "go", "ti", "re", "in", "un", "fi", "tr", "de", "we", "ho", "no"];
 Change8 = ["#73", "#93", "#74", "#94", "#75", "#95", "#76", "#96", "#77", "#97", "#78", "#98", "#79", "#99"];
 Change9 = ["Bo", "bo", "Ro", "ro", "Ki", "ki", "Co", "co", "Ja", "ja", "Ch", "ch", "Do", "do", "Du", "du", "Yo", "yo"];
 Change10 = ["#01", "#11", "#02", "#12", "#03", "#13", "#04", "#14", "#05", "#15", "#06", "#16", "#07", "#17", "#08", "#18", "#09", "#19"];
 Change21 = ["ba", "Ba", "da", "DA", "sa", "Sa", "pr", "Pr", "se", "Se"];
 Change22 = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"];
 Change23 = ["Ck", "ck", "Ne", "ne", "N�", "n�", "L�", "l�", "Lo", "lo", "Fo", "fo", "Su", "su", "Dis", "dis", "Us", "us", "Zy", "zy", "Si", "si", "Po", "po", "Mo", "mo", "GM", "gm", "CD", "cd"];
 Change24 = ["#{0}", "#{00}", "#{10}", "#{1}", "#{01}", "#{11}", "#{2}", "#{02}", "#{12}", "#{3}", "#{03}", "#{13}", "#{4}", "#{04}", "#{14}", "#{5}", "#{05}", "#{15}", "#{6}", "#{06}", "#{16}", "#{7}", "#{07}", "#{17}", "#{8}", "#{08}", "#{18}", "#{9}", "#{09}", "#{19}"];
 Change25 = ["Wo", "wo", "Jc", "jc", "Ge", "ge", "Ze", "ze", "Ph", "ph", "On", "on", "Te", "te", "If", "if", "IF", "IL", "Ps", "ps", "Il", "il", "Wi", "wi", "Li", "li", "La", "la", "Cr", "cr", "Ar", "ar", "Rs", "rs", "Pl", "pl", "Ab", "ab", "Ic", "ic"];
 Change26 = ["#{20}", "#{40}", "#{21}", "#{41}", "#{22}", "#{42}", "#{23}", "#{43}", "#{24}", "#{44}", "#{25}", "#{45}", "#{26}", "#{46}", "#{27}", "#{47}", "#{28}", "#{48}", "#{29}", "#{49}", "#{30}", "#{50}", "#{31}", "#{51}", "#{32}", "#{52}", "#{33}", "#{53}", "#{34}", "#{54}", "#{35}", "#{55}", "#{36}", "#{56}", "#{37}", "#{57}", "#{38}", "#{58}", "#{39}", "#{59}"];
 Change27 = ["Al", "al", "Ha", "ha", "Be", "be", "Ta", "ta", "Ga", "ga", "Gr", "gr", "Mu", "mu", "Nu", "nu", "Pi", "pi", "Zo", "zo", "Am", "am", "Sk", "sk", "Jo", "jo", "Rk", "rk", "Bu", "bu", "Ve", "ve", "Mp", "mp", "Ma", "ma", "Vi", "vi"];
 Change28 = ["#{60}", "#{80}", "#{61}", "#{81}", "#{62}", "#{82}", "#{63}", "#{83}", "#{64}", "#{84}", "#{65}", "#{85}", "#{66}", "#{86}", "#{67}", "#{87}", "#{68}", "#{88}", "#{69}", "#{89}", "#{70}", "#{90}", "#{71}", "#{91}", "#{72}", "#{92}", "#{73}", "#{93}", "#{74}", "#{94}", "#{75}", "#{95}", "#{76}", "#{96}", "#{78}", "#{98}", "#{79}", "#{99}"];
 matches = str_replace(Change03, Change04, matches);
 matches = str_replace(Change9, Change10, matches);
 matches = str_replace(Change21, Change22, matches);
 matches = str_replace(Change23, Change24, matches);
 matches = str_replace(Change25, Change26, matches);
 matches = str_replace(Change27, Change28, matches);
 matches = str_replace(Change5, Change6, matches);
 matches = str_replace(Change7, Change8, matches);
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 matches = str_replace(Change01, Change02, matches);
 return matches;

def GM2k_Encrypt2Old(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 matches = str_replace(Change03, Change04, matches);
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 matches = str_replace(Change01, Change02, matches);
 return matches;

def GM2k_Encrypt3(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 Change5 = ["Th", "Wh", "En", "Go", "Ti", "Re", "In", "Un", "Fi", "Tr", "De", "We", "Ho", "No"];
 Change6 = ["#33", "#53", "#34", "#54", "#35", "#55", "#36", "#56", "#37", "#57", "#38", "#58", "#39", "#59"];
 Change7 = ["th", "wh", "en", "go", "ti", "re", "in", "un", "fi", "tr", "de", "we", "ho", "no"];
 Change8 = ["#73", "#93", "#74", "#94", "#75", "#95", "#76", "#96", "#77", "#97", "#78", "#98", "#79", "#99"];
 Change9 = ["Bo", "bo", "Ro", "ro", "Ki", "ki", "Co", "co", "Ja", "ja", "Ch", "ch", "Do", "do", "Du", "du", "Yo", "yo"];
 Change10 = ["#01", "#11", "#02", "#12", "#03", "#13", "#04", "#14", "#05", "#15", "#06", "#16", "#07", "#17", "#08", "#18", "#09", "#19"];
 Change21 = ["ba", "Ba", "da", "DA", "sa", "Sa", "pr", "Pr", "se", "Se"];
 Change22 = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"];
 Change23 = ["Ck", "ck", "Ne", "ne", "N�", "n�", "L�", "l�", "Lo", "lo", "Fo", "fo", "Su", "su", "Dis", "dis", "Us", "us", "Zy", "zy", "Si", "si", "Po", "po", "Mo", "mo", "GM", "gm", "CD", "cd"];
 Change24 = ["#{0}", "#{00}", "#{10}", "#{1}", "#{01}", "#{11}", "#{2}", "#{02}", "#{12}", "#{3}", "#{03}", "#{13}", "#{4}", "#{04}", "#{14}", "#{5}", "#{05}", "#{15}", "#{6}", "#{06}", "#{16}", "#{7}", "#{07}", "#{17}", "#{8}", "#{08}", "#{18}", "#{9}", "#{09}", "#{19}"];
 Change25 = ["Wo", "wo", "Jc", "jc", "Ge", "ge", "Ze", "ze", "Ph", "ph", "On", "on", "Te", "te", "If", "if", "IF", "IL", "Ps", "ps", "Il", "il", "Wi", "wi", "Li", "li", "La", "la", "Cr", "cr", "Ar", "ar", "Rs", "rs", "Pl", "pl", "Ab", "ab", "Ic", "ic"];
 Change26 = ["#{20}", "#{40}", "#{21}", "#{41}", "#{22}", "#{42}", "#{23}", "#{43}", "#{24}", "#{44}", "#{25}", "#{45}", "#{26}", "#{46}", "#{27}", "#{47}", "#{28}", "#{48}", "#{29}", "#{49}", "#{30}", "#{50}", "#{31}", "#{51}", "#{32}", "#{52}", "#{33}", "#{53}", "#{34}", "#{54}", "#{35}", "#{55}", "#{36}", "#{56}", "#{37}", "#{57}", "#{38}", "#{58}", "#{39}", "#{59}"];
 Change27 = ["Al", "al", "Ha", "ha", "Be", "be", "Ta", "ta", "Ga", "ga", "Gr", "gr", "Mu", "mu", "Nu", "nu", "Pi", "pi", "Zo", "zo", "Am", "am", "Sk", "sk", "Jo", "jo", "Rk", "rk", "Bu", "bu", "Ve", "ve", "Mp", "mp", "Ma", "ma", "Vi", "vi"];
 Change28 = ["#{60}", "#{80}", "#{61}", "#{81}", "#{62}", "#{82}", "#{63}", "#{83}", "#{64}", "#{84}", "#{65}", "#{85}", "#{66}", "#{86}", "#{67}", "#{87}", "#{68}", "#{88}", "#{69}", "#{89}", "#{70}", "#{90}", "#{71}", "#{91}", "#{72}", "#{92}", "#{73}", "#{93}", "#{74}", "#{94}", "#{75}", "#{95}", "#{76}", "#{96}", "#{78}", "#{98}", "#{79}", "#{99}"];
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 matches = str_replace(Change9, Change10, matches);
 matches = str_replace(Change21, Change22, matches);
 matches = str_replace(Change23, Change24, matches);
 matches = str_replace(Change25, Change26, matches);
 matches = str_replace(Change27, Change28, matches);
 matches = str_replace(Change5, Change6, matches);
 matches = str_replace(Change7, Change8, matches);
 matches = str_replace(Change01, Change02, matches);
 matches = str_replace(Change03, Change04, matches);
 return matches;

def GM2k_Encrypt3Old(matches):
 Change03 = ["$", "&#", "%", "@", "&", "?", "!", "'", '"', "~", "`", "�", "�"];
 Change04 = ["�", "$", "#[,]", "#[.]", "#[;]", "#[:]", "#[-]", "#[^]", "#[/]", "#[|]", "#[+]", "#[�]", "#[�]"];
 Change01 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<" ,">"];
 Change02 = ["#(%)", "#{%}", "#(@)", "#{@}", "#(&)", "#{&}", "#(?)", "#{?}", "#(!)", "#{!}", "#{~}", "#{`}"];
 Change1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "	", " "];
 Change2 = ["#20", "#40", "#21", "#41", "#22", "#42", "#23", "#43", "#24", "#44", "#25", "#45", "#26", "#46", "#27", "#47", "#28", "#48", "#29", "#49", "#30", "#50", "#31", "#51", "#32", "#52", "#10", " "];
 Change3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
 Change4 = ["#60", "#80", "#61", "#81", "#62", "#82", "#63", "#83", "#64", "#84", "#65", "#85", "#66", "#86", "#67", "#87", "#68", "#88", "#69", "#89", "#70", "#90", "#71", "#91", "#72", "#92"];
 Change11 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change12 = ["#(20)", "#(40)", "#(21)", "#(41)", "#(22)", "#(42)", "#(23)", "#(43)", "#(24)", "#(44)", "#(25)", "#(45)", "#(26)", "#(46)", "#(27)", "#(47)", "#(28)", "#(48)", "#(29)", "#(49)", "#(30)", "#(50)", "#(31)", "#(51)", "#(32)", "#(53)", "#(33)", "#(54)", "#(34)"];
 Change13 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change14 = ["#(60)", "#(80)", "#(61)", "#(81)", "#(62)", "#(82)", "#(63)", "#(83)", "#(64)", "#(84)", "#(65)", "#(85)", "#(66)", "#(86)", "#(67)", "#(87)", "#(68)", "#(88)", "#(69)", "#(89)", "#(70)", "#(90)", "#(71)", "#(91)", "#(72)", "#(92)", "#(93)", "#(73)", "#(94)", "#(74)", "#(95)", "#(75)"];
 Change15 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�" ,"*"];
 Change16 = ["#(34)", "#(54)", "#(35)", "#(55)", "#(36)", "#(56)", "#(37)", "#(57)", "#(38)", "#(58)", "#(39)", "#(59)", "#(00)", "#(10)", "#(01)", "#(11)", "#(02)", "#(12)", "#(03)", "#(13)"];
 Change17 = ["�", "�", "�", "�", "�", "�", "�", "�"];
 Change18 = ["#(76)", "#(96)", "#(77)", "#(97)", "#(78)", "#(98)", "#(79)", "#(99)"];
 Change19 = ["�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�", "�"];
 Change20 = ["#(05)", "#(15)", "#(5)", "#(06)", "#(16)", "#(6)", "#(07)", "#(17)", "#(7)", "#(08)", "#(18)", "#(8)", "#(09)", "#(19)", "#(9)", "#(0)", "#(1)", "#(2)", "#(3)", "#(4)"];
 matches = str_replace(Change1, Change2, matches);
 matches = str_replace(Change3, Change4, matches);
 matches = str_replace(Change11, Change12, matches);
 matches = str_replace(Change13, Change14, matches);
 matches = str_replace(Change15, Change16, matches);
 matches = str_replace(Change17, Change18, matches);
 matches = str_replace(Change19, Change20, matches);
 matches = str_replace(Change01, Change02, matches);
 matches = str_replace(Change03, Change04, matches);
 return matches;

def GM2k_Encrypt(matches, encrypt=100):
 if(encrypt==100):
  return GM2k_Encrypt1(matches);
 if(encrypt==150):
  return GM2k_Encrypt1Old(matches);
 if(encrypt==200):
  return GM2k_Encrypt2(matches);
 if(encrypt==250):
  return GM2k_Encrypt2Old(matches);
 if(encrypt==300):
  return GM2k_Encrypt1(GM2k_Encrypt2(matches));
 if(encrypt==400):
  return GM2k_Encrypt3(matches);
 if(encrypt==500):
  return GM2k_Decrypt(matches);
 return matches;
