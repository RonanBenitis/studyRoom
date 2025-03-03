import model.Cliente;
import view.View;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Cliente cliente = View.login(sc);
        View.menu(sc, cliente);
    }
}