# (c) 2015, Toshio Kuratomi <tkuratomi@ansible.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from six import StringIO

from ansible.compat.tests import unittest
from ansible.executor.connection_info import ConnectionInformation

from ansible.plugins.connections import ConnectionBase
#from ansible.plugins.connections.accelerate import Connection as AccelerateConnection
#from ansible.plugins.connections.chroot import Connection as ChrootConnection
#from ansible.plugins.connections.funcd import Connection as FuncdConnection
#from ansible.plugins.connections.jail import Connection as JailConnection
#from ansible.plugins.connections.libvirt_lxc import Connection as LibvirtLXCConnection
from ansible.plugins.connections.local import Connection as LocalConnection
from ansible.plugins.connections.paramiko_ssh import Connection as ParamikoConnection
from ansible.plugins.connections.ssh import Connection as SSHConnection
#from ansible.plugins.connections.winrm import Connection as WinRmConnection

class TestConnectionBaseClass(unittest.TestCase):

    def setUp(self):
        self.conn_info = ConnectionInformation()
        self.in_stream = StringIO()

    def tearDown(self):
        pass

    def test_subclass_error(self):
        class ConnectionModule1(ConnectionBase):
                pass
        with self.assertRaises(TypeError):
            ConnectionModule1()

        class ConnectionModule2(ConnectionBase):
            def get(self, key):
                super(ConnectionModule2, self).get(key)

        with self.assertRaises(TypeError):
            ConnectionModule2()

    def test_subclass_success(self):
        class ConnectionModule3(ConnectionBase):
            @property
            def transport(self):
                pass
            def _connect(self):
                pass
            def exec_command(self):
                pass
            def put_file(self):
                pass
            def fetch_file(self):
                pass
            def close(self):
                pass
        self.assertIsInstance(ConnectionModule3(self.conn_info, self.in_stream), ConnectionModule3)

#    def test_accelerate_connection_module(self):
#        self.assertIsInstance(AccelerateConnection(), AccelerateConnection)
#
#    def test_chroot_connection_module(self):
#        self.assertIsInstance(ChrootConnection(), ChrootConnection)
#
#    def test_funcd_connection_module(self):
#        self.assertIsInstance(FuncdConnection(), FuncdConnection)
#
#    def test_jail_connection_module(self):
#        self.assertIsInstance(JailConnection(), JailConnection)
#
#    def test_libvirt_lxc_connection_module(self):
#        self.assertIsInstance(LibvirtLXCConnection(), LibvirtLXCConnection)

    def test_local_connection_module(self):
        self.assertIsInstance(LocalConnection(self.conn_info, self.in_stream), LocalConnection)

    def test_paramiko_connection_module(self):
        self.assertIsInstance(ParamikoConnection(self.conn_info, self.in_stream), ParamikoConnection)

    def test_ssh_connection_module(self):
        self.assertIsInstance(SSHConnection(self.conn_info, self.in_stream), SSHConnection)

#    def test_winrm_connection_module(self):
#        self.assertIsInstance(WinRmConnection(), WinRmConnection)
