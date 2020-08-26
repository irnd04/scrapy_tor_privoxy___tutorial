# tor, privoxy 설치

    apt install tor
    apt install privoxy

# torrc 작성
    sudo vi /etc/tor/torrc
```
ControlPort 9051   
HashedControlPassword 16:85E4506F6003E05660AEB53C0ED6718AC42017BB9062DBB49208FBE91A
```
    service tor restart

# privoxy config 작성
    sudo vi /etc/privoxy/config
```
forward-socks5 / 127.0.0.1:9050 .
forward-socks4a / 127.0.0.1:9050 .
```
    service privoxy restart

# python lib 설치
    pip install scrapy
    pip install toripchanger
    pip install fake-useragent

# 스크래피 실행
    scrapy crawl quotes
