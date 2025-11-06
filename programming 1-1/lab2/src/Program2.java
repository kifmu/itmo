package src; 

import ru.ifmo.se.pokemon.*;
import src.my_pokemons.*;

public class Program2 {
    public static void main(String[] args) {
        Battle b = new Battle();
        Articuno p1 = new Articuno("Banana", 1);
        Sunkern p2 = new Sunkern("Qiwi", 1);
        Sunflora p3 = new Sunflora("Coconut", 1);
        Togepi p4 = new Togepi("Apple", 1);
        Togetic p5 = new Togetic("Pie", 1);
        Togekiss p6 = new Togekiss("Bee", 1);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}
