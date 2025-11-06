package src.my_pokemons;

import physical_moves.*;
import ru.ifmo.se.pokemon.*;
import status_moves.*;

public class Sunkern extends Pokemon{
    public Sunkern(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(30, 30, 30, 30, 30, 30);
        setMove(new Growth(), new Facade(),new SwordsDance());
    }

}
