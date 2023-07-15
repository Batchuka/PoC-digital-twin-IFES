Para desenvolver um supervisório, optei pela versão open source do Grafana, por alguns motivos:

- Principalmente por ser altamente integrável — eu posso integrar com virtualmente qualquer coisa muito facilmente, via plug-in's desenvolvidos pela comunidade do grafana.
- Posso instalar em um container docker facilmente;
- É fácil de construir os dashboars;

No caso, optei por fazer uma integração com websocket por hora, para dispensar o uso de banco de dados. Assim, a comunicação se dá em tempo real e utiliza a mesma filosofia da comunicação da planta com o controlador. 


Não é necessário a construção de Dockerfile, visto que há uma imagem pronta no repositório docker. Nesse caso, pegamos o [a imagem oficial](https://hub.docker.com/r/grafana/grafana) via comando no terminal.


```bash
    docker run -d --name=grafana -p 3000:3000 grafana/grafana
```

Infelizmente, o grafana não permite interação com o ambiente de forma  nativa, isto é, não há uma feature default para que eu possa ajustar parâmetros do controlador PI via Dashboard, por exemplo. Provavelmente há algum plug-in para isso, mas não irei explorar o tema por hora.