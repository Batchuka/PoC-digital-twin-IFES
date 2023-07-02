Para criar o ambiente da do plc, é necesário usar 'Dockerfile' visto que não há uma imagem pronta no repositório docker. Nesse caso, pegamos o [projeto oficial no GitHub](https://github.com/thiagoralves/OpenPLC_v3), onde o Thiago disponibilizou um 'Dockerfile'. 

> obs: Aqui estamos sucetíveis a uma fragilidade. Digamos que esse método de construção do ambiente não mantem ele atualizado, diferente do node-red onde sempre fazemos o fetch da imagem mais atualizada.

O 'Dockerfile' é um documento descritivo que diz ao Docker como construir a imagem do container. Deixei comentado o significado dos comandos. Entre no mesmo diretório e dê o seguinte comando.

```bash
    docker build -t plc .
```
