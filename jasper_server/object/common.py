# -*- coding: utf-8 -*-
##############################################################################
#
#    jasper_server module for OpenERP, Management module for Jasper Server
#    Copyright (C) 2011 SYLEAM (<http://www.syleam.fr/>)
#              Christophe CHAUVET <christophe.chauvet@syleam.fr>
#
#    This file is a part of jasper_server
#
#    jasper_server is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasper_server is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import netsvc
from ..report.jasper import report_jasper

_logger = netsvc.Logger()


def registered_report(name):
    """ Register dynamicaly the report for each entry"""
    gname = 'report.' + name
    if netsvc.service_exist(gname):
        if isinstance(netsvc.SERVICES[gname], report_jasper):
            return
        del netsvc.SERVICES[gname]
    report_jasper(gname)
    _logger.notifyChannel('jasper_server', netsvc.LOG_INFO, 'Register the jasper report service [%s]' % name)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
