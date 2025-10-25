import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.Pokemon;
import mypokemons.*;
import special_moves.*;
public class Program2 {
    public static void main(String[] args) {
        Battle b = new Battle();
        Articuno p1 = new Articuno("Чужой", 1);
        Sunkern p2 = new Sunkern("Хищник", 1);
        Sunflora p3 = new Sunflora("Вождь", 1);
        Togepi p4 = new Togepi("Крутой", 1);
        Togetic p5 = new Togetic("Классный", 1);
        Togekiss p6 = new Togekiss("Прикольный", 1);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}
