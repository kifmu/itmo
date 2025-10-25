package mypokemons;

import physical_moves.AerialAce;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import special_moves.AncientPower;
import special_moves.FrostBreath;
import special_moves.Hurricane;

public class Articuno extends Pokemon{

    public Articuno(String name, int level) {
        super(name, level);
        setType(Type.ICE, Type.FLYING);
        setStats(90, 85, 100, 95, 125, 85);
        setMove(new Hurricane(), new AncientPower(), new FrostBreath(), new AerialAce());
    }
}
