package special_moves;

import ru.ifmo.se.pokemon.*;

public class MagicalLeaf extends SpecialMove{
    public MagicalLeaf() {
        super(Type.GRASS, 60, Double.POSITIVE_INFINITY);
    }
    @Override
    protected boolean checkAccuracy(Pokemon att, Pokemon def) {
        return true;
    }
    @Override
    protected String describe() {
        return "использует Magical Leaf";
    }
}
