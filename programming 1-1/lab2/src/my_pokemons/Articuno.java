package src.my_pokemons;

import physical_moves.*;
import ru.ifmo.se.pokemon.*;
import special_moves.*;

public class Articuno extends Pokemon{

    public Articuno(String name, int level) {
        super(name, level);
        setType(Type.ICE, Type.FLYING);
        setStats(90, 85, 100, 95, 125, 85);
        setMove(new Hurricane(), new AncientPower(), new FrostBreath(), new AerialAce());
    }
}
