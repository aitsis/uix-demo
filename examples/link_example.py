from uix.elements import link

def link_example():
    main = link("Ai Ait",href="https://ai.ait.com.tr/",target="_blank",title="Ai Ait Website'sine Git") 
    return main

title = "Link"
description = '''
## link(value,id,href,title,target)
1. Link elementi. Html'deki a elementine karşılık gelir. Sayfaya bağlantı eklemek için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Link elementinin id'si                            |
| value         | Link elementinin yazısı                           |
| href          | Link elementinin href'i                           |
| title         | Kullanıcı linkin üzerine geldiğinde göreceği yazı |
| target        | Linkin açılacağı pencere seçeneği                 |
'''