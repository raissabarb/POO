/* Para manter o usuário atualizado quanto ao status do carro (ligado/ desligado), ao iniciar o programa eu pergunto
 se é da vontade do usuário ligar o carro. Se a resposta for sim, os passos do exercício anterior são feitos, caso
 contrário, o status já afirma que o carro está desligado. Seguindo esse raciocínio, após cada pergunta feita, o
 status é mostrado na tela e o usuário tem controle de suas "ações" ao longo de todo o programa, sempre sabendo se
 o carro está ligado ou não, como pode ser visto ao executar o arquivo "Main2.java". */

import java.util.Scanner;

public class Main2{
    public static void main(String[] arg){
        
        Scanner input = new Scanner(System.in);
        int opc, statusFinal = 0;
        System.out.print("Deseja ligar o carro? [1 para sim, 0 para não] ");
        opc = input.nextInt();
        Carro carroVerificação = new Carro();
        
        if (opc == 1){
            
            statusFinal = 1;
            
            // Chamando os métodos e verificando alguns atributos.
            Carro carro = new Carro();
            float velAce = carro.aceleracao;
            String marcaCarro = carro.marca;
            float precoCarro = carro.preco;
            int opc2;
            System.out.print(carro.ligar() + "\n");
            System.out.print(carro.status(statusFinal) + "\n");
            
            System.out.print("\n");
            System.out.println(carro.acelerar(velAce));
            System.out.println(carro.frear());
            System.out.println(carro.infoCarro(marcaCarro, precoCarro));
            System.out.print("\n");
            System.out.println("--------------------------------------------------------");
            System.out.print("\n");
            
            System.out.print("-> Deseja manter o carro ligado? [1 para sim, 0 para não] ");
            opc2 = input.nextInt();
            if (opc2 == 0){
                System.out.println(carro.desligar());
                statusFinal = 0;
                System.out.println(carro.status(statusFinal));
                return;
            } else{
                System.out.println(carro.status(statusFinal));
            }
        
            // Criando objetos, alterando atributos e chamando os métodos.
            Carro carroMaria = new Carro();
            carroMaria.marca = "Ford";
            carroMaria.preco = 35520;
            carroMaria.aceleracao = 80;
            int opc3;
            
            System.out.print("\n");
            System.out.println(carroMaria.acelerar(carroMaria.aceleracao));
            System.out.println(carroMaria.frear());
            System.out.println(carroMaria.infoCarro(carroMaria.marca, carroMaria.preco));
            System.out.print("\n");
            System.out.println("--------------------------------------------------------");
            System.out.print("\n");
            
            System.out.print("-> Deseja manter o carro ligado? [1 para sim, 0 para não] ");
            opc3 = input.nextInt();
            if (opc3 == 0){
                System.out.println(carroMaria.desligar());
                statusFinal = 0;
                System.out.println(carroMaria.status(statusFinal));
                return;
            } else{
                System.out.println(carroMaria.status(statusFinal));
            }
        
            Carro carroJoao = new Carro();
            carroJoao.marca = "Honda";
            carroJoao.preco = 95500;
            carroJoao.aceleracao = 110;
            int opc4;
            
            System.out.print("\n");
            System.out.println(carroJoao.acelerar(carroJoao.aceleracao));
            System.out.println(carroJoao.frear());
            System.out.println(carroJoao.infoCarro(carroJoao.marca, carroJoao.preco));
            System.out.print("\n");
            System.out.println("--------------------------------------------------------");
            System.out.print("\n");
            
            System.out.print("-> Deseja manter o carro ligado? [1 para sim, 0 para não] ");
            opc4 = input.nextInt();
            if (opc4 == 0){
                System.out.println(carroJoao.desligar());
                statusFinal = 0;
                System.out.println(carroJoao.status(statusFinal));
                return;
            } else{
                statusFinal = 1;
                System.out.println(carroJoao.status(statusFinal));
                return;
            }
        }
        System.out.print(carroVerificação.status(statusFinal));
    }
}