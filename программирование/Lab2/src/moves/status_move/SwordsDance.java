package status_move;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.StatusMove;

public class SwordsDance extends StatusMove{
    public SwordsDance() {
    }
    int isUsed = 0;
    public void applySelfEffects(Pokemon pokemon) {
        if (isUsed <= 3) {
            pokemon.setMod(Stat.ATTACK, 2);
        } 
        isUsed += 1;
    }
    @Override
    protected String describe() {
        return "использует Swords Dance";
    }
}
