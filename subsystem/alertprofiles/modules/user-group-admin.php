<?php
/* $Id$
 *
 * Copyright 2002-2004 UNINETT AS
 * 
 * This file is part of Network Administration Visualized (NAV)
 *
 * NAV is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * NAV is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NAV; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 *
 * Authors: Andreas Aakre Solberg <andreas.solberg@uninett.no>
 *
 */
?><table width="100%" class="mainWindow">
<tr><td class="mainWindowHead">
<p><?php echo gettext("User groups"); ?></p>
</td></tr>

<tr><td>
<?php
include("loginordie.php");
loginOrDie();


echo "<p>";
echo gettext("Here you can create and setup user groups."); 

echo '<p><a href="#nygruppe">';
echo gettext("Add a new user group");
echo '</a><p>';



if (get_exist('subaction'))
	session_set('gruppesubaction', get_get('subaction'));
if (get_exist('gid'))
	session_set('endregruppeid', get_get('gid') );
if (get_exist('hl'))
	session_set('endregruppehighlight', get_get('hl') );


if (session_get('gruppesubaction') == 'endre') {
	$stekst = gettext("Change user group"); 
	$saction = "endregruppe";
} else {
	$stekst = gettext("Add user group");
	$saction = "nygruppe";
}

if (session_get('gruppesubaction') == "nygruppe") {

	print "<h3>" . gettext("Registering new user group...") . "</h3>";

	$gid = $dbh->nyBrukerGruppe(post_get('navn'), post_get('descr') );

	if ($gid > 0) { 
		$navn = ""; 	$descr = gettext("Description : ");
		
		print "<p><font size=\"+3\">" . gettext("OK</font>, a new user group is created. Please add users, equipment groups and permissions to it.");

	} else {
    	print "<p><font size=\"+3\">" . gettext("An error</font> occured, a new user is <b>not</b> created.");
	}
	session_set('gruppesubaction', 'clean');
}

if (session_get('gruppesubaction') == "slett") {

	if (session_get('endregruppeid') > 0) { 
	
		$dbh->slettBrukergruppe( session_get('endregruppeid') );
		print "<p><font size=\"+3\">" . gettext("OK</font>, the user group is removed.");

	} else {
		print "<p><font size=\"+3\">" . gettext("An error</font> occured, the user group is <b>not</b> removed.");
	}

	session_set('gruppesubaction', 'clean');
}


if (session_get('gruppesubaction') == "endregruppe") {
	print "<h3>" . gettext("Setup user group...") . "</h3>";

	$dbh->endreBrukergruppe(session_get('endregruppeid'), post_get('navn'), post_get('descr') );
	
	reset ($HTTP_POST_VARS);
	
	while ( list($n, $val) = each ($HTTP_POST_VARS)) {
		if ( preg_match("/bvalg([0-9]+)/i", $n, $m) ) {
			$var = "bvelg" . $m[1];
			$dbh->endreBrukerTilGruppe($m[1], session_get('endregruppeid'), isset(${$var}) );	
		}	
	
		if ( preg_match("/rvalg([0-9]+)/i", $n, $m) ) {
			$var = "rvelg" . $m[1];				
			$dbh->endreRettighet(session_get('endregruppeid'), $m[1], isset(${$var}));
		}
		if ( preg_match("/dvalg([0-9]+)/i", $n, $m) ) {
			$var = "dvelg" . $m[1];		
			$dbh->endreDefault(session_get('endregruppeid'), $m[1], isset(${$var}) );	
		}
	}

	$navn = ""; $descr = gettext("Description : ");
	print "<p><font size=\"+3\">" . gettext("OK</font>, changes applied for user group.");
	
	session_set('gruppesubaction', 'clean');

  
}

$l = new Lister( 103,
	array(gettext('User group'), gettext('#users'), gettext('#permissions'), 
		gettext('#std. groups'), gettext('Options..') ),
	array(25, 20, 20, 20, 15),
	array('left', 'right', 'right', 'right', 'right' ),
	array(true, true, true, true, false),
	0
);

print "<h3>" . gettext("User groups") . "</h3>";

if ( get_exist('sortid') )
	$l->setSort(get_get('sort'), get_get('sortid') );
	
$grupper = $dbh->listBrukerGrupper($l->getSort() );

if (session_get('gruppesubaction') == 'endre')
	$l->highlight(session_get('endregruppehighlight'));

for ($i = 0; $i < sizeof($grupper); $i++) {
  
	$valg = '<a href="index.php?subaction=endre&gid=' . $grupper[$i][0] . '&hl=' . $i . '">' .
		'<img alt="Edit" src="icons/edit.gif" border=0></a>&nbsp;' .
    	'<a href="index.php?subaction=slett&gid=' . $grupper[$i][0] . '">' .
    	'<img alt="Delete" src="icons/delete.gif" border=0>' .
    	'</a>';

	if ($grupper[$i][3] > 0 ) { 
		$ab = $grupper[$i][3]; 
	} else { 
		$ab = "<img alt=\"Ingen\" src=\"icons/stop.gif\">"; 
	}

	if ($grupper[$i][4] > 0 ) { 
		$ar = $grupper[$i][4]; 
	} else { 
		$ar = "<img alt=\"Ingen\" src=\"icons/stop.gif\">"; 
	}

	if ($grupper[$i][5] > 0 ) { 
		$ag = $grupper[$i][5]; 
	} else { 
		$ag = "<img alt=\"Ingen\" src=\"icons/stop.gif\">"; 
	}
	
	$l->addElement( array($grupper[$i][1],  // gruppenavn
		$ab,  // #bruekre
		$ar, // #rettigheter
		$ag,  // #std grupper
		$valg
		) 
	);
	
	$inh = new HTMLCell("<p class=\"descr\">" . $grupper[$i][2] . "</p>");	  
	$l->addElement (&$inh);	
	
	
}

print $l->getHTML();

print "<p>[ <a href=\"index.php\">" . gettext("update") . " <img class=\"refresh\" src=\"icons/refresh.gif\" alt=\"oppdater\" border=0> ]</a> ";
print gettext("Number of groups: ") . sizeof($grupper);


if (session_get('gruppesubaction') == 'endre') {
	$gr = $dbh->brukergruppeInfo(session_get('endregruppeid') );
	$navn = $gr[0];
	$descr = $gr[1];
} else {
	$descr = gettext("Description : ");
}

?>

<a name="nygruppe"></a><p><h3><?php print $stekst; ?></h3>
<form name="form1" method="post" action="index.php?subaction=<?php echo $saction; ?>">
  <table width="100%" border="0" cellspacing="0" cellpadding="3">
    <tr>
      <td width="30%"><p><?php echo gettext("Name of group"); ?></p></td>
      <td width="70%"><input name="navn" type="text" size="40" 
value="<?php echo $navn; ?>"></td>
    </tr>

    <tr>
    	<td colspan="2"><textarea name="descr" cols="60" rows="4">
<?php echo $descr; ?></textarea>  </td>
   	</tr>    
   	
    <tr>
      <td>&nbsp;</td>
      <td align="right">
<?php
print '<input type="submit" name="Submit" value="' . $stekst  . '">';
?>
</td>
    </tr>
  </table>

<?php
if (session_get('gruppesubaction') == 'endre' OR session_get('gruppesubaction') == 'nygruppe') {

	$l = new Lister( 104,
		array(gettext('Options'), gettext('User name'), gettext('Name') ),
		array(15, 30, 55),
		array('left', 'left', 'left'),
		array(false, true, true),
		2
	);
	
	if ( get_exist('sortid') )
		$l->setSort(get_get('sort'), get_get('sortid') );	
	
	// Henter ut alle brukerene og om de tilhører gruppen eller ikke
	$brukere = $dbh->listGrBrukere(session_get('endregruppeid'), $l->getSort() );
	for ($i = 0; $i < sizeof($brukere); $i++) {
	
		if ($brukere[$i][3] == 't') $medl = " checked"; else $medl = "";
		$velg = '<input name="bvelg' . $brukere[$i][0] . '" type="checkbox" value="1"' . $medl . '>';
		$velg .= '<input name="bvalg' . $brukere[$i][0] . '" value="1" type="hidden">';

		$l->addElement( array(
			$velg,
			$brukere[$i][1],
			$brukere[$i][2],
		) );
		
	}
	print "<h3>" . gettext("Users subscribed to the group") . "</h3>";
	print $l->getHTML();

	$l = new Lister( 105,
		array(gettext('Permissions'), gettext('Standard groups'), gettext('Group name') ),
		array(15, 15, 70),
		array('left', 'left', 'left'),
		array(false, false, true),
		2
	);

	if ( get_exist('sortid') )
		$l->setSort(get_get('sort'), get_get('sortid') );	

	$utstyr = $dbh->listGrUtstyr(session_get('uid'), session_get('endregruppeid'), $sort);
	for ($i = 0; $i < sizeof($utstyr); $i++) {
	
		if ($utstyr[$i][3] == 't') $r = " checked"; else $r = "";
		$rvelg = '<input name="rvelg' . $utstyr[$i][0] . '" type="checkbox" value="1"' . $r . '>';
		$rvelg .= '<input name="rvalg' . $utstyr[$i][0] . '" value="1" type="hidden">';

		if ($utstyr[$i][4] == 't') $d = " checked"; else $d = "";
		$dvelg = '<input name="dvelg' . $utstyr[$i][0] . '" type="checkbox" value="1"' . $d . '>';
		$dvelg .= '<input name="dvalg' . $utstyr[$i][0] . '" value="1" type="hidden">';

		$l->addElement( array(
			$rvelg,
			$dvelg,			
			$utstyr[$i][1]
		) );
	}
	
	print "<h3>" . gettext("Equipment groups") . "</h3>";
	print $l->getHTML();
	print '<p><input type="submit" name="Submit" value="' . $stekst  . '">';

}

?>

</form>

</td></tr>
</table>
