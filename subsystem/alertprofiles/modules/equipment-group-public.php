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
<p><?php echo gettext('Public filter groups'); ?></p>
</td></tr>

<tr><td>
<?php
include("loginordie.php");
loginOrDie();

echo '<p>' . gettext('Here you can create and setup public filter groups. Be careful when you edit public filter groups because users can be using these groups in their profiles.');
echo '<p>' . gettext('Filter groups are used to setup alert subscriptions. Filter groups may be 
predefined by the NAV administrator or you may define your own.');
echo '<p>' . gettext('A filter group is put together using filters and filter group operators.');


if (get_get('allowdelete') == 1 ) {
	print '
<div style="
		padding: 2px 50px 5px 50px; 
		background: #772020; 
		color: #fcfcfc ! important;
		margin: 10px 5px 10px 5px;
		border: 1px solid #000"><h2>Warning</h2><p>You are about to delete a filter group that is in use by some alert profile. Deleting such a filter group will change the behaviour of those alert profiles. Be absolutely sure that you know what you do.</p></div>';
}



echo '<p><a href="?subaction=ny">';
echo gettext("Add a new filter group") . "</a>";


session_set('lastaction', 'futstyr');
$brukernavn = session_get('bruker'); $uid = session_get('uid');





if (in_array(get_get('subaction'), array('ny', 'endre') )) {

	$descr = ""; //gettext("Description :");
	print '<a name="nygruppe"></a><div class="newelement">';
	

	if ($subaction == 'endre') {
		print '<h2>' . gettext("Rename filter group") . '</h2>';
	} else {
		print '<h2>' . gettext("Add a new filter group") . '</h2>';
	}

	
	echo '<form name="form1" method="post" action="index.php?action=futstyr&subaction=';
	if ($subaction == 'endre') echo "endret"; else echo "nygruppe";
	echo '">';
	
	if ($subaction == 'endre') {
		print '<input type="hidden" name="gid" value="' . get_get('gid') . '">';
		$old_values = $dbh->utstyrgruppeInfo( get_get('gid') );
	}

	echo '<table width="100%" border="0" cellspacing="0" cellpadding="3">
	    <tr>
	    	<td width="30%"><p>' . gettext("Name") . '</p></td>
	    	<td width="70%"><input name="navn" type="text" size="40" 
	value="';
	if (isset($old_values)) { echo $old_values[0]; }
	echo '"></select>
	        </td>
	   </tr>';
	
    if ($subaction != 'endre') {
        echo '<tr><td width="30%"><p>' . gettext("Based upon") . '</p></td>';
    	echo '<td width="70%">';
        
        $ilist = '<SELECT name="basertpaa">' . "\n";
        $ilist .= '<OPTION value="0">' . gettext("Empty filter group");

        $utstyrgrlist = $dbh->listUtstyr($uid, 1);
        if (count($utstyrgrlist) > 0) {
            foreach ($utstyrgrlist as $utstyrelement) {
                if ( $utstyrelement[4] ) {
                    $owner = "Min";
                } else {
                    $owner = "Arvet";
                }
        
                $ilist .= '<OPTION value="' . $utstyrelement[0] . '">' . 
                    $utstyrelement[1] . "  [" . $owner  . "]\n" ;
            }
        }
        $ilist .= '</SELECT>' . "\n";
	
        echo $ilist;
        
        echo '</select></td></tr>';
    }
	
	echo '<tr><td colspan="2"><p>Description:<br><textarea name="descr" cols="60" rows="4">';
	
	if ($subaction == 'endre') {
	    echo $old_values[1];
	} else  {
	    echo $descr;
	}
	
	echo '</textarea>  </td>
	   </tr>	
	    <tr><td>&nbsp;</td><td align="right"><input type="submit" name="Submit" value="';
	    
	if ($subaction == 'endre') {
	    echo gettext("Save changes"); 
	} else  {
	    echo gettext("Add a new filter group");
	}
	echo '"></td>
	    </tr>
	  </table>
	</form></div>';
	
}









if (isset($subaction) && $subaction == 'endret') {

	if (post_get('gid') > 0) { 

		$dbh->endreUtstyrgruppe(post_get('gid'), post_get('navn'), post_get('descr') );
		$dbh->nyLogghendelse($uid, 5, gettext("Renamed public filter group") . " (" . post_get('navn') . ")");		
		unset($navn);
		unset($descr);
		print "<p><font size=\"+3\">" . gettext("OK</font>, filter group is renamed.");

	} else {
		print "<p><font size=\"+3\">" . gettext("An error</font> occured, the name is <b>not</b> changed.");
	}

}

if (isset($subaction) && $subaction == 'slett') {

	if (get_get('gid') > 0) { 	
		$dbh->slettUtstyrgruppe(get_get('gid') );
		$dbh->nyLogghendelse($uid, 4, gettext("Public filter group removed") . " (id=" . get_get('gid') . ")");		

		print "<p><font size=\"+3\">" . gettext("OK</font>, filter group is removed from the database.");

	} else {
		print "<p><font size=\"+3\">" . gettext("An error occured</font>, the filter group is <b>not</b> removed.");
	}

  
}



if (isset($subaction) && $subaction == "nygruppe") {
	print "<h3>" . gettext("Registering new filter group...") . "</h3>";
  
	if ($navn == "") $navn = gettext("No name");
	if ($uid > 0) { 

		$matchid = $dbh->nyUtstyrgruppeAdm(post_get('navn'), post_get('descr') );
		$dbh->nyLogghendelse($uid, 6, gettext("New public filter group") . " (" . post_get('navn') . ")");		
		print "<p><font size=\"+3\">" . gettext("OK</font>, a new filter group is created.");
    
	} else {
		print "<p><font size=\"+3\">" . gettext("An error</font> occured, a new filter group is <b>not</b> added to the database.");
	}

}




if (session_get('admin') >= 100) {


$l = new Lister( 113,
		array(gettext('Name'), gettext('#periods'), gettext('#filters'), gettext('Options..') ),
		array(50,  15, 15, 20),
		array('left',  'right', 'right', 'right'),
		array(true, true, true, false),
		0
);


//print "<h3>" . gettext("Public filter groups") . "</h3>";
print "<p>";

if ( get_exist('sortid') )
	$l->setSort(get_get('sort'), get_get('sortid') );
$utst = $dbh->listUtstyrAdm($l->getSort() );

for ($i = 0; $i < sizeof($utst); $i++) {


  if ($utst[$i][2] > 0 ) 
    { $ap = $utst[$i][2]; }
  else 
    {
      $ap = "<img alt=\"Ingen\" src=\"icons/stop.gif\">";
    }
    
  if ($utst[$i][3] > 0 ) 
    { $af = $utst[$i][3]; }
  else 
    {
      $af = "<img alt=\"Ingen\" src=\"icons/stop.gif\">";
    }    

	if ($utst[$i][4] == 't' ) { 
		$valg = '<a href="index.php?action=utstyrgrp&gid=' . $utst[$i][0]. 
			'">' . '<img alt="Open" src="icons/open2.gif" border=0></a>&nbsp;' .
			'<a href="index.php?action=futstyr&subaction=endre&gid=' . 
			$utst[$i][0] . '#nygruppe">' .
			'<img alt="Edit" src="icons/edit.gif" border=0></a>&nbsp;';
		
		if (get_get('allowdelete') == 1 or $utst[$i][2] < 1) {
			$valg .= '<a href="index.php?action=futstyr&subaction=slett&gid=' . 
				$utst[$i][0] . '"><img alt="Delete" src="icons/delete.gif" border=0></a>';
		} else {
			$valg .= '<img alt="Delete" title="This filter group is in use in at least one profile." src="icons/delete-grey.gif" border=0>';			
		}
			
	} else {
		$valg = "&nbsp;";
    }

	$l->addElement( array("<p>" . $utst[$i][1],  // navn
		$ap, $af, // verdi
		$valg ) 
	);

	$inh = new HTMLCell("<p class=\"descr\">" . $utst[$i][5] . "</p>");	  
	$l->addElement (&$inh);
}

print $l->getHTML();

print "<p>[ <a href=\"index.php?action=" . best_get('action') . "\">" . gettext("update") . " <img src=\"icons/refresh.gif\" class=\"refresh\" alt=\"oppdater\" border=0> ]</a> ";
print gettext("Number of filter groups: ") . sizeof($utst);

if (get_get('allowdelete') != 1 ) {
	print '<p align="right">[ <a href="index.php?action=' . best_get('action'). '&allowdelete=1">Allow removal of filter groups in use</a> ]';
}

}


?>
</td></tr>
</table>
