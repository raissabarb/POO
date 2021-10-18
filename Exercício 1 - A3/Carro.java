public class Carro{
    String marca = "Fiat";
    float preco = 48000;
    float aceleracao = 50;
  
    public String infoCarro(String marca, float preco){
        String imprimir1 = "\nMarca: " + marca;
        String imprimir2 = "\nPreço: " + preco;
        return imprimir1 + imprimir2; 
    }

    public String acelerar(float vel){
        String ato = "Acelerando o carro para " + vel + "Km/h!";
        return ato;
    }

    public String frear(){
        String ato2 = "Freando o carro!";
        return ato2;
    }
  
    public String ligar(){
        String carroLigado = "- O carro foi ligado! -\n";
        return carroLigado;
    }
  
    public String desligar(){
        String carroDesligado = "- O carro foi desligado! -\n";
        return carroDesligado;
    }
  
    public String status(int aux){
        if (aux == 1){
            String result1 = "--- O carro está ligado! ---";
            return result1;
        } else{
            String result2 = "--- O carro está desligado! ---";
            return result2;
        }
    }
}