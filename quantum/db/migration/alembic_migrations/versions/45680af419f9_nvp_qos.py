# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2013 OpenStack LLC
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
#

"""nvp_qos

Revision ID: 45680af419f9
Revises: 54c2c487e913
Create Date: 2013-02-17 13:27:57.999631

"""

# revision identifiers, used by Alembic.
revision = '45680af419f9'
down_revision = '54c2c487e913'

# Change to ['*'] if this migration applies to all plugins

migration_for_plugins = [
    'quantum.plugins.nicira.nicira_nvp_plugin.QuantumPlugin.NvpPluginV2'
]

from alembic import op
import sqlalchemy as sa


from quantum.db import migration


def upgrade(active_plugin=None, options=None):
    if not migration.should_run(active_plugin, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'qosqueues',
        sa.Column('tenant_id', sa.String(length=255), nullable=True),
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('default', sa.Boolean(), nullable=True),
        sa.Column('min', sa.Integer(), nullable=False),
        sa.Column('max', sa.Integer(), nullable=True),
        sa.Column('qos_marking', sa.Enum('untrusted', 'trusted',
                                         name='qosqueues_qos_marking'),
                  nullable=True),
        sa.Column('dscp', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'networkqueuemappings',
        sa.Column('network_id', sa.String(length=36), nullable=False),
        sa.Column('queue_id', sa.String(length=36), nullable=True),
        sa.ForeignKeyConstraint(['network_id'], ['networks.id'],
                                ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['queue_id'], ['qosqueues.id'],
                                ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('network_id')
    )
    op.create_table(
        'portqueuemappings',
        sa.Column('port_id', sa.String(length=36), nullable=False),
        sa.Column('queue_id', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(['port_id'], ['ports.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['queue_id'], ['qosqueues.id'], ),
        sa.PrimaryKeyConstraint('port_id', 'queue_id')
    )
    ### end Alembic commands ###


def downgrade(active_plugin=None, options=None):
    if not migration.should_run(active_plugin, migration_for_plugins):
        return

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portqueuemappings')
    op.drop_table('networkqueuemappings')
    op.drop_table('qosqueues')
    ### end Alembic commands ###
