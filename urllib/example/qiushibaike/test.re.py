#!/usr/bin/env python3.6
import re
s = """<div class="author clearfix">
<a href="/users/16441997/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1644/16441997/thumb/20170219231144.JPEG?imageView2/1/w/90/h/90" alt="国家大妓院院长">
</a>
<a href="/users/16441997/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
国家大妓院院长
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>"""

print(s)

pattern =re.compile(r'<div.*?class="author.*?</a>.*?<a.*?<h2>(.*?)</h2>',re.S)
res = re.findall(pattern,s)

print(res)

page = 1

ss = "a"+ str(page)

print(ss)