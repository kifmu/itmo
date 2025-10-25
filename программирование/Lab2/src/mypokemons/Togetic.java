package mypokemons;

import ru.ifmo.se.pokemon.*;
import special_moves.FireBlast;
import special_moves.MagicalLeaf;
import status_move.WorkUp;

public class Togetic extends Pokemon{
    public Togetic(String name, int level) {
        super(name,level);
        setType(Type.FAIRY, Type.FLYING);
        setStats(55, 40, 85, 80, 105, 40);
        setMove(new WorkUp(), new FireBlast(), new MagicalLeaf());
    }

}
