# QQ_pythonSDK
A python SDK for [go_cqhttp](https://docs.go-cqhttp.org/) basic on websocket.
为go_cqhttp开发的一个python SDK，目前主要实现群聊/私聊消息处理，转化成可直接处理的文字消息。
消息处理使用正向websocket。
类的初步思路：
对于对话，基类是对话类，分为群聊，私聊（暂时不处理临时对话）
对于消息，基类是消息类，分为
