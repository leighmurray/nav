# -*- coding: ISO8859-1 -*-
"""Database wrappers.
Autogenerated by forgetSQL 2004-10-29.
"""

import forgetSQL

class _Wrapper(forgetSQL.Forgetter):
    """Just a simple wrapper class so that you may
    easily change stuff for all forgetters. Typically
    this involves subcliassing MysqlForgetter instead."""

    # Remember to change the class function cursor() so that
    # it returns a cursor connected to the database.
    # 
    ## cursor = lambda: myDatabase.cursor()
    pass



class Alertengine(_Wrapper):
    _sqlFields =  {'lastalertqid': 'lastalertqid'}
    _sqlLinks =  {}
    _userClasses =  {}
    _shortView =  ()
    _sqlTable =  'alertengine'
    _descriptions =  {}

class Alerthist(_Wrapper):
    _sqlFields =  {'alerthistid': 'alerthistid',
                  'alerttype': 'alerttypeid',
                  'device': 'deviceid',
                  'end_time': 'end_time',
                  'eventtype': 'eventtypeid',
                  'netbox': 'netboxid',
                  'severity': 'severity',
                  'source': 'source',
                  'start_time': 'start_time',
                  'subid': 'subid',
                  'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'alerttype': 'Alerttype',
                    'device': 'Device',
                    'eventtype': 'Eventtype',
                    'netbox': 'Netbox'}
    _sqlPrimary =  ('alerthistid',)
    _shortView =  ()
    _sqlTable =  'alerthist'
    _descriptions =  {}

class Alerthistmsg(_Wrapper):
    _sqlFields =  {'alerthist': 'alerthistid',
                  'language': 'language',
                  'msg': 'msg',
                  'msgtype': 'msgtype',
                  'state': 'state'}
    _sqlLinks =  {}
    _userClasses =  {'alerthist': 'Alerthist'}
    _shortView =  ()
    _sqlTable =  'alerthistmsg'
    _descriptions =  {}

class Alerthistvar(_Wrapper):
    _sqlFields =  {'var': 'var', 'alerthist': 'alerthistid', 'state': 'state', 'val': 'val'}
    _sqlLinks =  {}
    _userClasses =  {'alerthist': 'Alerthist'}
    _shortView =  ()
    _sqlTable =  'alerthistvar'
    _descriptions =  {}

class Alertq(_Wrapper):
    _sqlFields =  {'alertqid': 'alertqid',
                  'alerttype': 'alerttypeid',
                  'device': 'deviceid',
                  'eventtype': 'eventtypeid',
                  'netbox': 'netboxid',
                  'severity': 'severity',
                  'source': 'source',
                  'state': 'state',
                  'subid': 'subid',
                  'time': 'time',
                  'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'alerttype': 'Alerttype',
                    'device': 'Device',
                    'eventtype': 'Eventtype',
                    'netbox': 'Netbox'}
    _sqlPrimary =  ('alertqid',)
    _shortView =  ()
    _sqlTable =  'alertq'
    _descriptions =  {}

class Alertqmsg(_Wrapper):
    _sqlFields =  {'alertq': 'alertqid',
                  'language': 'language',
                  'msg': 'msg',
                  'msgtype': 'msgtype'}
    _sqlLinks =  {}
    _userClasses =  {'alertq': 'Alertq'}
    _shortView =  ()
    _sqlTable =  'alertqmsg'
    _descriptions =  {}

class Alertqvar(_Wrapper):
    _sqlFields =  {'var': 'var', 'val': 'val', 'alertq': 'alertqid'}
    _sqlLinks =  {}
    _userClasses =  {'alertq': 'Alertq'}
    _shortView =  ()
    _sqlTable =  'alertqvar'
    _descriptions =  {}

class Alerttype(_Wrapper):
    _sqlFields =  {'alerttype': 'alerttype',
                  'alerttypedesc': 'alerttypedesc',
                  'alerttypeid': 'alerttypeid',
                  'eventtype': 'eventtypeid'}
    _sqlLinks =  {}
    _userClasses =  {'eventtype': 'Eventtype'}
    _sqlPrimary =  ('alerttype',)
    _shortView =  ()
    _sqlTable =  'alerttype'
    _descriptions =  {}

class Arp(_Wrapper):
    _sqlFields =  {'arpid': 'arpid',
                  'end_time': 'end_time',
                  'ip': 'ip',
                  'mac': 'mac',
                  'netbox': 'netboxid',
                  'prefix': 'prefixid',
                  'start_time': 'start_time',
                  'sysname': 'sysname'}
    _sqlLinks =  {}
    _userClasses =  {'prefix': 'Prefix', 'netbox': 'Netbox'}
    _sqlPrimary =  ('arpid',)
    _shortView =  ()
    _sqlTable =  'arp'
    _descriptions =  {}

class Cabling(_Wrapper):
    _sqlFields =  {'building': 'building',
                  'cablingid': 'cablingid',
                  'category': 'category',
                  'descr': 'descr',
                  'jack': 'jack',
                  'room': 'roomid',
                  'targetroom': 'targetroom'}
    _sqlLinks =  {}
    _userClasses =  {'room': 'Room'}
    _sqlPrimary =  ('cablingid',)
    _shortView =  ()
    _sqlTable =  'cabling'
    _descriptions =  {}

class Cam(_Wrapper):
    _sqlFields =  {'camid': 'camid',
                  'end_time': 'end_time',
                  'ifindex': 'ifindex',
                  'mac': 'mac',
                  'misscnt': 'misscnt',
                  'module': 'module',
                  'netbox': 'netboxid',
                  'port': 'port',
                  'start_time': 'start_time',
                  'sysname': 'sysname'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox', 'module': 'Module'}
    _sqlPrimary =  ('camid',)
    _shortView =  ()
    _sqlTable =  'cam'
    _descriptions =  {}

class Cat(_Wrapper):
    _sqlFields =  {'req_snmp': 'req_snmp', 'descr': 'descr', 'catid': 'catid'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('catid',)
    _shortView =  ()
    _sqlTable =  'cat'
    _descriptions =  {}

class Device(_Wrapper):
    _sqlFields =  {'active': 'active',
                  'auto': 'auto',
                  'deviceid': 'deviceid',
                  'deviceorder': 'deviceorderid',
                  'fw_ver': 'fw_ver',
                  'hw_ver': 'hw_ver',
                  'product': 'productid',
                  'serial': 'serial',
                  'sw_ver': 'sw_ver'}
    _sqlLinks =  {}
    _userClasses =  {'product': 'Product', 'deviceorder': 'Deviceorder'}
    _sqlPrimary =  ('deviceid',)
    _shortView =  ()
    _sqlTable =  'device'
    _descriptions =  {}

class Deviceorder(_Wrapper):
    _sqlFields =  {'arrived': 'arrived',
                  'comment': 'comment',
                  'deviceorderid': 'deviceorderid',
                  'lastupdated': 'lastupdated',
                  'ordered': 'ordered',
                  'ordernumber': 'ordernumber',
                  'org': 'orgid',
                  'product': 'productid',
                  'registered': 'registered',
                  'retailer': 'retailer',
                  'updatedby': 'updatedby',
                  'username': 'username'}
    _sqlLinks =  {}
    _userClasses =  {'org': 'Org', 'product': 'Product'}
    _sqlPrimary =  ('deviceorderid',)
    _shortView =  ()
    _sqlTable =  'deviceorder'
    _descriptions =  {}

class Emotd(_Wrapper):
    _sqlFields =  {'affected': 'affected',
                  'affected_en': 'affected_en',
                  'author': 'author',
                  'description': 'description',
                  'description_en': 'description_en',
                  'detail': 'detail',
                  'detail_en': 'detail_en',
                  'downtime': 'downtime',
                  'downtime_en': 'downtime_en',
                  'emotdid': 'emotdid',
                  'last_changed': 'last_changed',
                  'publish_end': 'publish_end',
                  'publish_start': 'publish_start',
                  'published': 'published',
                  'replaces_emotd': 'replaces_emotd',
                  'title': 'title',
                  'title_en': 'title_en',
                  'type': 'type'}
    _sqlLinks =  {}
    _userClasses =  {'type': 'Type'}
    _sqlPrimary =  ('emotdid',)
    _shortView =  ()
    _sqlTable =  'emotd'
    _descriptions =  {}

class Emotd_related(_Wrapper):
    _sqlFields =  {'value': 'value', 'emotd': 'emotdid', 'key': 'key'}
    _sqlLinks =  {}
    _userClasses =  {'emotd': 'Emotd'}
    _shortView =  ()
    _sqlTable =  'emotd_related'
    _descriptions =  {}

class Eventq(_Wrapper):
    _sqlFields =  {'device': 'deviceid',
                  'eventqid': 'eventqid',
                  'eventtype': 'eventtypeid',
                  'netbox': 'netboxid',
                  'severity': 'severity',
                  'source': 'source',
                  'state': 'state',
                  'subid': 'subid',
                  'target': 'target',
                  'time': 'time',
                  'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'device': 'Device', 'eventtype': 'Eventtype', 'netbox': 'Netbox'}
    _sqlPrimary =  ('eventqid',)
    _shortView =  ()
    _sqlTable =  'eventq'
    _descriptions =  {}

class Eventqvar(_Wrapper):
    _sqlFields =  {'var': 'var', 'val': 'val', 'eventq': 'eventqid'}
    _sqlLinks =  {}
    _userClasses =  {'eventq': 'Eventq'}
    _shortView =  ()
    _sqlTable =  'eventqvar'
    _descriptions =  {}

class Eventtype(_Wrapper):
    _sqlFields =  {'eventtypedesc': 'eventtypedesc',
                  'eventtypeid': 'eventtypeid',
                  'stateful': 'stateful'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('eventtypeid',)
    _shortView =  ()
    _sqlTable =  'eventtype'
    _descriptions =  {}

class Gwport(_Wrapper):
    _sqlFields =  {'gwportid': 'gwportid',
                  'ifindex': 'ifindex',
                  'interface': 'interface',
                  'link': 'link',
                  'masterindex': 'masterindex',
                  'metric': 'metric',
                  'module': 'moduleid',
                  'speed': 'speed',
                  'to_netboxid': 'to_netboxid',
                  'to_swportid': 'to_swportid'}
    _sqlLinks =  {}
    _userClasses =  {'module': 'Module'}
    _sqlPrimary =  ('gwportid',)
    _shortView =  ()
    _sqlTable =  'gwport'
    _descriptions =  {}

class Gwportprefix(_Wrapper):
    _sqlFields =  {'prefix': 'prefixid', 'gwip': 'gwip', 'hsrp': 'hsrp', 'gwport': 'gwportid'}
    _sqlLinks =  {}
    _userClasses =  {'prefix': 'Prefix', 'gwport': 'Gwport'}
    _shortView =  ()
    _sqlTable =  'gwportprefix'
    _descriptions =  {}

class Location(_Wrapper):
    _sqlFields =  {'locationid': 'locationid', 'descr': 'descr'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('locationid',)
    _shortView =  ()
    _sqlTable =  'location'
    _descriptions =  {}

class Maintenance(_Wrapper):
    _sqlFields =  {'emotd': 'emotdid',
                  'maint_end': 'maint_end',
                  'maint_start': 'maint_start',
                  'maintenanceid': 'maintenanceid',
                  'state': 'state'}
    _sqlLinks =  {}
    _userClasses =  {'emotd': 'Emotd'}
    _sqlPrimary =  ('maintenanceid',)
    _shortView =  ()
    _sqlTable =  'maintenance'
    _descriptions =  {}

class Maintenance_view(_Wrapper):
    _sqlFields =  {'emotd': 'emotdid',
                  'key': 'key',
                  'maint_end': 'maint_end',
                  'maint_start': 'maint_start',
                  'maintenance': 'maintenanceid',
                  'state': 'state',
                  'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'emotd': 'Emotd', 'maintenance': 'Maintenance'}
    _shortView =  ()
    _sqlTable =  'maintenance_view'
    _descriptions =  {}

class Mem(_Wrapper):
    _sqlFields =  {'device': 'device',
                  'memid': 'memid',
                  'memtype': 'memtype',
                  'netbox': 'netboxid',
                  'size': 'size',
                  'used': 'used'}
    _sqlLinks =  {}
    _userClasses =  {'device': 'Device', 'netbox': 'Netbox'}
    _sqlPrimary =  ('memid',)
    _shortView =  ()
    _sqlTable =  'mem'
    _descriptions =  {}

class Module(_Wrapper):
    _sqlFields =  {'descr': 'descr',
                  'device': 'deviceid',
                  'downsince': 'downsince',
                  'model': 'model',
                  'module': 'module',
                  'moduleid': 'moduleid',
                  'netbox': 'netboxid',
                  'up': 'up'}
    _sqlLinks =  {}
    _userClasses =  {'device': 'Device', 'netbox': 'Netbox'}
    _sqlPrimary =  ('moduleid',)
    _shortView =  ()
    _sqlTable =  'module'
    _descriptions =  {}

class Netbox(_Wrapper):
    _sqlFields =  {'cat': 'catid',
                  'device': 'deviceid',
                  'ip': 'ip',
                  'netboxid': 'netboxid',
                  'org': 'orgid',
                  'prefix': 'prefixid',
                  'ro': 'ro',
                  'room': 'roomid',
                  'rw': 'rw',
                  'snmp_agent': 'snmp_agent',
                  'snmp_version': 'snmp_version',
                  'subcat': 'subcat',
                  'sysname': 'sysname',
                  'type': 'typeid',
                  'up': 'up',
                  'upsince': 'upsince',
                  'uptodate': 'uptodate'}
    _sqlLinks =  {}
    _userClasses =  {'cat': 'Cat',
                    'device': 'Device',
                    'org': 'Org',
                    'prefix': 'Prefix',
                    'room': 'Room',
                    'subcat': 'Subcat',
                    'type': 'Type'}
    _sqlPrimary =  ('netboxid',)
    _shortView =  ()
    _sqlTable =  'netbox'
    _descriptions =  {}

class Netbox_vtpvlan(_Wrapper):
    _sqlFields =  {'netbox': 'netboxid', 'vtpvlan': 'vtpvlan'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _shortView =  ()
    _sqlTable =  'netbox_vtpvlan'
    _descriptions =  {}

class Netboxcategory(_Wrapper):
    _sqlFields =  {'category': 'category', 'netbox': 'netboxid'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _shortView =  ()
    _sqlTable =  'netboxcategory'
    _descriptions =  {}

class Netboxinfo(_Wrapper):
    _sqlFields =  {'key': 'key',
                  'netbox': 'netboxid',
                  'netboxinfoid': 'netboxinfoid',
                  'val': 'val',
                  'var': 'var'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _sqlPrimary =  ('netboxinfoid',)
    _shortView =  ()
    _sqlTable =  'netboxinfo'
    _descriptions =  {}

class Netboxmac(_Wrapper):
    _sqlFields =  {'mac': 'mac', 'netbox': 'netboxid'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _shortView =  ()
    _sqlTable =  'netboxmac'
    _descriptions =  {}

class Netboxsnmpoid(_Wrapper):
    _sqlFields =  {'netbox': 'netboxid', 'frequency': 'frequency', 'snmpoid': 'snmpoidid'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox', 'snmpoid': 'Snmpoid'}
    _shortView =  ()
    _sqlTable =  'netboxsnmpoid'
    _descriptions =  {}

class Nettype(_Wrapper):
    _sqlFields =  {'edit': 'edit', 'nettypeid': 'nettypeid', 'descr': 'descr'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('nettypeid',)
    _shortView =  ()
    _sqlTable =  'nettype'
    _descriptions =  {}

class Org(_Wrapper):
    _sqlFields =  {'descr': 'descr',
                  'opt1': 'opt1',
                  'opt2': 'opt2',
                  'opt3': 'opt3',
                  'orgid': 'orgid',
                  'parent': 'parent'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('orgid',)
    _shortView =  ()
    _sqlTable =  'org'
    _descriptions =  {}

class Patch(_Wrapper):
    _sqlFields =  {'cabling': 'cablingid',
                  'patchid': 'patchid',
                  'split': 'split',
                  'swport': 'swportid'}
    _sqlLinks =  {}
    _userClasses =  {'swport': 'Swport', 'cabling': 'Cabling'}
    _sqlPrimary =  ('patchid',)
    _shortView =  ()
    _sqlTable =  'patch'
    _descriptions =  {}

class Prefix(_Wrapper):
    _sqlFields =  {'prefixid': 'prefixid', 'vlan': 'vlanid', 'netaddr': 'netaddr'}
    _sqlLinks =  {}
    _userClasses =  {'vlan': 'Vlan'}
    _sqlPrimary =  ('prefixid',)
    _shortView =  ()
    _sqlTable =  'prefix'
    _descriptions =  {}

class Prefix_active_ip_cnt(_Wrapper):
    _sqlFields =  {'prefix': 'prefixid', 'active_ip_cnt': 'active_ip_cnt'}
    _sqlLinks =  {}
    _userClasses =  {'prefix': 'Prefix'}
    _shortView =  ()
    _sqlTable =  'prefix_active_ip_cnt'
    _descriptions =  {}

class Prefix_max_ip_cnt(_Wrapper):
    _sqlFields =  {'max_ip_cnt': 'max_ip_cnt', 'prefix': 'prefixid'}
    _sqlLinks =  {}
    _userClasses =  {'prefix': 'Prefix'}
    _shortView =  ()
    _sqlTable =  'prefix_max_ip_cnt'
    _descriptions =  {}

class Priority(_Wrapper):
    _sqlFields =  {'description': 'description',
                  'id': 'id',
                  'keyword': 'keyword',
                  'priority': 'priority'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('priority',)
    _shortView =  ()
    _sqlTable =  'priority'
    _descriptions =  {}

class Product(_Wrapper):
    _sqlFields =  {'descr': 'descr',
                  'productid': 'productid',
                  'productno': 'productno',
                  'vendor': 'vendorid'}
    _sqlLinks =  {}
    _userClasses =  {'vendor': 'Vendor'}
    _sqlPrimary =  ('productid',)
    _shortView =  ()
    _sqlTable =  'product'
    _descriptions =  {}

class Room(_Wrapper):
    _sqlFields =  {'descr': 'descr',
                  'location': 'locationid',
                  'opt1': 'opt1',
                  'opt2': 'opt2',
                  'opt3': 'opt3',
                  'opt4': 'opt4',
                  'roomid': 'roomid'}
    _sqlLinks =  {}
    _userClasses =  {'location': 'Location'}
    _sqlPrimary =  ('roomid',)
    _shortView =  ()
    _sqlTable =  'room'
    _descriptions =  {}

class Rrd_datasource(_Wrapper):
    _sqlFields =  {'delimiter': 'delimiter',
                  'descr': 'descr',
                  'dstype': 'dstype',
                  'max': 'max',
                  'name': 'name',
                  'rrd_datasourceid': 'rrd_datasourceid',
                  'rrd_file': 'rrd_fileid',
                  'threshold': 'threshold',
                  'thresholdstate': 'thresholdstate',
                  'units': 'units'}
    _sqlLinks =  {}
    _userClasses =  {'rrd_file': 'Rrd_file'}
    _sqlPrimary =  ('rrd_datasourceid',)
    _shortView =  ()
    _sqlTable =  'rrd_datasource'
    _descriptions =  {}

class Rrd_file(_Wrapper):
    _sqlFields =  {'filename': 'filename',
                  'key': 'key',
                  'netbox': 'netboxid',
                  'path': 'path',
                  'rrd_fileid': 'rrd_fileid',
                  'step': 'step',
                  'subsystem': 'subsystem',
                  'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'subsystem': 'Subsystem', 'netbox': 'Netbox'}
    _sqlPrimary =  ('rrd_fileid',)
    _shortView =  ()
    _sqlTable =  'rrd_file'
    _descriptions =  {}

class Rrddatasourcenetbox(_Wrapper):
    _sqlFields =  {'sysname': 'sysname', 'rrd_datasource': 'rrd_datasourceid', 'descr': 'descr'}
    _sqlLinks =  {}
    _userClasses =  {'rrd_datasource': 'Rrd_datasource'}
    _shortView =  ()
    _sqlTable =  'rrddatasourcenetbox'
    _descriptions =  {}

class Service(_Wrapper):
    _sqlFields =  {'active': 'active',
                  'handler': 'handler',
                  'netbox': 'netboxid',
                  'serviceid': 'serviceid',
                  'up': 'up',
                  'version': 'version'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _sqlPrimary =  ('serviceid',)
    _shortView =  ()
    _sqlTable =  'service'
    _descriptions =  {}

class Serviceproperty(_Wrapper):
    _sqlFields =  {'property': 'property', 'service': 'serviceid', 'value': 'value'}
    _sqlLinks =  {}
    _userClasses =  {'service': 'Service'}
    _shortView =  ()
    _sqlTable =  'serviceproperty'
    _descriptions =  {}

class Snmpoid(_Wrapper):
    _sqlFields =  {'decodehex': 'decodehex',
                  'descr': 'descr',
                  'getnext': 'getnext',
                  'match_regex': 'match_regex',
                  'mib': 'mib',
                  'oidkey': 'oidkey',
                  'oidname': 'oidname',
                  'oidsource': 'oidsource',
                  'snmpoid': 'snmpoid',
                  'snmpoidid': 'snmpoidid',
                  'uptodate': 'uptodate'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('snmpoidid',)
    _shortView =  ()
    _sqlTable =  'snmpoid'
    _descriptions =  {}

class Status(_Wrapper):
    _sqlFields =  {'boksid': 'boksid',
                  'fra': 'fra',
                  'statusid': 'statusid',
                  'til': 'til',
                  'tilstandsfull': 'tilstandsfull',
                  'trap': 'trap',
                  'trapdescr': 'trapdescr',
                  'trapsource': 'trapsource'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('statusid',)
    _shortView =  ()
    _sqlTable =  'status'
    _descriptions =  {}

class Subcat(_Wrapper):
    _sqlFields =  {'subcatid': 'subcatid', 'descr': 'descr', 'cat': 'catid'}
    _sqlLinks =  {}
    _userClasses =  {'cat': 'Cat'}
    _sqlPrimary =  ('subcatid',)
    _shortView =  ()
    _sqlTable =  'subcat'
    _descriptions =  {}

class Subsystem(_Wrapper):
    _sqlFields =  {'name': 'name', 'descr': 'descr'}
    _sqlLinks =  {}
    _userClasses =  {}
    _shortView =  ()
    _sqlTable =  'subsystem'
    _descriptions =  {}

class Swp_netbox(_Wrapper):
    _sqlFields =  {'ifindex': 'ifindex',
                  'misscnt': 'misscnt',
                  'netbox': 'netboxid',
                  'swp_netboxid': 'swp_netboxid',
                  'to_netboxid': 'to_netboxid',
                  'to_swportid': 'to_swportid'}
    _sqlLinks =  {}
    _userClasses =  {'netbox': 'Netbox'}
    _sqlPrimary =  ('swp_netboxid',)
    _shortView =  ()
    _sqlTable =  'swp_netbox'
    _descriptions =  {}

class Swport(_Wrapper):
    _sqlFields =  {'duplex': 'duplex',
                  'ifindex': 'ifindex',
                  'interface': 'interface',
                  'link': 'link',
                  'media': 'media',
                  'module': 'moduleid',
                  'port': 'port',
                  'portname': 'portname',
                  'speed': 'speed',
                  'swportid': 'swportid',
                  'to_netboxid': 'to_netboxid',
                  'to_swportid': 'to_swportid',
                  'trunk': 'trunk',
                  'vlan': 'vlan'}
    _sqlLinks =  {}
    _userClasses =  {'vlan': 'Vlan', 'module': 'Module'}
    _sqlPrimary =  ('swportid',)
    _shortView =  ()
    _sqlTable =  'swport'
    _descriptions =  {}

class Swportallowedvlan(_Wrapper):
    _sqlFields =  {'hexstring': 'hexstring', 'swport': 'swportid'}
    _sqlLinks =  {}
    _userClasses =  {'swport': 'Swport'}
    _shortView =  ()
    _sqlTable =  'swportallowedvlan'
    _descriptions =  {}

class Swportblocked(_Wrapper):
    _sqlFields =  {'swport': 'swportid', 'vlan': 'vlan'}
    _sqlLinks =  {}
    _userClasses =  {'swport': 'Swport', 'vlan': 'Vlan'}
    _shortView =  ()
    _sqlTable =  'swportblocked'
    _descriptions =  {}

class Swportvlan(_Wrapper):
    _sqlFields =  {'direction': 'direction',
                  'swport': 'swportid',
                  'swportvlanid': 'swportvlanid',
                  'vlan': 'vlanid'}
    _sqlLinks =  {}
    _userClasses =  {'swport': 'Swport', 'vlan': 'Vlan'}
    _sqlPrimary =  ('swportvlanid',)
    _shortView =  ()
    _sqlTable =  'swportvlan'
    _descriptions =  {}

class Type(_Wrapper):
    _sqlFields =  {'cdp': 'cdp',
                  'chassis': 'chassis',
                  'cs_at_vlan': 'cs_at_vlan',
                  'descr': 'descr',
                  'frequency': 'frequency',
                  'sysobjectid': 'sysobjectid',
                  'tftp': 'tftp',
                  'typeid': 'typeid',
                  'typename': 'typename',
                  'vendor': 'vendorid'}
    _sqlLinks =  {}
    _userClasses =  {'vendor': 'Vendor'}
    _sqlPrimary =  ('typeid',)
    _shortView =  ()
    _sqlTable =  'type'
    _descriptions =  {}

class Usage(_Wrapper):
    _sqlFields =  {'usageid': 'usageid', 'descr': 'descr'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('usageid',)
    _shortView =  ()
    _sqlTable =  'usage'
    _descriptions =  {}

class Vendor(_Wrapper):
    _sqlFields =  {'vendorid': 'vendorid'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('vendorid',)
    _shortView =  ()
    _sqlTable =  'vendor'
    _descriptions =  {}

class Vlan(_Wrapper):
    _sqlFields =  {'description': 'description',
                  'netident': 'netident',
                  'nettype': 'nettype',
                  'org': 'orgid',
                  'usage': 'usageid',
                  'vlan': 'vlan',
                  'vlanid': 'vlanid'}
    _sqlLinks =  {}
    _userClasses =  {'usage': 'Usage', 'org': 'Org', 'nettype': 'Nettype'}
    _sqlPrimary =  ('vlanid',)
    _shortView =  ()
    _sqlTable =  'vlan'
    _descriptions =  {}

class Vp_netbox_grp(_Wrapper):
    _sqlFields =  {'pnetboxid': 'pnetboxid', 'vp_netbox_grp_info': 'vp_netbox_grp_infoid'}
    _sqlLinks =  {}
    _userClasses =  {'vp_netbox_grp_info': 'Vp_netbox_grp_info'}
    _shortView =  ()
    _sqlTable =  'vp_netbox_grp'
    _descriptions =  {}

class Vp_netbox_grp_info(_Wrapper):
    _sqlFields =  {'hideicons': 'hideicons',
                  'iconname': 'iconname',
                  'name': 'name',
                  'vp_netbox_grp_infoid': 'vp_netbox_grp_infoid',
                  'x': 'x',
                  'y': 'y'}
    _sqlLinks =  {}
    _userClasses =  {}
    _sqlPrimary =  ('vp_netbox_grp_infoid',)
    _shortView =  ()
    _sqlTable =  'vp_netbox_grp_info'
    _descriptions =  {}

class Vp_netbox_xy(_Wrapper):
    _sqlFields =  {'pnetboxid': 'pnetboxid',
                  'vp_netbox_grp_info': 'vp_netbox_grp_infoid',
                  'vp_netbox_xyid': 'vp_netbox_xyid',
                  'x': 'x',
                  'y': 'y'}
    _sqlLinks =  {}
    _userClasses =  {'vp_netbox_grp_info': 'Vp_netbox_grp_info'}
    _sqlPrimary =  ('vp_netbox_xyid',)
    _shortView =  ()
    _sqlTable =  'vp_netbox_xy'
    _descriptions =  {}



# Prepare them all. We need to send in our local
# namespace.
forgetSQL.prepareClasses(locals())

