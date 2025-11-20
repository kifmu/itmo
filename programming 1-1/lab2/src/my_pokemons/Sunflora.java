package src.my_pokemons;

import special_moves.*;
import ru.ifmo.se.pokemon.*;

public class Sunflora extends Sunkern{
    public Sunflora(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(75, 75, 105, 55, 85, 30);
        setMove(new LeafStorm());
    }

}
