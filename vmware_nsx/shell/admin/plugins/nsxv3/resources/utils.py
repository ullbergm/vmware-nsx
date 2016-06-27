# Copyright 2016 VMware, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron import context
from neutron.db import db_base_plugin_v2

from vmware_nsx.db import db as nsx_db


class NeutronDbClient(db_base_plugin_v2.NeutronDbPluginV2):
    def __init__(self):
        super(NeutronDbClient, self).__init__()
        self.context = context.get_admin_context()

    def get_ports(self, filters=None, fields=None):
        return super(NeutronDbClient, self).get_ports(
            self.context, filters=filters, fields=fields)

    def get_networks(self, filters=None, fields=None):
        return super(NeutronDbClient, self).get_networks(
            self.context, filters=filters, fields=fields)

    def get_network(self, network_id):
        return super(NeutronDbClient, self).get_network(
            self.context, network_id)

    def get_subnet(self, subnet_id):
        return super(NeutronDbClient, self).get_subnet(self.context, subnet_id)

    def get_lswitch_and_lport_id(self, port_id):
        return nsx_db.get_nsx_switch_and_port_id(self.context.session, port_id)

    def lswitch_id_to_net_id(self, lswitch_id):
        net_ids = nsx_db.get_net_ids(self.context.session, lswitch_id)
        return net_ids[0] if net_ids else None

    def net_id_to_lswitch_id(self, net_id):
        lswitch_ids = nsx_db.get_nsx_switch_ids(self.context.session, net_id)
        return lswitch_ids[0] if lswitch_ids else None