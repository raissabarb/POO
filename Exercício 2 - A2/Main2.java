public class Main2{
  public static void main(String[] arg){
      
    // Chamando os métodos e verificando alguns atributos.
    Carro carro = new Carro();
    float velAce = carro.aceleracao;
    String marcaCarro = carro.marca;
    float precoCarro = carro.preco;
    
    System.out.println(carro.acelerar(velAce));
    System.out.println(carro.frear());
    System.out.println(carro.infoCarro(marcaCarro, precoCarro));
    System.out.println("------------------------------------");
    
    // Criando objetos, alterando atributos e chamando os métodos.
    Carro carroMaria = new Carro();
    carroMaria.marca = "Ford";
    carroMaria.preco = 35520;
    carroMaria.aceleracao = 80;
    
    System.out.println(carroMaria.acelerar(carroMaria.aceleracao));
    System.out.println(carroMaria.frear());
    System.out.println(carroMaria.infoCarro(carroMaria.marca, carroMaria.preco));
    System.out.println("------------------------------------");
    
    Carro carroJoao = new Carro();
    carroJoao.marca = "Honda";
    carroJoao.preco = 95500;
    carroJoao.aceleracao = 110;
    
    System.out.println(carroJoao.acelerar(carroJoao.aceleracao));
    System.out.println(carroJoao.frear());
    System.out.println(carroJoao.infoCarro(carroJoao.marca, carroJoao.preco));
  }
}