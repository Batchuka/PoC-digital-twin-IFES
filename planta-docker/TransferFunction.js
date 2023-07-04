// Função de transferência: G(s) = 1.3885 * (20.223 / (s^2 + 3s + 20.223))

// Parâmetros da função
var a = 20.223;
var b = 3;
var c = 20.223;
var gain = 1.3885;

// Entrada do sinal analógico
var input = msg.payload;

// Cálculo da função de transferência
var s = (gain * a) / (Math.pow(input, 2) + (b * input) + c);

// Saída do sinal processado
msg.payload = s;
return msg;
