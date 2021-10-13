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
}