package src.my_pokemons;

import ru.ifmo.se.pokemon.*;
import special_moves.*;

public class Togekiss extends Togetic{
    public Togekiss(String name, int level) {
        super(name, level);
        setType(Type.FAIRY, Type.FLYING);
        setStats(85, 50, 95, 120, 115, 80);
        setMove(new FireBlast());
    }
}
