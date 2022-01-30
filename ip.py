#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, web
import json



def get_ip_address(url):
    res = web.get(url)
    pattern = re.compile('\d{0,3}\.\d{0.3}\.\d{0,3}\.\d{0,3}')
    # print(res.content)
    # print(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res.content))
    result = re.search(r"<body.*?>(.*?)</body>", res.content).group(1)
    return result
    # space_pos = result.find(' ')
    # return {
    #         'ip': result[:space_pos],
    #         'location':result[space_pos+1:],
    #         }

    return 
def main(wf):
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`
    # import somemodule
    # import anothermodule

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...

    data = {'method': 'login', 'params': ["root", "12qwaszx"]}

    # wf.add_item(u'Thinkpad1', '02:21:C0:E8:44:14', arg='https://www.google.com',
    #         valid=True)

    # wf.add_item(u'从国内测试', get_ip_address('http://ip111.cn'))
    res = web.get('http://ip111.cn')
    wf.add_item(re.search(r"<p>\s*(\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b.*?)</p>", res.content).group(1), u'从国内测试')

    wf.add_item(get_ip_address('http://23.80.5.90/ip.php'), u'从国外测试')

    wf.add_item(get_ip_address('http://sspanel.net/ip.php'), u'从谷歌测试')

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
