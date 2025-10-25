package mypokemons;

import ru.ifmo.se.pokemon.*;
import special_moves.FireBlast;
import status_move.WorkUp;

public class Togepi extends Pokemon{
    public Togepi(String name, int level) {
        super(name, level);
        setType(Type.FAIRY);
        setStats(35, 20, 65, 40, 65, 20);
        setMove(new WorkUp(), new FireBlast());

    }
    

}
