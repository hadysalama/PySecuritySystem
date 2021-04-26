import base64
string = b"b'AN2C9MMFdKyYYfldalUGB5+IBogoMUKnmdEBLHEY2dFsZE3rDrJI76hSHNFWC5INOKhQaF01Vkwn4Ui7JgwtVxZKOFJ2nuRqok2bHWhNjaiEr6LoNypflyOu+p7oApcMnLKoMRSb+jZYSGPDjWMIAf102yIYb6mTOKNSfH0CIZQ7WYLRPgcAoLKMs6Na+CvDWVKi4NbRPwnJi/62gK2BVjjRxHav4jiheJyyuaVmTjTLvD7Q4dWbQTDo9qzzGixDOshEAZ7anB2UYDn+gP8bDAImxvfzBupWjG/PJNjMp0pZmO5nHzJdh96gYM804K24lNCibmSwoaDm0evX3JlGYw=='"
string = string.decode()

str1 = b'HGCsy/903GXRF+KPJj2k+5tSRuRruRQk5uRTr2ZI+V2kLQVxM+6H6TdBUnqBv2MgaUnan1rD7hqcsexeENX3wB6sAP98nsQy7uOX6W52oIvwCSRyO4uRs26tATvI1qH0isp4X5dsC4LHpMlmQaWHxXzDsMNy5eoGCv/JmF9U5JuZKXnGT54f8CWqTOksUe8JPkurVqtwiYPrtxsMJYxhbVQ6GZR/UBd0xK7Igo3f/EzyLJa+N1Gn1DVXFLde48/MP0hIOHwIx+5s0Ax08qv6smwNhEH6tkkKHgBccftLQHGFjO/5zTpYdK3dHSpJ4UtwEC7XOfS+8F6r29AGZKXSsg=='

str2 = b'HGCsy/903GXRF+KPJj2k+5tSRuRruRQk5uRTr2ZI+V2kLQVxM+6H6TdBUnqBv2MgaUnan1rD7hqcsexeENX3wB6sAP98nsQy7uOX6W52oIvwCSRyO4uRs26tATvI1qH0isp4X5dsC4LHpMlmQaWHxXzDsMNy5eoGCv/JmF9U5JuZKXnGT54f8CWqTOksUe8JPkurVqtwiYPrtxsMJYxhbVQ6GZR/UBd0xK7Igo3f/EzyLJa+N1Gn1DVXFLde48/MP0hIOHwIx+5s0Ax08qv6smwNhEH6tkkKHgBccftLQHGFjO/5zTpYdK3dHSpJ4UtwEC7XOfS+8F6r29AGZKXSsg=='

str3 = b'HGCsy/903GXRF+KPJj2k+5tSRuRruRQk5uRTr2ZI+V2kLQVxM+6H6TdBUnqBv2MgaUnan1rD7hqcsexeENX3wB6sAP98nsQy7uOX6W52oIvwCSRyO4uRs26tATvI1qH0isp4X5dsC4LHpMlmQaWHxXzDsMNy5eoGCv/JmF9U5JuZKXnGT54f8CWqTOksUe8JPkurVqtwiYPrtxsMJYxhbVQ6GZR/UBd0xK7Igo3f/EzyLJa+N1Gn1DVXFLde48/MP0hIOHwIx+5s0Ax08qv6smwNhEH6tkkKHgBccftLQHGFjO/5zTpYdK3dHSpJ4UtwEC7XOfS+8F6r29AGZKXSsg=='

print(str1 == str2 == str3)



raw_key = b'C\xbbNTl~\xe6c\xb3}\xb1\xaa;\xc4\xabX\xc1v\xe3t\xe5\xc8\xc5\xc2\xaa\r\x9ek\\\x17v\xf7'

cipher_text = b"m\x07\xfa!F\x08\xd1\xbd5\x058\x152\x17\xf8\x8d\xc5\xb8\x1f*\xc5\xb0\tT]]M\x86\xdb`\xe7\xb1\xdb\xde\x9c\xde\xd3\xc0\x1eh\x880a>fF\x82\x80'\xfe=a\xdd\xaf\x97^\xa1\xb5K\xe38T\xe2\xa3\\\xbcU\t\xe5\xe5\x93\x91\xb4\xf8\xa2J\xd2P\xa89\xd2VT\x81%\xde/\xc8\xcb\xe5\r\x8f\x9eQ\x9c\xcd\xf0\xca\xf4\xe2$NX\x05?\t\xfc\xdb\xde\x035\xc4\xee\x8d\x9fwp<yK\x85\xc3\xff\xceyypUf*Q\x8aP}\x9a\xec\x04\xfa\xe7B\xd7\t\x1c[\x0fbW\xf15\xfb\x838\x8dh4\xd4Y\x01\xecc\x1f\xce\xde\x97U\xe3k\xc7\xde\x99:$\x93\xa9H\x03_\xb8p\x9f\xe0c\xc6\xa5\t\x80^q\xfeE\x8a i\xb5\x1bR\x17\xd7g3\xed+*O!\xe2\x8aT\xe5\x90\xb66\xack\xfc\xeddY\xdf\xa9YSe\xfa\xd2\x0b)\xe7\r\xba\x89\xfej\xbbH\xa5\x95^\xd7\xb3\xb0\xb6\x80@\x16t\x8a\x0c\xceG\x9a\x9e\x84u\xd5\x86"

base64_cipher_text = b'bQf6IUYI0b01BTgVMhf4jcW4HyrFsAlUXV1Nhttg57Hb3pze08AeaIgwYT5mRoKAJ/49Yd2vl16htUvjOFTio1y8VQnl5ZORtPiiStJQqDnSVlSBJd4vyMvlDY+eUZzN8Mr04iROWAU/Cfzb3gM1xO6Nn3dwPHlLhcP/znl5cFVmKlGKUH2a7AT650LXCRxbD2JX8TX7gziNaDTUWQHsYx/O3pdV42vH3pk6JJOpSANfuHCf4GPGpQmAXnH+RYogabUbUhfXZzPtKypPIeKKVOWQtjasa/ztZFnfqVlTZfrSCynnDbqJ/mq7SKWVXtezsLaAQBZ0igzOR5qehHXVhg=='

read_cipher_text = b'bQf6IUYI0b01BTgVMhf4jcW4HyrFsAlUXV1Nhttg57Hb3pze08AeaIgwYT5mRoKAJ/49Yd2vl16htUvjOFTio1y8VQnl5ZORtPiiStJQqDnSVlSBJd4vyMvlDY+eUZzN8Mr04iROWAU/Cfzb3gM1xO6Nn3dwPHlLhcP/znl5cFVmKlGKUH2a7AT650LXCRxbD2JX8TX7gziNaDTUWQHsYx/O3pdV42vH3pk6JJOpSANfuHCf4GPGpQmAXnH+RYogabUbUhfXZzPtKypPIeKKVOWQtjasa/ztZFnfqVlTZfrSCynnDbqJ/mq7SKWVXtezsLaAQBZ0igzOR5qehHXVhg=='

base64_decode_cipher_text = b'm\xb4\x1f\xe8\x85\x18#F\xf4\xd4\x14\xe0T\xc8_\xe27\x16\xe0|\xab\x16\xc0%Quu6\x1bm\x83\x9e\xc7ozs{O\x00y\xa2 \xc1\x84\xf9\x99\x1a\n\x00\x9f\xf8\xf5\x87v\xbe]z\x86\xd5/\x8c\xe1S\x8a\x8dr\xf1T\'\x97\x96NF\xd3\xe2\x89+IB\xa0\xe7IYR\x04\x97x\xbf#/\x946>yFs7\xc3+\xd3\x88\x919`\x14\xfc\'\xf3ox\x0c\xd7\x13\xba6}\xdd\xc0\xf1\xe5.\x17\x0f\xff9\xe5\xe5\xc1U\x98\xa9F)A\xf6k\xb0\x13\xeb\x9d\x0b\\$ql=\x89_\xc4\xd7\xee\x0c\xe25\xa0\xd3Qd\x07\xb1\x8c\x7f;z]W\x8d\xaf\x1fzd\xe8\x92N\xa5 \r~\xe1\xc2\x7f\x81\x8f\x1a\x94&\x01y\xc7\xf9\x16(\x81\xa6\xd4mH_]\x9c\xcf\xb4\xac\xa9<\x87\x8a)S\x96B\xd8\xda\xb1\xaf\xf3\xb5\x91g~\xa5eM\x97\xebH,\xa7\x9c6\xea\'\xf9\xaa\xed"\x96U{^\xce\xc2\xda\x01\x00Y\xd2(39\x1ejz\x11\xd7V\x18'

print(cipher_text == base64_decode_cipher_text)