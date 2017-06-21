# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:11:26 2017

@author: admin
"""

    
#App ID: 6822086
#
#API Key: SXoFGdC9VDSWngR2CgcSu5rp
#
#Secret Key: ulf1QYaV17ZCMDBbFQy26SCrQ66cTOw3

#!/usr/bin/python3

import urllib.request
import urllib
import json
import base64
class BaiduRest:
    def __init__(self, 
                 cu_id="6822086", 
                 api_key = "SXoFGdC9VDSWngR2CgcSu5rp",
                 api_secert = "ulf1QYaV17ZCMDBbFQy26SCrQ66cTOw3"):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)

        r_str = urllib.request.urlopen(token_url).read().decode('utf-8')
#        print(r_str)
        token_data = json.loads(r_str)
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        # 2. 向Rest接口提交数据
        # 语音的一些参数
        data = {}
        data['format'] = 'wav'
        data['rate'] = 8000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.request.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8")).read().decode('utf-8')
        
        # 3.处理返回数据
        if 'result' not in r_data:
            print(r_data)
            return 'error'
        else:
            return json.loads(r_data)['result']

if __name__ == "__main__":
    # 我的api_key,供大家测试用，在实际工程中请换成自己申请的应用的key和secert
    api_key = "SXoFGdC9VDSWngR2CgcSu5rp" 
    api_secert = "ulf1QYaV17ZCMDBbFQy26SCrQ66cTOw3"
    # 初始化
    bdr = BaiduRest()
    # 将字符串语音合成并保存为out.mp3
    bdr.getVoice("fangyue", "out.mp3")
    # 识别test.wav语音内容并显示
    print(bdr.getText("out.wav"))
