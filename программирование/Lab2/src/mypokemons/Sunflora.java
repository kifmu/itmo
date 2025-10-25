package mypokemons;

import physical_moves.*;
import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.Type;
import special_moves.LeafStorm;
import status_move.Growth;
import status_move.SwordsDance;

public class Sunflora extends Pokemon{
    public Sunflora(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(75, 75, 105, 55, 85, 30);
        setMove(new Growth(), new Facade(),new SwordsDance(), new LeafStorm());
    }

}
