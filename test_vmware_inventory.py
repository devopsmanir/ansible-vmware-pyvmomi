#!/usr/bin/env python

import json
import pickle
import unittest

from vmware_inventory import VMWareInventory

BASICINVENTORY = {'all': {'hosts': ['foo', 'bar']},
                  '_meta': { 'hostvars': { 'foo': {'hostname': 'foo'},
                                           'bar': {'hostname': 'bar'}}
                           }
                 }

class FakeArgs(object):
    debug = False
    write_dumpfile = None
    load_dumpfile = None
    host = False
    list = True

class TestVMWareInventory(unittest.TestCase):

    def test_host_info_returns_single_host(self):
        vmw = VMWareInventory(load=False)
        vmw.inventory = BASICINVENTORY
        foo = vmw.get_host_info('foo')
        bar = vmw.get_host_info('bar')
        assert foo == {'hostname': 'foo'}
        assert bar == {'hostname': 'bar'}

    def test_show_returns_serializable_data(self):
        fakeargs = FakeArgs()
        vmw = VMWareInventory(load=False)
        vmw.args = fakeargs
        vmw.inventory = BASICINVENTORY
        showdata = vmw.show()        
        serializable = False

        try:
            json.loads(showdata)
            serializable = True
        except:
            pass
        assert serializable
        #import epdb; epdb.st()

    def test_show_list_returns_serializable_data(self):
        fakeargs = FakeArgs()
        vmw = VMWareInventory(load=False)
        vmw.args = fakeargs
        vmw.args.list = True
        vmw.inventory = BASICINVENTORY
        showdata = vmw.show()        
        serializable = False

        try:
            json.loads(showdata)
            serializable = True
        except:
            pass
        assert serializable
        #import epdb; epdb.st()

    def test_show_list_returns_all_data(self):
        fakeargs = FakeArgs()
        vmw = VMWareInventory(load=False)
        vmw.args = fakeargs
        vmw.args.list = True
        vmw.inventory = BASICINVENTORY
        showdata = vmw.show()        
        expected = json.dumps(BASICINVENTORY, indent=2)
        assert showdata == expected

    def test_show_host_returns_serializable_data(self):
        fakeargs = FakeArgs()
        vmw = VMWareInventory(load=False)
        vmw.args = fakeargs
        vmw.args.host = 'foo'
        vmw.inventory = BASICINVENTORY
        showdata = vmw.show()        
        serializable = False

        try:
            json.loads(showdata)
            serializable = True
        except:
            pass
        assert serializable
        #import epdb; epdb.st()

    def test_show_host_returns_just_host(self):
        fakeargs = FakeArgs()
        vmw = VMWareInventory(load=False)
        vmw.args = fakeargs
        vmw.args.list = False
        vmw.args.host = 'foo'
        vmw.inventory = BASICINVENTORY
        showdata = vmw.show()        
        expected = BASICINVENTORY['_meta']['hostvars']['foo']
        expected = json.dumps(expected, indent=2)
        #import epdb; epdb.st()
        assert showdata == expected




if __name__ == '__main__':
    unittest.main()
