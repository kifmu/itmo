package special_moves;

import ru.ifmo.se.pokemon.*;

public class LeafStorm extends SpecialMove{
    public LeafStorm() {
        super(Type.GRASS, 130, 90);
    }
    int isUsed = 0;
    public void applySelfEffects(Pokemon pokemon) {
        if (isUsed <= 3) {
            pokemon.setMod(Stat.SPECIAL_ATTACK, -2);
        }
        isUsed += 1;
    }
    @Override
    protected String describe() {
        return "использует Leaf Storm";
    }
}
