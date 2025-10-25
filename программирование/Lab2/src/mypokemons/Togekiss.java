package mypokemons;

import ru.ifmo.se.pokemon.*;
import special_moves.FireBlast;
import special_moves.MagicalLeaf;
import status_move.WorkUp;

public class Togekiss extends Pokemon{
    public Togekiss(String name, int level) {
        super(name, level);
        setType(Type.FAIRY, Type.FLYING);
        setStats(85, 50, 95, 120, 115, 80);
        setMove(new WorkUp(), new FireBlast(), new MagicalLeaf(), new FireBlast());
    }
}
