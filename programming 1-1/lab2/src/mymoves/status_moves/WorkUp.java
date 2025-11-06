package status_moves;

import ru.ifmo.se.pokemon.*;

public class WorkUp extends StatusMove{
    public WorkUp() {
    }
    int isUsed = 0;
    public void applySelfEffects(Pokemon pokemon) {
        if (isUsed <= 6) {
            pokemon.setMod(Stat.ATTACK, 1);
            pokemon.setMod(Stat.SPECIAL_ATTACK, 1);
        }
    }
    @Override
    protected String describe() {
        return "использует Work Up";
    }
}
