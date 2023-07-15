Para criar o ambiente da planta, não é necesário usar 'Dockerfile' visto que já há uma [imagem pronta](https://nodered.org/docs/getting-started/docker) no repositório docker. A única coisa necessária aqui é rodar o comando:

```bash
    docker run -it -p 1880:1880 -v node_red_data:/data --name planta-nível nodered/node-red
```

Após iniciar o ambiente, suba o projeto da planta que está em *'flows.json'*.