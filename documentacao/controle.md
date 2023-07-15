
# Vamos falar de Controle

O objetivo é representar um sistema dinâmico, isso se faz com modelos. Há várias ferramentas para construir modelos:

- Você pode represemtar um sistema através de uma *Equação Diferencial* — spoiler: corra disso!
- Você pode representar um sistema graficamente, através de *Diagrama de blocos* — que só serve para te ajudar a obter uma equação diferencial, então corra disso também;
- Você pode representar um sistema através de uma matriz *Espaço de Estados* — provavelmente é a melhor forma.
- Você pode representar um sistema através de uma *Função de transferência*.


Essa última será o objeto inicial de nossos estudos (depois vamos pensar sobre *Espaços de estados*). Uma função de transferência mostra como algo é transferido de um domínio para outro, e o que é esse algo? **Infomação**! Ela mapeia a informação do domínio do tempo em outros domínios mais interessantes, como o da frequência. Na verdade, o domínio da frequência é tão interessante que existe diferentes domínios de frequência, a saber:

- **Domínio frequência:** que é só o espectro de frequência de um sinal. Nesse domínio você perde a componente do tempo, mas pode visualizar quais são as frequências dominantes do sinal;
  
- **Domínio de Laplace (L):** é um domínio de frequência pensado para transformar operação matemáticas difíceis em fáceis, principalmente, transformar a convolução no tempo em uma operação de multiplicação.
  
- **Domínio de Fourier:** é um domínio de frequência pensado para transformar um sinal em uma coleção de senoides mais básicas e com isso conseguir fazer algumas operações matemáticas interessantes.
  
- **Domínio s (complexo):** é um domínio muito esperto, que foi inventado porque perceberam que se representassemos a frequência, que é um sinal senoidal, em sua forma complexa — todo sinal senoidal pode ser representado de maneira complexa pela forma de Euler — isso iria manter somente características muito substânciais da fonte geradora daquele sinal, de maneira a ser possível saber se ela é ou não um estável, como um sistema dinâmico;

Bom! Aí nós começamos a levantar nossas orelhas, porque é disso que estamos falando aqui. É o que queremos! Saber se uma planta física, dinâmica, louca! É estável... Em última instância, queremos saber como controlar ela de acordo com requisitos de projeto. Mas ainda não está ideal, porque é contínuo e em computação nós não conseguimos lidar com o contínuo. Na computação é tudo digital e sistemas contíniuos são fundamentalmente analógicos!

- **Domínio Z (discreto):** É o domínio de frequência discretizado! O objetivo é transferir amostras do sinal no tempo para seus valores pontuais no domínio da frequência. Logo, a perda aqui é proporcional a sua taxa de amostragem.
  
Ou seja, eu primeiro preciso discretizar meu sinal no tempo para que os computadores possam lidar com ele e depois eu preciso levar para o domínio da frequência para que a teoria de controle possa me dizer algo interessante sobre o sinal. Na prática isso acontece de forma direta, dada uma equação que fala no tempo e gaguejando — através de uma técnica — eu obtenho outra equação que fala outra lingua, a frequência, também gaguejando. 

Acontece que também existem diversas técnicas diferentes de discretizar um sinal de frequência.
