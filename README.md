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
$ docker-compose up   
Recreating openrestry-fulllog_openrestry_1 ... done
Starting openrestry-fulllog_app_1          ... done
Attaching to openrestry-fulllog_app_1, openrestry-fulllog_openrestry_1
app_1         |  * Serving Flask app "main" (lazy loading)
app_1         |  * Environment: production
app_1         |    WARNING: This is a development server. Do not use it in a production deployment.
app_1         |    Use a production WSGI server instead.
app_1         |  * Debug mode: on
app_1         |  * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
app_1         |  * Restarting with stat
app_1         |  * Debugger is active!
app_1         |  * Debugger PIN: 534-421-937
app_1         | 192.168.16.3 - - [21/Nov/2020 16:06:41] "POST /small_res_body HTTP/1.0" 201 -
openrestry_1  | 192.168.16.1 -  [21/Nov/2020:16:06:41 +0000] "POST /small_res_body HTTP/1.1" 201 21 "" "PostmanRuntime/7.26.5" 0.006 "11111111" "" "{\n  \"test\": \"test\"\n}\n"
# 以下、別Terminalで実施し、上記のログが出力
$ curl -XPOST http://127.0.0.1:8000//small_res_body
{
  "test": "test"
}```

## developer向け

python環境を構築しsample-appを変更する(python3/pipenv がinstall済と想定)

```bash
$ git clone https://github.com/kazu0716/openresty-full-log.git
$ cd openrestry-fulllog/sample-app
$ pipenv install --dev

```

 
# Note
 
## appは2つのendpointを有する
  - /small_res_body
    - シンプルなrespomse bodyを返す
  - /large_res_body
    - 数MBのrespomse bodyを返す

## http response headerのlogging
  - ex account_idというresponse headerに関して
    - log_format にて `$sent_http_account_id` といった形で記述すればloggingされる

```
    log_format bodylog escape=json '$remote_addr - $remote_user [$time_local] '
        '"$request" $status $body_bytes_sent '
        '"$http_referer" "$http_user_agent" $request_time '
        '"$sent_http_account_id" '
        '"$request_body" "$resp_body"';
```

