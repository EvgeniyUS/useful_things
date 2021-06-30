from xml.etree import ElementTree as ET
from pprint import pprint
from random import randint

def xml_to_dict(XML=None):
    """
    xml (str) to dict magic
    """
    
    root = ET.fromstring(XML)

    def rec(node):
        tag_dict = dict()
        node_text = node.text.strip() if type(node.text) == str else ''
        if node_text:
            tag_dict['text_value'] = node_text
        #if node.attrib:
        #    tag_dict = dict()
        #    for attr, value in node.attrib.items():
        #        try:
        #            tag_dict[attr] = int(value)
        #        except ValueError:
        #            tag_dict[attr] = value
        #num = 0
        for child in node:
            try:
                tag_dict[child.tag].append(rec(child))
            except KeyError:
                tag_dict[child.tag] = rec(child)
            except AttributeError:
                if type(tag_dict[child.tag]) == dict:
                    tag_dict[child.tag] = [tag_dict[child.tag], rec(child)]
                else:
                    tag_dict[child.tag+'_tag_{}'.format(num)] = rec(child)
                    num += 1
        return tag_dict

    pprint({root.tag: rec(root)})


XML = """
<domain type='kvm' id='1'>
  <name>451d9eca-98ba-4871-b3dc-c2eb66d7ad74</name>
  <uuid>451d9eca-98ba-4871-b3dc-c2eb66d7ad74</uuid>
  <metadata>
    <veil:instance xmlns:veil="http://controller/">
      <veil:controller_id>5d6ea142-21f7-45c6-a6c0-f8bf6735ee0e</veil:controller_id>
      <veil:created>2019-09-30 07:38:35.757619+00:00</veil:created>
      <veil:verbose_name>qwerq</veil:verbose_name>
    </veil:instance>
  </metadata>
  <maxMemory slots='16' unit='KiB'>4049920</maxMemory>
  <memory unit='KiB'>2572288</memory>
  <currentMemory unit='KiB'>2572288</currentMemory>
  <vcpu placement='static'>2</vcpu>
  <resource>
    <partition>/machine</partition>
  </resource>
  <os>
    <type arch='x86_64' machine='pc-i440fx-2.12'>hvm</type>
  </os>
  <features>
    <acpi/>
    <apic/>
  </features>
  <cpu>
    <topology sockets='2' cores='1' threads='1'/>
    <numa>
      <cell id='0' cpus='0-1' memory='2572288' unit='KiB'/>
    </numa>
  </cpu>
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <emulator>/usr/bin/kvm</emulator>
    <disk type='file' device='cdrom'>
      <driver name='qemu'/>
      <target dev='hda' bus='ide'/>
      <readonly/>
      <boot order='1'/>
      <alias name='ide0-0-0'/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <controller type='pci' index='0' model='pci-root'>
      <alias name='pci.0'/>
    </controller>
    <controller type='pci' index='1' model='pci-bridge'>
      <model name='pci-bridge'/>
      <target chassisNr='1'/>
      <alias name='pci.1'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </controller>
    <controller type='ide' index='0'>
      <alias name='ide'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
    </controller>
    <controller type='sata' index='0'>
      <alias name='sata0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0'/>
    </controller>
    <controller type='usb' index='0' model='nec-xhci'>
      <alias name='usb'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
    </controller>
    <controller type='virtio-serial' index='0'>
      <alias name='virtio-serial0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </controller>
    <channel type='spicevmc'>
      <target type='virtio' name='com.redhat.spice.0' state='disconnected'/>
      <alias name='channel0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>
    <channel type='spiceport'>
      <source channel='org.spice-space.webdav.0'/>
      <target type='virtio' name='org.spice-space.webdav.0' state='disconnected'/>
      <alias name='channel1'/>
      <address type='virtio-serial' controller='0' bus='0' port='2'/>
    </channel>
    <channel type='unix'>
      <source mode='bind' path='/var/lib/ecp-veil/transport/vm-agents/451d9eca-98ba-4871-b3dc-c2eb66d7ad74.qemu'/>
      <target type='virtio' name='org.qemu.guest_agent.1' state='disconnected'/>
      <alias name='channel2'/>
      <address type='virtio-serial' controller='0' bus='0' port='3'/>
    </channel>
    <channel type='unix'>
      <source mode='bind' path='/var/lib/ecp-veil/transport/vm-agents/451d9eca-98ba-4871-b3dc-c2eb66d7ad74.ovirt'/>
      <target type='virtio' name='com.redhat.rhevm.vdsm' state='disconnected'/>
      <alias name='channel3'/>
      <address type='virtio-serial' controller='0' bus='0' port='4'/>
    </channel>
    <input type='mouse' bus='ps2'>
      <alias name='input0'/>
    </input>
    <input type='keyboard' bus='ps2'>
      <alias name='input1'/>
    </input>
    <graphics type='spice' port='50000' autoport='yes' listen='0.0.0.0'>
      <listen type='address' address='0.0.0.0'/>
      <image compression='auto_glz'/>
      <jpeg compression='auto'/>
      <zlib compression='auto'/>
      <playback compression='on'/>
      <streaming mode='filter'/>
      <mouse mode='client'/>
      <clipboard copypaste='yes'/>
      <filetransfer enable='yes'/>
    </graphics>
    <sound model='ich6'>
      <codec type='micro'/>
      <alias name='sound0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
    </sound>
    <video>
      <model type='virtio' vram='16384' heads='1' primary='yes'/>
      <alias name='video0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
    </video>
    <memballoon model='virtio' autodeflate='on'>
      <stats period='1'/>
      <alias name='balloon0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>
    </memballoon>
  </devices>
  <seclabel type='dynamic' model='dac' relabel='yes'>
    <label>+931:+931</label>
    <imagelabel>+931:+931</imagelabel>
  </seclabel>
</domain>

"""
xml_to_dict(XML)
