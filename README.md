# openrestry-fulllog
 
openrestryで巨大なresponse bodyをloggingするsample
 
# Features
 
openrestryで巨大なresponse bodyをdockerの標準出力にloggingすることを確認するためのrepo
 
# Requirement
 
- docker
- docker-compose

## developer向け

数MBのresponse bodyを出力するためのアプリ(json fileをresponseとして返す)

- python3.8
- pip
 
# Installation
 
実行環境はMacであることを想定する

- [Dockerのインストールに関して](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- [Docker-Composeのインストールに関して](https://docs.docker.com/docker-for-mac/install/)

```
$ git clone https://github.com/kazu0716/openresty-full-log.git
$ cd openrestry-fulllog
$ docker-compose up -d
$ curl -XPOST http://127.0.0.1:8000/users
[
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 183.26,
        "Year": 2002
    },
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 198.736,
        "Year": 2003
    },
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 200.069,
        "Year": 2004
    },
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 223.737,
        "Year": 2005
    },
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 235.731,
        "Year": 2006
    },
    {
        "Country": "AFG",
        "Indicator": "NGDP_R",
        "Value": 267.177,
        "Year": 2007
    },
 ==省略==
```

## developer向け

python環境を構築しsample-appを変更する(python3/pipenv がinstall済と想定)

```bash
$ git clone https://github.com/kazu0716/openresty-full-log.git
$ cd openrestry-fulllog/sample-app
$ pipenv install --dev

```

 
# Note
 
- `docker-compose logs`でログの出力結果を確認できる

```
$ docker-compose logs
==省略==
ountry\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 930.228, \n    \"Year\": 2009\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1044.497, \n    \"Year\": 2010\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1161.215, \n    \"Year\": 2011\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1152.216, \n    \"Year\": 2012\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1176.475, \n    \"Year\": 2013\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1236.042, \n    \"Year\": 2014\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1038.885, \n    \"Year\": 2015\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1135.765, \n    \"Year\": 2016\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1268.722, \n    \"Year\": 2017\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1350.107, \n    \"Year\": 2018\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1444.495, \n    \"Year\": 2019\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"NGDPDPC\", \n    \"Value\": 1504.154, \n    \"Year\": 2020\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 1.916, \n    \"Year\": 1980\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 1.868, \n    \"Year\": 1981\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 2.091, \n    \"Year\": 1982\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 2.514, \n    \"Year\": 1983\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 2.74, \n    \"Year\": 1984\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 3.051, \n    \"Year\": 1985\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 3.298, \n    \"Year\": 1986\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 3.505, \n    \"Year\": 1987\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 3.902, \n    \"Year\": 1988\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 4.133, \n    \"Year\": 1989\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 4.423, \n    \"Year\": 1990\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 5.045, \n    \"Year\": 1991\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 5.284, \n    \"Year\": 1992\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 5.297, \n    \"Year\": 1993\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 5.707, \n    \"Year\": 1994\n  }, \n  {\n    \"Country\": \"TCD\", \n    \"Indicator\": \"PPPGDP\", \n    \"Value\": 5.781, \n    \"Year\": 1995\n  }\n]\n"
```
