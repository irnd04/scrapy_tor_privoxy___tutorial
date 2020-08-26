# Ubuntu 환경기준
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

# 참고자료
* https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b
* https://stackoverflow.com/questions/56889999/how-to-rotate-proxies-and-user-agents
