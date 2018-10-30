#encoding: utf-8
import requests
# import re

def main():

    for i in range(0, 0x3f + 1):

        i_hex = '%02x' % i
        url = 'https://www.xorpd.net/pages/xchg_rax/snip_%s.html' % i_hex
        # print(url)
        page = requests.get(url).content
        # asm = re.findall(r'<pre>.*</pre>', page)
        start = page.find('<pre>')
        end = page.find('</pre>', start + 1)
        asm = page[start + 5 : end]

        print(i_hex)
        print('')
        print(asm)
        print('')
        print('')

        # break


if __name__ == '__main__':
    main()