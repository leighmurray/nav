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
<p><?php echo gettext('Endre Passord'); ?></p>
</td></tr>

<tr><td>
<?php
include("loginordie.php");
loginOrDie();

if (session_get('admin') >= 100) {
    echo "<p>" . gettext("Her kan du endre passord for en bruker.");
} else {
    echo "<p>" . gettext("Her kan du endre passord for din bruker.");
}

$brukernavn = session_get('bruker'); $uid = session_get('uid');

if (get_get('subaction') == 'endre') {

    if (post_exist('ebrukernavn') ) { 

        if (post_get('pass1') == post_get('pass2') ) {
            if (session_get('admin') >= 100) {
                $cb = post_get('ebrukernavn');
            } else {
                $cb = $brukernavn;
            }
            $dbh->endrePassord($cb, post_get('pass1'));

            print "<p><font size=\"+3\">" . gettext("OK</font>, passordet er endret for brukeren ") . $ebrukernavn . ".";
            unset($ebrukernavn);			

        } else {
            print "<p><font size=\"+3\">" . gettext("Feil</font>, du skrev ikke to like passord, derfor vil det <b>ikke</b> bli endret.");
        }
		

    } else {
        print "<p><font size=\"+3\">" . gettext("Feil</font> oppstod, passord er <b>ikke</b> endret.");
    }

  
}

print "<h3>" . gettext("Endre passord") . "</h3>";

?>

<form name="endrepassord" method="post" action="index.php?subaction=endre">

  <table width="100%" border="0" cellspacing="0" cellpadding="3">
    

    
    <tr>
    	<td width="30%"><p><?php echo gettext("Brukernavn"); ?></p></td>
    	<td width="70%">
<?php
if (session_get('admin') >= 100) {
    echo '<input name="ebrukernavn" type="text" size="15" value="' . $brukernavn . '">';
} else {
    echo '<input name="ebrukernavn" type="text" size="15" value="' . $brukernavn . '" disabled >';
}
?>
        </td>
   	</tr>

    <tr>
    	<td width="30%"><p><?php echo gettext("Passord"); ?></p></td>
    	<td width="70%"><input name="pass1" type="password" size="15" 
value=""></select>
        </td>
   	</tr>
   	
    <tr>
    	<td width="30%"><p><?php echo gettext("Passord igjen") ?></p></td>
    	<td width="70%"><input name="pass2" type="password" size="15" 
value=""></select>
        </td>
   	</tr>   	
    <tr>
      <td>&nbsp;</td>
      <td align="right"><input type="submit" name="Submit" value="<?php echo gettext("Endre Passord"); ?>"></td>
    </tr>
  </table>

</form>


</td></tr>
</table>
