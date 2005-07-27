# -*- coding: ISO8859-1 -*-
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
# Authors: Hans J�rgen Hoel <hansjorg@orakel.ntnu.no>
#


from nav.db.manage import *

class editdbLocation(Location):
    def getOptions(cls):
        options = []
        for entry in cls.getAllIterator(orderBy='locationid'):
            options.append((entry.locationid,entry.locationid + \
                            ' (' + entry.descr + ')'))    
        return options       
    getOptions = classmethod(getOptions)

class editdbOrg(Org):
    def getOptions(cls):
        options = []
        for entry in cls.getAllIterator(orderBy='orgid'):
            options.append((entry.orgid,entry.orgid + ' (' + \
                            str(entry.descr) + ')'))    
        return options       
    getOptions = classmethod(getOptions)

class editdbVendor(Vendor):
    def getOptions(cls):
        options = []
        for entry in cls.getAllIterator(orderBy='vendorid'):
            options.append((entry.vendorid,entry.vendorid))    
        return options       
    getOptions = classmethod(getOptions)

#class editdbTypegroup(Typegroup):
#    def getOptions(cls):
#        options = []
#        for entry in cls.getAllIterator(orderBy='typegroupid'):
#            text = entry.typegroupid + ': ' + entry.descr
#            options.append((entry.typegroupid,text))    
#        return options       
#    getOptions = classmethod(getOptions)


class editdbNetbox(Netbox):
    # added catid
    _sqlFields =  {'catid': 'catid',
                   'cat': 'catid',
                   'device': 'deviceid',
                   'ip': 'ip',
                   'netboxid': 'netboxid',
                   'org': 'orgid',
                   'orgid': 'orgid',
                   'prefix': 'prefixid',
                   'ro': 'ro',
                   'room': 'roomid',
                   'roomid': 'roomid',
                   'rw': 'rw',
                   'snmp_agent': 'snmp_agent',
                   'snmp_version': 'snmp_version',
                   'subcat': 'subcat',
                   'sysname': 'sysname',
                   'type': 'typeid',
                   'up': 'up',
                   'serial': 'device.serial'}
    _sqlLinks =  (('deviceid', 'device.deviceid'),)
    _userClasses =  {'cat': Cat,
                    'device': Device,
                    'org': Org,
                    'prefix': Prefix,
                    'room': Room,
                    'subcat': Subcat,
                    'type': Type}
    _sqlPrimary =  ('netboxid',)
    _shortView =  ()
                                                        

class editdbProduct(Product):
    # adds vendorid
    _sqlFields =  {'descr': 'descr',
                  'productid': 'productid',
                  'productno': 'productno',
                  'vendor': 'vendorid',
                  'vendorid': 'vendorid'}
                                                          
class editdbType(Type):
    # adds typegroupid and vendorid
    _sqlFields =  {'cdp': 'cdp',
                   'descr': 'descr',
                   'frequency': 'frequency',
                   'sysobjectid': 'sysobjectid',
                   'tftp': 'tftp',
                   'typeid': 'typeid',
                   'typename': 'typename',
                   'vendor': 'vendorid',
                   'vendorid': 'vendorid'}

class editdbRoom(Room):
    _sqlFields =  {'descr': 'descr',
                  'locationid': 'locationid',
                  'location': 'locationid',
                  'opt1': 'opt1',
                  'opt2': 'opt2',
                  'opt3': 'opt3',
                  'opt4': 'opt4',
                  'roomid': 'roomid'}
    _sqlLinks =  {}
    _userClasses = {}
    #_userClasses =  {'location': 'Location'}
    _sqlPrimary =  ('roomid',)
    _shortView =  ()
    _sqlTable =  'room'
    _descriptions =  {}

class editdbPrefixVlan(Prefix):
    _sqlFields =  {'prefixid': 'prefixid',
                   'vlan': 'vlanid', 
                   'netaddr': 'netaddr',
                   'nettype': 'vlan.nettype',
                   'vlannumber': 'vlan.vlan',
                   'orgid': 'vlan.orgid',
                   'netident': 'vlan.netident',
                   'description': 'vlan.description',
                   'usageid': 'vlan.usageid'}
    _sqlLinks = (('vlanid','vlan.vlanid'),)
    _userClasses = {'vlan': Vlan}
    _shortView = ()
    _sqlTable = 'prefix'
    _descriptions = {}

class editdbVlan(Vlan):
    _sqlFields =  {'description': 'description',
                   'netident': 'netident',
                   'nettype': 'nettype',
                   'org': 'orgid',
                   'usage': 'usageid',
                   'orgid': 'orgid',
                   'usageid': 'usageid',
                   'vlan': 'vlan',
                   'vlanid': 'vlanid'}
    _sqlLinks =  {}
    _userClasses =  {'usage': Usage, 'org': Org}
    _sqlPrimary =  ('vlanid',)
    _shortView =  ()
    _sqlTable =  'vlan'
    _descriptions =  {}

class editdbSubcat(Subcat):
    _sqlFields =  {'subcatid': 'subcatid', 'descr': 'descr', 'catid': 'catid'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('subcatid',)
    _shortView =  ()
    _sqlTable =  'subcat'
    _descriptions =  {}
                            
class editdbService(Service):
    _sqlFields =  {'active': 'active',
                   'handler': 'handler',
                   'netboxid': 'netboxid',
                   'netbox': 'netboxid',
                   'serviceid': 'serviceid',
                   'up': 'up',
                   'version': 'version'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': Netbox}
    _sqlPrimary =  ('serviceid',)
    _shortView =  ()
    _sqlTable =  'service'
    _descriptions =  {}

## class editdbNetboxsnmpoid(Netboxsnmpoid):
##     _sqlFields =  {'frequency': 'frequency',
##                    'netbox': 'netboxid',
##                    'snmpoid': 'snmpoidid'}
##     _sqlLinks =  {}
##     _sqlPrimary = ('typeid',)
##     _userClasses =  {'netbox': 'Netbox', 'snmpoid': 'Snmpoid'}
##     _shortView =  ()
##     _sqlTable =  'netboxsnmpoid'
##     _descriptions =  {}
                                                 
