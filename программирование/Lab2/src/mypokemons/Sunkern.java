package mypokemons;

import physical_moves.Facade;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import status_move.Growth;
import status_move.SwordsDance;

public class Sunkern extends Pokemon{
    public Sunkern(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(30, 30, 30, 30, 30, 30);
        setMove(new Growth(), new Facade(),new SwordsDance());
    }

}
