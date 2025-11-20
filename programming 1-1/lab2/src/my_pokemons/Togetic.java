package src.my_pokemons;

import special_moves.*;
import ru.ifmo.se.pokemon.*;

public class Togetic extends Togepi{
    public Togetic(String name, int level) {
        super(name,level);
        setType(Type.FAIRY, Type.FLYING);
        setStats(55, 40, 85, 80, 105, 40);
        setMove(new MagicalLeaf());
    }

}
