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
<p><?php echo gettext("Administration of filter variables"); ?></p>
</td></tr>

<tr><td>
<?php
include("loginordie.php");
loginOrDie();

echo "<p>" . gettext("Here you can setup and create new filter variables.
<p><b>Warning</b>: The new filter variables has to be supported by the Alert Engine.");



$dbhk = $dbinit->get_dbhk();

/*
echo "dbhk:<pre>";
print_r($dbhk);
echo "</pre>";
*/

if (get_get('subaction') == "slett") {
	
    $dbh->slettMatchField(get_get('mfid') );
    print "<p><font size=\"+3\">" . gettext("OK</font>, the filter variable is removed from the database.");

}

if (get_get('subaction') == "nymatch") {
  print "<h3>" . gettext("Registering a new filter variable...") . "</h3>";
  


  $fid = $dbh->nyttMatchFelt(
    post_get('name'), post_get('descr'), post_get('valuehelp'), post_get('valueid'),
    post_get('valuename'), post_get('valuecategory'), post_get('valuesort'), post_get('listlimit'),
    post_get('showlist'), post_get('datatype')
  );

    print "<p><font size=\"+3\">" . gettext("OK</font>, a new filter variable is added to the datbase and will be available for usage immediately (if supported by Alert Enige). The match field ID is ") . $fid;



}

$l = new Lister( 301,
	array(gettext('ID'), gettext('Name'), gettext('Database-reference'), gettext('Options...')),
	array(10, 30, 40, 20),
	array('left', 'left', 'left', 'right'),
	array(true, true, true, false),
	1
);


//print "<h3>" . gettext("Available Match Fields") . "</h3>";
print "<p>";

if ( get_exist('sortid') )
	$l->setSort(get_get('sort'), get_get('sortid') );


$fmlist = $dbh->listFilterMatchAdm($l->getSort() );

for ($i = 0; $i < sizeof($fmlist); $i++) {
  
  $valg = '<a href="index.php?action=filtermatchadm&subaction=slett&mfid=' . $fmlist[$i][0]. '">' .
    '<img alt="Delete" src="icons/delete.gif" border=0></a>';

  $l->addElement( array($fmlist[$i][0],  // id
			$fmlist[$i][1],  // navn
			$fmlist[$i][2], // referanse
			$valg
			) 
		  );
}

print $l->getHTML(1);

print "<p>[ <a href=\"index.php?action=" . $action. "\">" . gettext("update") . " <img src=\"icons/refresh.gif\" alt=\"oppdater\" class=\"refresh\" border=0> ]</a> ";
print gettext("Number of available filter variables: ") . sizeof($fmlist);
?>
<a name="nymatch"></a><div class="newelement"><h3>
<?php
echo gettext("Add a new filter variable"); 
?>
</h3>

<?php 

echo '<form name="nymatch" method="post" action="index.php?action=filtermatchadm&subaction=nymatch">';

echo '<table width="100%" border="0" cellspacing="0" cellpadding="3">';

echo '    <tr>';
echo '      <td width="30%">';
echo '<p>' . gettext("Name") . '</p></td>';

echo '      <td width="70%">';
echo '<input name="name" type="text" size="40"></td>';

echo '    </tr>';


echo '    <tr>';
echo '      <td width="30%">' . gettext("Show list") . '</td>';

echo '      <td width="70%">';
echo '<input name="showlist" value="true" type="radio" checked> ' . gettext("Show list") . '<br>';
echo '<input name="showlist" value="false" type="radio"> ' . gettext("Show input field");
echo '      </td>';
echo '    </tr>';

echo '    <tr>';
echo '      <td width="30%">' . gettext("Max list length") . '</td>';

echo '      <td width="70%">';
echo '<select name="listlimit">';
echo '<option value="100">100</option>';
echo '<option value="200">200</option>';
echo '<option value="300" selected>300</option>';
echo '<option value="500">500</option>';
echo '<option value="1000">1000</option>';
echo '<option value="10000">10000</option>';
echo '</select>';

echo '    </td></tr>';

echo '    <tr>';
echo '      <td width="30%">' . gettext("Data type") . '</td>';

$dtype = array(
    0 => gettext("String"),
    1 => gettext("Integer"),
    2 => gettext("IP-address")
);

echo '      <td width="70%">';
echo '<select name="datatype">';
foreach ($dtype AS $dval => $dt) {
    echo '<option value="' . $dval . '">' . $dt . '</option>' . "\n";
}
echo '</select>';

echo '    </td></tr>';





$f = $dbhk->listFelter();



echo '    <tr>';
echo '      <td width="30%">' . gettext("Database (id)") . '</td>';

echo '      <td width="70%">';
echo '<select name="valueid" id="select">';
echo '<option value="." selected>' . gettext("No reference") . '</option>';   
// Traverser kategorier
foreach ($f AS $cat => $catlist) {
    if ($cat != "") echo '<optgroup label="' . $cat . '">';
    foreach ($catlist AS $catelem) {
        echo ' <option value="' . $cat . '.' . $catelem[0] . '">' . $cat . '.'  . $catelem[0] . ' (' .$catelem[1]  . ') </option>' . "\n";
    }
    if ($cat != "") echo '</optgroup>';
}
echo '</select>';
echo '    </td></tr>';



echo '    <tr>';
echo '      <td width="30%">' . gettext("Database (Name)") . '</td>';

echo '      <td width="70%">';
echo '<select name="valuename" id="select">';   
echo '<option value="" selected>' . gettext("No references") . '</option>';  
// Traverser kategorier
foreach ($f AS $cat => $catlist) {
    if ($cat != "") echo '<optgroup label="' . $cat . '">';
    foreach ($catlist AS $catelem) {
        echo ' <option value="' . $cat . '.' . $catelem[0] . '">' . $cat . '.'  . $catelem[0] . ' (' .$catelem[1]  . ') </option>' . "\n";
    }
    if ($cat != "") echo '</optgroup>';
}
echo '</select>';
echo '    </td></tr>';




echo '    <tr>';
echo '      <td width="30%">' . gettext("Database (Category)") . '</td>';

echo '      <td width="70%">';
echo '<select name="valuecategory" id="select">';   

echo '<option value="" selected>' . gettext("No reference") . '</option>';   
// Traverser kategorier
foreach ($f AS $cat => $catlist) {
    if ($cat != "") echo '<optgroup label="' . $cat . '">';
    foreach ($catlist AS $catelem) {
        echo ' <option value="' . $cat . '.' . $catelem[0] . '">' . $cat . '.'  . $catelem[0] . ' (' .$catelem[1]  . ') </option>' . "\n";
    }
    if ($cat != "") echo '</optgroup>';
}
echo '</select>';
echo '    </td></tr>';




echo '    <tr>';
echo '      <td width="30%">' . gettext("Database (Sort by)") . '</td>';

echo '      <td width="70%">';
echo '<select name="valuesort" id="select">';    
echo '<option value="" selected>' . gettext("No reference") . '</option>';
// Traverser kategorier
foreach ($f AS $cat => $catlist) {
    if ($cat != "") echo '<optgroup label="' . $cat . '">';
    foreach ($catlist AS $catelem) {
        echo ' <option value="' . $cat . '.' . $catelem[0] . '">' . $cat . '.' . $catelem[0] . ' (' .$catelem[1]  . ') </option>' . "\n";
    }
    if ($cat != "") echo '</optgroup>';
}
echo '</select>';
echo '    </td></tr>';





echo '    <tr>';
echo '      <td width="30%">';
echo '<p>' . gettext("Description") . '</p></td>';

echo '      <td width="70%">';
echo '<textarea name="descr" cols="40" rows="6"></textarea></td>';

echo '    </tr>';

echo '    <tr>';
echo '      <td width="30%">';
echo '<p>' . gettext("Value help") . '</p></td>';

echo '      <td width="70%">';
echo '<textarea name="valuehelp" cols="40" rows="6"></textarea></td>';

echo '    </tr>';




echo '    <tr>';
echo '      <td colspan="2" align="right"><input type="submit" name="Submit" value="';
echo gettext('Add new filter variable') . '"></td>';
echo '    </tr>';


echo '</table></form></div>';
?>

</td></tr>
</table>
