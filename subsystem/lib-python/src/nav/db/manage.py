# -*- coding: ISO8859-1 -*-
#
# $Id$
#
# Copyright 2003, 2004 Norwegian University of Science and Technology
#
# This file is part of Network Administration Visualized (NAV)
#
# NAV is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# NAV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NAV; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
# Authors: Stian S�iland <stain@itea.ntnu.no>
#
"""
This module extends the database abstraction generated by forgetSQL
for the manage database, defines some joint-tables and a
getNetbox() function.
"""


import re
import nav
import nav.db
import forgotten
from forgotten.manage import *


def _customizeTables():
    # Add/replace links between tables
    Swp_netbox._userClasses['to_module'] = Module
    Swp_netbox._userClasses['to_netbox'] = Netbox
    Swport._userClasses['to_netbox'] = Netbox
    Swport._userClasses['to_swport'] = Swport
    # rename from *_netboxid to *_netbox
    Swp_netbox._sqlFields['to_netbox'] = 'to_netboxid'
    Swport._sqlFields['to_netbox'] = 'to_netboxid'
    Swport._sqlFields['to_swport'] = 'to_swportid'
    del Swp_netbox._sqlFields['to_netboxid']
    del Swport._sqlFields['to_netboxid']
    del Swport._sqlFields['to_swportid']
    # this is not a reference to the Type-table =)
    del Emotd._userClasses['type']
    
    # some nice descriptive fields
    Netbox._shortView = ('sysname',)
    Room._shortView = ('roomid', 'location', 'descr')
    Location._shortView = ('descr',)
    Org._shortView = ('orgid', 'descr',)
    Cat._shortView = ('catid', 'descr',)
    Type._shortView = ('vendor', 'typename', 'descr') 
    Vlan._shortView = ('vlan','netident')

    # Link tables needs primary key
    Swportvlan._sqlPrimary = ('swport','vlan')
    Swportblocked._sqlPrimary = ('swport','vlan')
    Alerthistmsg._sqlPrimary = ('alerthist', 'language', 'msgtype')
    Alerthistvar._sqlPrimary = ('alerthist', 'var', 'val','state')
    Module._sqlPrimary = ('moduleid',)
    Swportallowedvlan._sqlPrimary = ('swport', 'hexstring')
    Emotd_related._sqlPrimary = ('emotd', 'key', 'value')
    Netboxinfo._sqlPrimary = ('key', 'var', 'val')
    Gwportprefix._sqlPrimary = ('gwip',)
    Serviceproperty._sqlPrimary = ('service', 'property')
    Netboxcategory._sqlPrimary = ('netbox', 'category')

    # connection with database
    def manageCursor(dummy):
        conn = nav.db.getConnection('default', 'manage')
        return conn.cursor()
    forgotten.manage._Wrapper.cursor = classmethod(manageCursor)
    forgotten.manage._Wrapper._dbModule = nav.db.driver


def getNetbox(address):
    """Retrieves a Netbox by IP address, sysname or netboxid.
       Returns None if nothing found."""
    if type(address) == int or _isNum.match(address):
        address = int(address)
        netbox = Netbox(address)
        try:
            netbox.load()
            return netbox
        except forgetSQL.NotFound:
            return None
    elif _isIP.match(address):
        query = "ip=%s" % nav.db.escape(address)
    else:    
        # eat our default domain until database is correct..
        #address = address.replace(".ntnu.no", "")
        hostname = nav.db.escape(address)
        query = "sysname=%s" % hostname

    results = Netbox.getAll(query)
    if not results:
        return None
    return results[0]

class RrdDataSourceFile(Rrd_datasource):
    """A join between Netbox, Rrd_file and Rrd_datasource"""
    _sqlFields = Rrd_datasource._sqlFields.copy()
    _sqlFields['netbox'] = 'rrd_file.netboxid'
    _userClasses = Rrd_datasource._userClasses.copy()
    _userClasses['netbox'] = Netbox
    _sqlLinks = (('rrd_fileid', 'rrd_file.rrd_fileid'),)


class Portconfig(Swport):
    """A join between Swport and Module"""
    _sqlFields =  {
                  # from swport
                  'duplex': 'duplex',
                  'ifindex': 'ifindex',
                  'link': 'link',
                  'media': 'media',
                  'port': 'port',
                  'portname': 'portname',
                  'speed': 'speed',
                  'swportid': 'swportid',
                  'to_netbox': 'to_netboxid',
                  'to_swport': 'to_swportid',
                  'trunk': 'trunk',
                  # from module
                  'module': 'module.module',
                  'device': 'module.deviceid',
                  'netbox': 'module.netboxid',
                  'submodule': 'module.submodule',
                  }
    _sqlLinks = ( ('moduleid', 'module.moduleid'),
                )
    # these userclasses are all from Module
    _userClasses =  {'device': 'Device', 'netbox': 'Netbox',
                     'to_netbox': 'Netbox',
                     'to_swport': 'Swport',
    }
    _orderBy = ('module', 'port')
    _shortView = ('module', 'port')

class RrdDataSourceFile(Rrd_datasource):
    _sqlFields = Rrd_datasource._sqlFields.copy()
    _sqlFields['netbox'] = 'rrd_file.netboxid'
    _userClasses = Rrd_datasource._userClasses.copy()
    _userClasses['netbox'] = Netbox
    _sqlLinks = (('rrd_fileid', 'rrd_file.rrd_fileid'),)



class NetboxSnmpoid(Snmpoid):
    """A join of Snmpoid and Typesnmpoid"""
    _sqlFields ={
		# from Smnpoid
		'descr': 'descr',
		'oidkey': 'oidkey',
		'snmpoid': 'snmpoid',
		'snmpoidid': 'snmpoidid',
		# from Typesnmpoid
		'frequency': 'typesnmpoid.frequency',
		'type': 'typesnmpoid.typeid'
		}
    _sqlLinks =	(
		('snmpoidid', 'typesnmpoid.snmpoidid'),
		)
    _userClasses = {'type': Type}
    _sqlPrimary = ('oidkey', 'type')

class AlerthistNetbox(forgotten.manage._Wrapper):
    """A join between Alerthist and Netbox"""
    _sqlFields =  {'alerthistid': 'alerthistid',
                  'device': 'deviceid',
                  'end_time': 'end_time',
                  'eventtype': 'eventtypeid',
                  'netbox': 'netboxid',
                  'severity': 'severity',
                  'source': 'source',
                  'start_time': 'start_time',
                  'subid': 'subid',
                  'value': 'value',
                      'cat': 'netbox.catid',
                      'subcat': 'netbox.subcat',
                      'org': 'netbox.orgid',
                      'netdevice': 'netbox.deviceid',
                      'ip': 'netbox.ip',
                      'prefix': 'netbox.prefixid',
                      'room': 'netbox.roomid',
                      'sysname': 'netbox.sysname',
                      'type': 'netbox.typeid',
                      'up': 'netbox.up',
                  }
    _sqlLinks =  ( ('netboxid', 'netbox.netboxid'),
                 )
    _userClasses =  {
    'device': 'Device', 'eventtype': 'Eventtype', 'netbox': 'Netbox',

    # things from netbox
        'cat': 'Cat',
        'netdevice': 'Device',
        'org': 'Org',
        'prefix': 'Prefix',
        'room': 'Room',
        'type': 'Type',
    }
    _sqlPrimary =  ('alerthistid',)
    _shortView =  ()
    _sqlTable =  'alerthist'
    _descriptions =  {}

def _buildOrgTree(tree, intermediate, key=None):
    """Recursively builds a tree structure for the parent/child
    relationships described in the flat intermediate dictionary."""
    if intermediate.has_key(key):
        for org in intermediate[key]:
            tree.update( {org: {}} )
            _buildOrgTree( tree[org], intermediate, key=org)

def _getOrgIntermediate():
    """Returns a dictionary, keys being the ids of organizations with
    children, values being a list of organization ids of the children.
    In effect, it is a flat structure describing the parent/child
    relationships of the organizational hierarchy.  The intermediate
    dictionary returned can be fed to _buildOrgTree() which will
    return a tree representation of the hierarchy."""
    
    orgObject = Org()
    intermediate = {}
    iterator = Org.getAllIterator(useObject = orgObject)
    for org in iterator:
        if org.parent not in intermediate.keys():
            intermediate[org.parent] = []
        intermediate[org.parent].append(org.orgid)
    return intermediate

def getOrgTree():
    """Returns a dictionary based tree structure of the organization
    hierarchy stored in the database."""
    orgTree = {}
    _buildOrgTree(orgTree, _getOrgIntermediate())
    return orgTree
    
_isIP = re.compile(r"^(\d{1,3}(\.\d{1,3}){3})$")
_isNum = re.compile(r"^\d+$")

forgetSQL.prepareClasses(locals())
_customizeTables()
