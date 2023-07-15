# Introdução

O objetivo desse projeto é integrar o que seriam o três primeiros componentes convencionais da 'pirâmide de automação'



- extrair empiricamente as características de um sistema dinâmico qualquer através de sua função transferência;
- simular sintonizações de controle e compensação neste sistema (o que implica visualizar o resultado em um supervisório qualquer) e;
- explorar recursos e táticas de procolos de comunicação industrial para controle da planta através de simulação (o protocolo base é o modbus).


Nossa planta de nível é representada pela função de transferência: 


$$ \frac{Y(s)}{U(s)} = \frac{0.9}{63s+ 1} $$

que no tempo pode será:

$$  y(t) = e^{\frac{-t}{63}} $$
